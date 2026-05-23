import docx
import sys
import re
import os
from lxml import etree

# Word XML namespace
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

def get_paragraph_text_with_citations(para_element, doc):
    """
    Extract text from a paragraph element, rendering citation field codes as [n].
    Word stores citations as w:fldChar (begin/end) with w:instrText containing
    "CITATION ref_id".
    """
    runs_text = []
    in_field = False
    field_type = None
    field_result_parts = []
    collecting_result = False

    for child in para_element.iter():
        tag = child.tag.split('}')[-1] if '}' in child.tag else child.tag

        if tag == 'fldChar':
            fld_type = child.get(f'{{{W}}}fldCharType')
            if fld_type == 'begin':
                in_field = True
                collecting_result = False
                field_result_parts = []
                field_type = None
            elif fld_type == 'separate':
                collecting_result = True
            elif fld_type == 'end':
                # For any field (CITATION, SEQ, etc.), use the cached result text
                if field_result_parts:
                    result = ''.join(field_result_parts).strip()
                    if result:
                        # Ensure proper spacing if the preceding run didn't have it
                        if runs_text and not runs_text[-1].endswith(' ') and not result.startswith(' '):
                            # Don't add space if the previous text ends with a dot/number 
                            # and the result is a number (e.g. 3.1)
                            if not (re.search(r'[\d\.]$', runs_text[-1].strip()) and re.match(r'^\d', result)):
                                runs_text.append(' ')
                        runs_text.append(result)
                in_field = False
                collecting_result = False
                field_type = None
                field_result_parts = []

        elif tag == 'instrText' and in_field:
            instr = child.text or ''
            if 'CITATION' in instr.upper():
                field_type = 'citation'

        elif tag == 't':
            parent = child.getparent()
            parent_tag = parent.tag.split('}')[-1] if parent is not None and '}' in parent.tag else ''
            if parent_tag == 'instrText':
                continue
            if in_field and collecting_result:
                field_result_parts.append(child.text or '')
            elif not in_field:
                runs_text.append(child.text or '')
        
        elif tag == 'drawing':
            # Identify the image in the drawing element
            try:
                # Find the blip element that links to the image part
                blip = child.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}blip')
                if blip is not None:
                    # Get the rId of the image
                    rid = blip.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                    if rid:
                        image_part = doc.part.related_parts[rid]
                        # We will store the image later, for now append a placeholder
                        runs_text.append(f"\n![[IMAGE_RID:{rid}]]\n")
            except Exception as e:
                pass

    return ''.join(runs_text)


def extract_element_text(element, doc, media_map):
    """Recursively extract text and images from an element."""
    tag = element.tag.split('}')[-1] if '}' in element.tag else element.tag
    
    if tag == 'p':
        # Check for paragraph style (Heading identification)
        style_id = "Normal"
        pPr = element.find(f'{{{W}}}pPr')
        if pPr is not None:
            pStyle = pPr.find(f'{{{W}}}pStyle')
            if pStyle is not None:
                style_id = pStyle.get(f'{{{W}}}val')
        
        # Check for numbering (Auto-numbering CHAPTER/1.1 etc)
        is_numbered = False
        if pPr is not None:
            numPr = pPr.find(f'{{{W}}}numPr')
            if numPr is not None:
                is_numbered = True

        text = get_paragraph_text_with_citations(element, doc)
        if not text or not text.strip():
            return None
            
        # Format based on style
        if style_id.startswith('Heading1') or style_id == 'Heading1':
            prefix = "[CHAPTER] " if is_numbered else ""
            return f"\n# {prefix}{text}\n"
        elif style_id.startswith('Heading2') or style_id == 'Heading2':
            prefix = "[SECTION] " if is_numbered else ""
            return f"\n## {prefix}{text}\n"
        elif style_id.startswith('Heading3') or style_id == 'Heading3':
            prefix = "[SUBSECTION] " if is_numbered else ""
            return f"\n### {prefix}{text}\n"
        
        # Check for Caption styles (Figure/Table)
        if style_id.lower() == 'caption':
            # Format as bold for better identification
            return f"\n**{text}**\n"
        
        # If it's numbered but text doesn't seem to have the number (missing list bullets)
        if is_numbered and not re.match(r'^(CHAPTER|SECTION|\d+\.)', text.upper()):
            return f"* {text}" # Use bullet point for normal lists
            
        return text
    
    elif tag == 'tbl':
        rows = []
        for row in element.findall(f'.//{{{W}}}tr'):
            cells = []
            for cell in row.findall(f'.//{{{W}}}tc'):
                cell_texts = []
                for para in cell.findall(f'{{{W}}}p'):
                    t = get_paragraph_text_with_citations(para, doc)
                    if t.strip():
                        cell_texts.append(t)
                if cell_texts:
                    cells.append(' | '.join(cell_texts))
            if cells:
                rows.append('\t'.join(cells))
        return '\n'.join(rows) if rows else None
    
    elif tag == 'sdt':
        texts = element.xpath('.//*[local-name()="t"]')
        sdt_text = ''.join([t.text for t in texts if t.text])
        if sdt_text.strip():
            formatted = re.sub(r'(\[\d+\])', r'\n\1', sdt_text).strip()
            return formatted
        return None
    
    else:
        texts = element.xpath('.//*[local-name()="t"]')
        other = ''.join([t.text for t in texts if t.text])
        return other if other.strip() else None


def extract_content(docx_path, output_path):
    try:
        doc = docx.Document(docx_path)
        full_content = []
        media_dir = os.path.join(os.path.dirname(output_path), 'media')
        if not os.path.exists(media_dir):
            os.makedirs(media_dir)

        # First pass to extract text with placeholders
        for element in doc.element.body:
            result = extract_element_text(element, doc, {})
            if result:
                full_content.append(result)

        full_text = '\n'.join(full_content)

        # Second pass to save images and replace placeholders
        for rid, part in doc.part.related_parts.items():
            if 'image' in part.content_type:
                ext = part.content_type.split('/')[-1]
                image_filename = f"image_{rid}.{ext}"
                image_path = os.path.join(media_dir, image_filename)
                with open(image_path, 'wb') as f:
                    f.write(part.blob)
                
                # Replace the placeholder in the text
                full_text = full_text.replace(f"![[IMAGE_RID:{rid}]]", f"![{image_filename}](media/{image_filename})")

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_text)
        print(f"Extraction successful: {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_docx.py <input_docx> <output_md>")
    else:
        extract_content(sys.argv[1], sys.argv[2])
