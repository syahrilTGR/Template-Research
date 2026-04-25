---
name: thesis-prose
description: >
  Use this explicitly for Chapter drafting or revision when the user asks to write thesis paragraphs.
  Skill untuk menulis, mendraft, atau merevisi bagian thesis dalam bahasa Inggris akademik formal.
---

# Thesis Prose Writing Skill

## When to Activate This Skill

Activate whenever the user asks to:
- Write, draft, or revise any section of the thesis document
- Check or improve the writing style of existing prose
- Convert bullet points or notes into formal paragraph prose
- Continue writing from the last written subsection

## Thesis Identity

**Title:** [Judul Skripsi/Penelitian Anda]
**Author:** [Nama Anda] | [Program Studi, Universitas]
**Language:** English (academic, formal)
**Citation style:**
- **Default**: IEEE numbered `[n]` at the end of sentences.
- **Optional (if requested)**: Author-date `[Author, Year]`
**Reference rule:** Only cite papers verified in `papers/index.md` or `supportFiles/ANTI_HALLUCINATION.md`. **No hallucinated references.**

## Mandatory Output Requirements

- Language: English — academic, formal, objective
- NO em dash (—) anywhere in prose — this is a dead giveaway of AI writing
- NO bullet points in thesis prose — paragraph structure only
- NO bold headers within the body of the paragraph
- NO italic for English technical terms (italic only for non-English terms or *et al.*)
- Do NOT mention researcher names in prose (avoid: "Author et al. showed that...")
- Focus on findings and methodology; integrate citations naturally at the end of sentences
- Paragraph structure: topic sentence → supporting sentences → closing/transition → [citation]
- Tone: objective and technical — do NOT use first person ("I", "we", "our")

## Interaction Style
1. Begin with the **core answer or key point**.
2. Follow with a **structured explanation** (headings/lists).
3. Provide **practical implementation suggestions** when relevant.
4. Ask **clarifying questions** if additional information is needed.
5. Avoid **unnecessary verbosity**.

## Citation Safety Rules (NON-NEGOTIABLE)

- NEVER generate a citation that is not present in the Reference Map or the `papers/index.md`.
- If a claim requires a citation but the specific paper has not been confirmed or is missing from the workspace, write: `[CITATION NEEDED]`.
- Do NOT infer author names, years, or titles from memory — only use what is explicitly documented in the workspace.
- Cite papers naturally at the end of sentences, e.g., "...resulted in significant accuracy improvements [8]."

## Thesis Reference Structure

```
BAB II  LITERATURE REVIEW
  2.1  Previous Research
  2.2  Theoretical Framework
       [Sesuaikan dengan kerangka teori proyek Anda]
```

## Current Writing Status

Always read `supportFiles/handoff.md` at the start to get the current prose status. Do not assume which subsections have been written — verify from the handoff file.

## Background Framing (Required)

Any background or introduction paragraph about this research must state:
1. [Konteks Isu Utama 1]
2. [Fokus Solusi Penelitian 2]
3. [Alasan pemilihan metode 3]
