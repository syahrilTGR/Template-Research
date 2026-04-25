import os
import re
import difflib
from pathlib import Path

# Target the main project draf for comparison
# UPDATE THIS PATH to your actual production .md file (after unpacking docx)
MASTER_MD = REPO_ROOT / "example/my_proposals/main_thesis_production.md"
HANDOFF_DIR = REPO_ROOT / "supportFiles/handoff"
REPORT_PATH = REPO_ROOT / "supportFiles/SYNC_AUDIT_REPORT.md"

# Ground Truth for Project Consistency
# Users should update this block to match their specific research parameters
TRUTH = {
    "expected_classes": 4, 
    "confidence_threshold": 0.80,
    "framework": "Change me in scripts/audit_prose_sync.py"
}

# Mapping filenames to Word Chapter titles
CHAPTER_MAPPING = {
    "01_introduction.md": "INTRODUCTION",
    "02_literature_review.md": "LITERATURE REVIEW",
    "03_methodology.md": "RESEARCH METHODOLOGY"
}

def extract_sections(file_path):
    """Extract ## headers and their content from a markdown file with line numbers."""
    sections = []
    if not os.path.exists(file_path): return sections
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = list(re.finditer(r"^##\s+(.+)$", content, re.MULTILINE))
    for i, match in enumerate(matches):
        header = match.group(1).strip()
        start = match.end()
        end = matches[i+1].start() if i + 1 < len(matches) else len(content)
        text_content = content[start:end].strip()
        line_num = content[:match.start()].count('\n') + 1
        sections.append({"text": header, "line": line_num, "content": text_content})
    return sections

def audit_parameters(master_content):
    """Check for specific numerical/technical parameters in Master MD."""
    results = []
    
    # Example Audit: Number of classes
    found_classes = set(re.findall(r"(\b\d+\b)\s+(?:classes|categories)", master_content, re.IGNORECASE))
    expected = str(TRUTH["expected_classes"])
    
    if expected in found_classes:
        results.append({"feature": "Taxonomy", "expected": expected, "found": expected, "status": "✅ SYNCED"})
    else:
        results.append({"feature": "Taxonomy", "expected": expected, "found": list(found_classes), "status": "❌ OUT-OF-SYNC"})

    return results

def main():
    print(f"🔍 Starting Prose Sync Audit for: {REPO_ROOT.name}")
    if not MASTER_MD.exists():
        print(f"⚠️ Warning: Master MD not found at {MASTER_MD}. Please create it by unpacking your .docx.")
        return

    with open(MASTER_MD, "r", encoding="utf-8") as f:
        master_content = f.read()

    param_results = audit_parameters(master_content)
    
    missing_sections = []
    outdated_prose = []
    for handoff_file, chapter_title in CHAPTER_MAPPING.items():
        handoff_path = HANDOFF_DIR / handoff_file
        headers = extract_sections(handoff_path)
        
        chapter_pattern = rf"#\s+{re.escape(chapter_title)}"
        chapter_match = re.search(chapter_pattern, master_content, re.IGNORECASE)
        
        if not chapter_match:
            missing_sections.append(f"- **{chapter_title}**: Entire chapter missing or title mismatch.")
            continue
            
        chapter_start = chapter_match.end()
        next_chapter = re.search(r"^#\s+", master_content[chapter_start:], re.MULTILINE)
        chapter_end = (chapter_start + next_chapter.start()) if next_chapter else len(master_content)
        chapter_text = master_content[chapter_start:chapter_end]
        
        word_matches = list(re.finditer(r"^##\s+(.+)$", chapter_text, re.MULTILINE))
        word_sections = {}
        for i, match in enumerate(word_matches):
            w_header = match.group(1).strip()
            w_start = match.end()
            w_end = word_matches[i+1].start() if i + 1 < len(word_matches) else len(chapter_text)
            word_sections[re.sub(r'\W+', '', w_header).lower()] = chapter_text[w_start:w_end].strip()
        
        for h in headers:
            header_text = h["text"]
            clean_h = re.sub(r'\W+', '', header_text).lower()
            handoff_uri = f"file:///{handoff_path.as_posix()}#L{h['line']}"
            
            if clean_h not in re.sub(r'\W+', '', chapter_text).lower():
                missing_sections.append(f"- **{chapter_title}**: Missing sub-section [`{header_text}`]({handoff_uri})")
            else:
                word_sect_content = word_sections.get(clean_h)
                if word_sect_content:
                    h_text = re.sub(r'\s+', ' ', h["content"]).strip()
                    w_text = re.sub(r'\s+', ' ', word_sect_content).strip()
                    
                    if len(h_text) > 50 and len(w_text) > 50:
                        h_stripped = re.sub(r'\[.*?\]', '', h_text.lower())
                        w_stripped = re.sub(r'\[.*?\]', '', w_text.lower())
                        
                        similarity = difflib.SequenceMatcher(None, h_stripped, w_stripped).ratio()
                        if similarity < 0.85: 
                            outdated_prose.append(
                                f"- **{chapter_title}** - [`{header_text}`]({handoff_uri}): Similarity **{similarity:.1%}**. Prose may be outdated."
                            )

    summary_status = "❌ OUT-OF-SYNC" if any(r["status"].startswith("❌") for r in param_results) or missing_sections or outdated_prose else "✅ SYNCED"
    
    reportLines = [
        f"# Thesis Sync Audit Report",
        f"\n**Overall Status:** {summary_status}",
        f"\n## 1. Parameter Consistency Audit",
        f"| Feature | Expected (Handoff) | Found (Word/MD) | Status |",
        f"| :--- | :--- | :--- | :--- |"
    ]
    
    for r in param_results:
        reportLines.append(f"| {r['feature']} | {r['expected']} | {r['found']} | {r['status']} |")
        
    reportLines.append(f"\n## 2. Coverage Audit (Missing from Word)")
    reportLines.extend(missing_sections if missing_sections else ["_No missing sections identified._"])
        
    reportLines.append(f"\n## 3. Prose Similarity Audit (Contents Differ)")
    reportLines.extend(outdated_prose if outdated_prose else ["_All sections have a high similarity match._"])
        
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(reportLines))
    
    print(f"✅ Audit complete. Progress tracker: {REPORT_PATH}")

if __name__ == "__main__":
    main()
