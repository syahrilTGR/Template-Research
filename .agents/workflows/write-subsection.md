---
description: Use this workflow when the user requests to draft a new section of their thesis. This workflow wraps multiple preparation steps and specifically triggers the thesis-prose skill.
---

1. Read `supportFiles/handoff.md` to understand the current writing status, reference map, and which subsection to write next.
2. Read `papers/index.md` or `supportFiles/ANTI_HALLUCINATION.md` to check which references are available and verified.
3. Read any relevant extracted texts or notes from `papers/` that the subsection requires.
4. **TRIGGER THE `thesis-prose` SKILL** to write the prose in formal academic English using the gathered context.
   - NEVER fabricate any citation not present in the workspace files
5. Output the prose and suggest saving it to the appropriate file in `thesis_bureau/`.
6. After writing, update `supportFiles/handoff.md` to reflect the new subsection status.
