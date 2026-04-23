import os
import shutil
import json
import pdfplumber
from pypdf import PdfReader
import pandas as pd

# Tentative OCR support (requires Tesseract and pdf2image)
try:
    import pytesseract
    from pdf2image import convert_from_path
    OCR_AVAILABLE = True
except ImportError:
    OCR_AVAILABLE = False

# --- Universal Configuration ---
# Menggunakan path relatif agar bisa dijalankan di komputer mana pun
base_dir = os.getcwd()
reference_dir = os.path.join(base_dir, "references")
output_dir = os.path.join(base_dir, "supportFiles", "extracted_pdfs")
tables_dir = os.path.join(base_dir, "supportFiles", "extracted_tables")

os.makedirs(output_dir, exist_ok=True)
os.makedirs(tables_dir, exist_ok=True)

# Collect all PDFs recursively
pdf_items = []
if os.path.exists(reference_dir):
    for root, dirs, files in os.walk(reference_dir):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_items.append(os.path.join(root, file))
else:
    print(f"Warning: Directory {reference_dir} not found.")

total_pdfs = len(pdf_items)
print(f"Found {total_pdfs} PDF files in {reference_dir}.", flush=True)

# --- Protocol: Incremental Cache Pruning ---
expected_txt_names = {os.path.basename(p).replace(".pdf", ".txt").replace(".PDF", ".txt") for p in pdf_items}
expected_table_folders = {os.path.basename(p).replace(".pdf", "").replace(".PDF", "") for p in pdf_items}

print("Running auto-prune to remove outdated indices...", flush=True)
# Prune orphaned texts
for existing_file in os.listdir(output_dir):
    if existing_file.endswith(".txt") and existing_file not in expected_txt_names:
        os.remove(os.path.join(output_dir, existing_file))
        print(f"    -> [PRUNED] Orphaned text removed: {existing_file}", flush=True)

# Prune orphaned table folders
for existing_folder in os.listdir(tables_dir):
    folder_path = os.path.join(tables_dir, existing_folder)
    if os.path.isdir(folder_path) and existing_folder not in expected_table_folders:
        shutil.rmtree(folder_path)
        print(f"    -> [PRUNED] Orphaned table folder removed: {existing_folder}", flush=True)

metadata_log = []

for idx, pdf_path in enumerate(pdf_items):
    pdf_name = os.path.basename(pdf_path)
    safe_name = pdf_name.replace('.pdf', '').replace('.PDF', '')
    output_filename = safe_name + ".txt"
    output_path = os.path.join(output_dir, output_filename)
    
    is_cached = os.path.exists(output_path)
    
    if is_cached:
        print(f"[{idx+1}/{total_pdfs}] Skipping {pdf_name} (Cache Hit)", flush=True)
    else:
        print(f"[{idx+1}/{total_pdfs}] Extracting {pdf_name}...", flush=True)
        try:
            text_content = ""
            has_text = False
            
            # 1. Advanced Text & Table Extraction with pdfplumber
            with pdfplumber.open(pdf_path) as pdf:
                for i, page in enumerate(pdf.pages):
                    page_num = i + 1
                    page_text = page.extract_text()
                    
                    if page_text and page_text.strip():
                        text_content += f"--- Page {page_num} ---\n{page_text}\n\n"
                        has_text = True
                    
                    # Table Extraction
                    try:
                        table_settings = {
                            "vertical_strategy": "lines",
                            "horizontal_strategy": "lines",
                            "snap_tolerance": 3,
                            "intersection_tolerance": 15
                        }
                        tables = page.extract_tables(table_settings)
                        for j, table in enumerate(tables):
                            if table and len(table) > 1:
                                # Header logic: use first row as header
                                df = pd.DataFrame(table[1:], columns=table[0])
                                
                                paper_tables_dir = os.path.join(tables_dir, safe_name)
                                os.makedirs(paper_tables_dir, exist_ok=True)
                                
                                table_filename = f"{safe_name}_Page{page_num}_Table{j+1}.xlsx"
                                table_path = os.path.join(paper_tables_dir, table_filename)
                                
                                df.to_excel(table_path, index=False, engine='openpyxl')
                                print(f"    -> Extracted Table to: {safe_name}/{table_filename}", flush=True)
                    except Exception as table_err:
                        print(f"    -> Warning: Table extraction error on page {page_num}: {table_err}", flush=True)
            
            # 2. OCR Fallback for Scanned Documents (Optional)
            if not has_text and OCR_AVAILABLE:
                print(f"    -> Warning: No text found in {pdf_name}. Attempting OCR fallback...", flush=True)
                try:
                    images = convert_from_path(pdf_path)
                    for i, image in enumerate(images):
                        text_content += f"--- Page {i+1} (OCR) ---\n"
                        text_content += pytesseract.image_to_string(image) + "\n\n"
                    print(f"    -> OCR Fallback successful.", flush=True)
                except Exception as ocr_err:
                    print(f"    -> OCR Fallback failed: {ocr_err}", flush=True)
            elif not has_text and not OCR_AVAILABLE:
                text_content = f"--- [ERROR] ---\nNo text found in {pdf_name} and OCR libraries (pytesseract/pdf2image) are not installed."

            # Write final text output
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text_content)
                
        except Exception as e:
            print(f"  -> Error processing {pdf_name}: {e}", flush=True)
            
    # 3. Metadata Extraction with pypdf
    try:
        reader = PdfReader(pdf_path)
        meta = reader.metadata
        meta_info = {
            "filename": pdf_name,
            "title": meta.title if meta and hasattr(meta, 'title') else None,
            "author": meta.author if meta and hasattr(meta, 'author') else None,
            "pages": len(reader.pages)
        }
        metadata_log.append(meta_info)
    except Exception:
        pass

# Save metadata registry
metadata_path = os.path.join(output_dir, "reference_metadata.json")
if metadata_log:
    with open(metadata_path, "w", encoding="utf-8") as mfile:
        json.dump(metadata_log, mfile, indent=4)
    
print(f"\n[SUCCESS] Extracted text saved to {output_dir}", flush=True)
print(f"[SUCCESS] Extracted tables saved to {tables_dir}", flush=True)
print("Smart Academic Extractor protocol complete.", flush=True)
