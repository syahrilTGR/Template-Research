import re
import os

# CONFIGURATION
# Modular approach: scan everything in handoff directory
HANDOFF_DIR = "supportFiles/handoff"
ANTI_HALLUCINATION_PATH = "supportFiles/ANTI_HALLUCINATION.md"

# DETECTION PATTERNS
FORBIDDEN_WORDS = ["furthermore", "in conclusion", "moreover", "consequently"]
FORBIDDEN_CHARS = ["—"]  # Em-dash
CITATION_PATTERN = r"\[([A-Za-z]+_[0-9]{4})\]"

def audit_file(file_path, valid_citations):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"🔍 Auditing: {file_path}")
    warnings = 0

    # 1. Check for AI Signatures (Em-dash)
    for char in FORBIDDEN_CHARS:
        if char in content:
            print(f"  ⚠️ WARNING: Found Forbidden Char '{char}' (AI Signature detected).")
            warnings += 1

    # 2. Check for Overused AI Transitions
    for word in FORBIDDEN_WORDS:
        if re.search(r'\b' + re.escape(word) + r'\b', content, re.IGNORECASE):
            print(f"  ⚠️ WARNING: Found AI transition word '{word}'.")
            warnings += 1

    # 3. Check for Bullet Points in Prose sections
    # Look for sections starting with ## Prose or ## CHAPTER/BAB
    draft_sections = re.findall(r"(?:###? (?:Prose|CHAPTER|BAB|##)).*?((?=\s###? )|$)", content, re.DOTALL)
    for section in draft_sections:
        if re.search(r"^\s*[\*\-]\s", section, re.MULTILINE):
            print(f"  ⚠️ WARNING: Bullet points detected in a prose section. Prose should be flowing paragraphs.")
            warnings += 1

    # 4. Check for Citation Integrity
    found_citations = re.findall(CITATION_PATTERN, content)
    for cit in found_citations:
        tag = f"[{cit}]"
        # We also check if it's in our metadata bibliography if it exists
        if tag not in valid_citations:
            print(f"  ❌ ERROR: Unregistered Citation found: {tag}. Add it to ANTI_HALLUCINATION.md or references!")
            warnings += 1
    
    return warnings

def audit_prose():
    if not os.path.exists(HANDOFF_DIR):
        print(f"❌ Error: {HANDOFF_DIR} not found.")
        return

    if not os.path.exists(ANTI_HALLUCINATION_PATH):
        # Create empty if missing
        with open(ANTI_HALLUCINATION_PATH, "w", encoding="utf-8") as f:
            f.write("# ANTI-HALLUCINATION\n")

    with open(ANTI_HALLUCINATION_PATH, "r", encoding="utf-8") as f:
        valid_citations = f.read()

    total_warnings = 0
    files_audited = 0

    # Scan recursive
    for root, dirs, files in os.walk(HANDOFF_DIR):
        for file in files:
            if file.endswith(".md") and "metadata" not in file.lower():
                file_path = os.path.join(root, file)
                total_warnings += audit_file(file_path, valid_citations)
                files_audited += 1

    print("-" * 30)
    if total_warnings == 0:
        print(f"✅ Prose Audit: CLEAN (Scanned {files_audited} files). Excellent academic quality!")
    else:
        print(f"\n📊 Total issues found: {total_warnings} across {files_audited} files.")

if __name__ == "__main__":
    audit_prose()
