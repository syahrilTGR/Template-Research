import xml.etree.ElementTree as ET
import sys
import os

def extract_code_perfect(docx_unpacked_path):
    """
    Extracts code blocks from an unpacked docx directory based on:
    1. Paragraph Shading (for dark themes)
    2. Font Face (Consolas or Courier New)
    """
    doc_xml = os.path.join(docx_unpacked_path, "word", "document.xml")
    if not os.path.exists(doc_xml):
        print(f"Error: {doc_xml} not found.")
        return

    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    tree = ET.parse(doc_xml)
    root = tree.getroot()
    
    code_lines = []
    for p in root.findall('.//w:p', ns):
        # Check shading (Dark Theme)
        pPr = p.find('w:pPr', ns)
        is_code = False
        
        if pPr is not None:
            shd = pPr.find('w:shd', ns)
            if shd is not None and shd.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fill') not in ['auto', 'FFFFFF', None]:
                is_code = True
            
            # Check fonts (Generic Code Fonts)
            rfonts = p.find('.//w:rFonts', ns)
            if rfonts is not None:
                ascii_f = rfonts.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ascii')
                if ascii_f in ['Consolas', 'Courier New', 'Monaco', 'Lucida Console']:
                    is_code = True

        if is_code:
            text = "".join([t.text for t in p.findall('.//w:t', ns) if t.text])
            # Handle non-breaking spaces and tabs
            text = text.replace('\u00A0', ' ')
            code_lines.append(text)
    
    if code_lines:
        print("\n--- EXTRACTED CODE BLOCK ---")
        print("\n".join(code_lines))
        print("--- END OF BLOCK ---\n")
    else:
        print("No code block detected using current heuristics.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_code.py [unpacked_docx_folder]")
    else:
        extract_code_perfect(sys.argv[1])
