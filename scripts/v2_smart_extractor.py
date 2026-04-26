import os
import shutil
import json
import re
import sys
import tempfile
import pandas as pd
import pdfplumber
import pytesseract
from pdf2image import convert_from_path
from markitdown import MarkItDown
from pypdf import PdfReader, PdfWriter
from concurrent.futures import ProcessPoolExecutor, as_completed

# --- Configuration (Generic for Template) ---
BASE_DIR = os.getcwd()
REFERENCE_DIR = os.path.join(BASE_DIR, "references")
OUTPUT_DIR = os.path.join(BASE_DIR, "supportFiles", "extracted_pdfs")
TABLES_DIR = os.path.join(BASE_DIR, "supportFiles", "extracted_tables")

def standalone_worker(pdf_path, force=False):
    """
    Independent worker function for ProcessPool.
    Everything is initialized inside the process to avoid serialization issues.
    """
    pdf_name = os.path.basename(pdf_path)
    safe_name = pdf_name.replace('.pdf', '').replace('.PDF', '')
    output_path_standard = os.path.join(OUTPUT_DIR, safe_name + ".md")
    output_folder_chunked = os.path.join(OUTPUT_DIR, safe_name)
    
    if not force:
        if os.path.exists(output_path_standard) or os.path.exists(output_folder_chunked): 
            return None

    try:
        # Initialize engines inside the process
        md_engine = MarkItDown()
        
        reader = PdfReader(pdf_path)
        pdf_source = pdf_path
        temp_files = []

        # Decryption logic
        if reader.is_encrypted:
            try:
                reader.decrypt("")
                writer = PdfWriter()
                for page in reader.pages: writer.add_page(page)
                tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
                writer.write(tmp.name); tmp.close()
                pdf_source = tmp.name; temp_files.append(tmp.name)
                reader = PdfReader(pdf_source)
            except: pass

        metadata = reader.metadata
        meta_yaml = "---\n"
        if metadata:
            try:
                if getattr(metadata, 'title', None): meta_yaml += f"Title: {metadata.title}\n"
                if getattr(metadata, 'author', None): meta_yaml += f"Author: {metadata.author}\n"
            except: pass
        meta_yaml += "---\n"

        total_pages = len(reader.pages)
        ai_header = f"{meta_yaml}\n## 🧠 AI AUDITOR INSTRUCTION\n> [!IMPORTANT]\n> ALWAYS prioritize the 'DATA APPENDIX' at the end of this document.\n---\n\n"
        tables_found_count = 0

        def _extract_page_data(p_source, p_safe_name, offset=0):
            b_content = ""
            # 1. MarkItDown
            try:
                res = md_engine.convert(p_source)
                b_content = res.text_content
            except: pass

            # 2. OCR Fallback
            if len(b_content.strip()) < 200:
                try:
                    images = convert_from_path(p_source)
                    ocr_pieces = []
                    for i, img in enumerate(images):
                        txt = pytesseract.image_to_string(img, config='--psm 1')
                        ocr_pieces.append(f"## Page {offset + i + 1}\n{txt}")
                    b_content = "\n\n".join(ocr_pieces)
                except: pass

            # 3. Table Extractor
            t_md = []
            try:
                with pdfplumber.open(p_source) as pdf:
                    for i, page in enumerate(pdf.pages):
                        pg_num = offset + i + 1
                        tabs = page.extract_tables() or page.extract_tables(table_settings={"vertical_strategy": "text", "horizontal_strategy": "text", "snap_tolerance": 3})
                        for j, tab in enumerate(tabs or []):
                            if not tab or len(tab) < 2: continue
                            try:
                                clean = [[str(c).replace('\n', ' ').strip() if c is not None else "" for c in row] for row in tab]
                                df = pd.DataFrame(clean)
                                df.dropna(axis=1, how="all", inplace=True)
                                df.dropna(axis=0, how="all", inplace=True)
                                if df.empty or df.shape[1] < 2: continue
                                if df.shape[0] > 1: df.columns = df.iloc[0]; df = df[1:]
                                
                                # Use local storage for table chunks 
                                p_tables_dir = os.path.join(TABLES_DIR, p_safe_name)
                                os.makedirs(p_tables_dir, exist_ok=True)
                                df.to_excel(os.path.join(p_tables_dir, f"{p_safe_name}_P{pg_num}_T{j+1}.xlsx"), index=False)
                                t_md.append({"page": pg_num, "index": j+1, "md": df.to_markdown(index=False)})
                            except: pass
            except: pass
            return b_content, t_md

        # Logic for Chunking vs Standard
        if total_pages > 100:
            os.makedirs(output_folder_chunked, exist_ok=True)
            for chunk_idx in range(0, total_pages, 50):
                cw = PdfWriter()
                ep = min(chunk_idx + 50, total_pages)
                for i in range(chunk_idx, ep): cw.add_page(reader.pages[i])
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    cw.write(tmp.name); tmp.close()
                    bc, tm = _extract_page_data(tmp.name, safe_name, offset=chunk_idx)
                    os.remove(tmp.name)
                
                final = ai_header + bc
                if tm:
                    tables_found_count += len(tm)
                    final += "\n\n---\n## 📊 DATA APPENDIX: EXTRACTED TABLES\n"
                    for en in tm: final += f"\n### TABLE (Source: Page {en['page']}, Index {en['index']})\n{en['md']}\n"
                
                with open(os.path.join(output_folder_chunked, f"Part_{chunk_idx+1}_to_{ep}.md"), "w", encoding="utf-8") as f: f.write(final)
        else:
            bc, tm = _extract_page_data(pdf_source, safe_name)
            final = ai_header + bc
            if tm:
                tables_found_count += len(tm)
                final += "\n\n---\n## 📊 DATA APPENDIX: EXTRACTED TABLES\n"
                for en in tm: final += f"\n### TABLE (Source: Page {en['page']}, Index {en['index']})\n{en['md']}\n"
            with open(output_path_standard, "w", encoding="utf-8") as f: f.write(final)

        for t in temp_files:
            try: os.remove(t)
            except: pass

        return {"filename": pdf_name, "pages": total_pages, "tables_found": tables_found_count}
    except Exception as e:
        return {"filename": pdf_name, "error": str(e)}

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(TABLES_DIR, exist_ok=True)

    pdf_items = []
    for root, _, files in os.walk(REFERENCE_DIR):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_items.append(os.path.join(root, file))
    
    metadata_path = os.path.join(OUTPUT_DIR, "reference_metadata.json")
    all_meta = {}
    if os.path.exists(metadata_path):
        try:
            with open(metadata_path, 'r', encoding='utf-8') as f:
                all_meta = {i['filename']: i for i in json.load(f)}
        except: pass

    jobs = [p for p in pdf_items if not (os.path.exists(os.path.join(OUTPUT_DIR, os.path.basename(p).replace('.pdf', '.md').replace('.PDF', '.md'))) or os.path.exists(os.path.join(OUTPUT_DIR, os.path.basename(p).replace('.pdf', '').replace('.PDF', ''))))]

    if not jobs:
        print("Everything is up to date.")
        return

    print(f"🔥 UNLEASHING MAX POWER: ProcessPool (Parallel) for {len(jobs)} jobs...")
    
    # Using full CPU power
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        future_to_pdf = {executor.submit(standalone_worker, p, False): p for p in jobs}
        
        for idx, future in enumerate(as_completed(future_to_pdf)):
            try:
                res = future.result()
                if res and "error" not in res:
                    all_meta[res['filename']] = res
                    print(f"   [DONE] {res['filename']} ({res['pages']} pgs)")
                elif res:
                    print(f"   [ERROR] {res['filename']}: {res['error']}")
            except Exception as e:
                print(f"   [FATAL] System error: {e}")
                
            if (idx + 1) % 5 == 0 or (idx + 1) == len(jobs):
                with open(metadata_path, 'w', encoding='utf-8') as f:
                    json.dump(list(all_meta.values()), f, indent=4)

    print("\n[SUCCESS] V2.5 Optimization complete.")

if __name__ == "__main__":
    main()
