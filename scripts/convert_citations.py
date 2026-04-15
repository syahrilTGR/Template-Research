"""
convert_citations.py
Converts numeric reference citations [n] in academic prose to unambiguous
[AuthorLastname_Year] format based on a dynamic mapping configuration.

Reads mapping from supportFiles/citations_map.json
"""

import os
import json
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP_PATH = os.path.join(BASE_DIR, "supportFiles", "citations_map.json")
HANDOFF_PATH = os.path.join(BASE_DIR, "supportFiles", "handoff.md")

def load_citation_map():
    if not os.path.exists(MAP_PATH):
        print(f"Error: Citation map not found at {MAP_PATH}")
        print("Please create the JSON mapping file first.")
        return {}
    with open(MAP_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def is_prose_or_placeholder_line(line):
    stripped = line.strip()
    if stripped.startswith("|") and "|" in stripped[1:]:
        return False
    return True

def replace_citations(text, citation_map):
    # Sort by length descending to avoid [1] matching inside [10], [11], etc.
    for numeric, author_year in sorted(citation_map.items(), key=lambda x: -len(x[0])):
        text = text.replace(numeric, author_year)
    return text

def main():
    citation_map = load_citation_map()
    if not citation_map:
        return

    if not os.path.exists(HANDOFF_PATH):
        print(f"Error: Target file not found at {HANDOFF_PATH}")
        return

    with open(HANDOFF_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    in_reference_section = False

    for line in lines:
        if "## Reference" in line:
            in_reference_section = True
        
        if in_reference_section:
            new_lines.append(line)
        elif is_prose_or_placeholder_line(line):
            new_lines.append(replace_citations(line, citation_map))
        else:
            new_lines.append(line)

    with open(HANDOFF_PATH, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print("✅ Citation conversion complete!")
    print(f"   Replaced {len(citation_map)} citation types.")

if __name__ == "__main__":
    main()
