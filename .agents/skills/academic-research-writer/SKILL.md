---
name: academic-research-writer
description: Write academic research documents following academic guidelines with peer-reviewed sources from Google Scholar and other academic databases. Always verify source credibility and generate IEEE standard references. Use for research papers, literature reviews, technical reports, theses, dissertations, conference papers, and academic proposals requiring proper citations and scholarly rigor.
---

# Academic Research Writer

This skill enables creation of high-quality academic research documents with proper scholarly standards, verified peer-reviewed sources, and IEEE-format citations.

## Core Principles

1. **Academic Rigor**: Follow scholarly writing conventions and maintain objectivity.
2. **Source Verification**: Use only peer-reviewed, credible academic sources.
3. **Proper Citation**: Generate accurate IEEE-format references.
4. **Research Integrity**: Ensure all claims are supported by verified sources (check `references/` folder).

## Workflow

### 1. Source Discovery and Verification

Use `web_search` and `extract-metrics` to find and analyze peer-reviewed sources from:
- Google Scholar (scholar.google.com)
- IEEE Xplore (ieeexplore.ieee.org)
- arXiv (arxiv.org)

**Verification Checklist:**
- [ ] Published in peer-reviewed journal or conference.
- [ ] Author credentials and institutional affiliation.
- [ ] Methodological soundness.

### 2. Document Structure (Standard)

1. **Title, Abstract, Keywords**
2. **Introduction** (Motivation & Problem Statement)
3. **Literature Review** (Research Gap Analysis)
4. **Methodology** (Architecture & Design)
5. **Results & Discussion** (Analysis of extracted metrics)
6. **Conclusion & Future Work**
7. **References** (IEEE format)

### 3. Writing Guidelines (Antigravity Style)

- **Tone**: Formal, objective, and neutral. Use passive voice for methodology.
- **Precision**: Use specific numbers and metrics from verified extractions.
- **Citation**: Use the **`[Author_Year]`** format in drafts for easier modular syncing.

## IEEE Reference Format Patterns

**Journal Article:**
`[1] A. Author, B. Author, and C. Author, "Title of article," Journal Name, vol. X, no. Y, pp. ZZ-ZZ, Month Year.`

**Conference Paper:**
`[2] A. Author and B. Author, "Title of paper," in Proc. Conference Name, City, Country, Year, pp. ZZ-ZZ.`

## Quality Assurance

- [ ] Clear research objectives.
- [ ] Logical flow and organization.
- [ ] All claims supported by citations in `references/`.
- [ ] No grammar or robotic AI-ism patterns (no em-dashes).
