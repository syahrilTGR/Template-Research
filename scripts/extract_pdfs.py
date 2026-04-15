import fitz  # PyMuPDF
import os

# Dynamic paths for Template structure
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
papers_dir = os.path.join(base_dir, "papers")
output_dir = os.path.join(base_dir, "supportFiles", "extracted_pdfs")

os.makedirs(output_dir, exist_ok=True)
os.makedirs(papers_dir, exist_ok=True)

pdf_files = [f for f in os.listdir(papers_dir) if f.lower().endswith(".pdf")]

print(f"Found {len(pdf_files)} PDF files in {papers_dir}.")

for pdf_name in pdf_files:
    pdf_path = os.path.join(papers_dir, pdf_name)
    output_filename = pdf_name.replace(".pdf", ".txt")
    output_path = os.path.join(output_dir, output_filename)
    
    # Skip if already extracted
    if os.path.exists(output_path):
        continue

    print(f"Extracting {pdf_name}...")
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"  -> Saved to {output_filename}")
    except Exception as e:
        print(f"  -> Error: {e}")

print("Done.")
