import re
import os

# CONFIGURATION
HANDOFF_PATH = "supportFiles/handoff.md"
ANTI_HALLUCINATION_PATH = "supportFiles/ANTI_HALLUCINATION.md"

# DETECTION PATTERNS
FORBIDDEN_WORDS = ["furthermore", "in conclusion", "moreover", "consequently"]
FORBIDDEN_CHARS = ["—"]  # Em-dash
CITATION_PATTERN = r"\[([A-Za-z]+_[0-9]{4})\]"

def audit_prose():
    if not os.path.exists(HANDOFF_PATH):
        print(f"❌ Error: {HANDOFF_PATH} not found.")
        return

    with open(HANDOFF_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"🔍 Auditing Prose in {HANDOFF_PATH}...\n")
    warnings = 0

    # 1. Check for AI Signatures (Em-dash)
    for char in FORBIDDEN_CHARS:
        if char in content:
            print(f"⚠️ WARNING: Found Forbidden Char '{char}' (AI Signature detected).")
            warnings += 1

    # 2. Check for Overused AI Transitions
    for word in FORBIDDEN_WORDS:
        if re.search(r'\b' + re.escape(word) + r'\b', content, re.IGNORECASE):
            print(f"⚠️ WARNING: Found AI transition word '{word}'.")
            warnings += 1

    # 3. Check for Bullet Points in Drafts
    # (Simplified: looks for '*' or '-' at start of lines in the Drafts section)
    draft_section = re.search(r"## ✍️ ACTIVE DRAFTS.*?(?=##|$)", content, re.DOTALL)
    if draft_section:
        if re.search(r"^\s*[\*\-]\s", draft_section.group(0), re.MULTILINE):
            print("⚠️ WARNING: Bullet points detected in ACTIVE DRAFTS. Prose should be in paragraphs.")
            warnings += 1

    # 4. Check for Citation Integrity
    with open(ANTI_HALLUCINATION_PATH, "r", encoding="utf-8") as f:
        valid_citations = f.read()
    
    found_citations = re.findall(CITATION_PATTERN, content)
    for cit in found_citations:
        tag = f"[{cit}]"
        if tag not in valid_citations:
            print(f"❌ ERROR: Unregistered Citation found: {tag}. Add it to ANTI_HALLUCINATION.md!")
            warnings += 1

    if warnings == 0:
        print("✅ Prose Audit: CLEAN. Excellent academic quality!")
    else:
        print(f"\n📊 Total issues found: {warnings}. Please refine the prose.")

if __name__ == "__main__":
    audit_prose()
