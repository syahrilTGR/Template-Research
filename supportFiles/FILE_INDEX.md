# FILE_INDEX.md — Central File Registry
> **Purpose:** Single source of truth for all files in this project. Every new file MUST be registered here.
> **Maintained by:** AI Agent (mandatory per `gemini.md` indexing protocol).
> **Last updated:** 2026-05-28

---

## How to Use This Index

When starting a new session, use this file to answer:
- *"File mana yang relevan untuk tugas X?"*
- *"Apa dependensi file Y?"*
- *"File ini sudah ada atau harus dibuat baru?"*

---

## 📂 Root Directory (`[Your_Project_Path]/`)

| File | Purpose | Read When |
|---|---|---|
| `gemini.md` | **AI Constitution** — mandatory rules, protocols, and project overview for every agent session | Always first |
| `intelligence/_INDEX.md` | Obsidian Map of Content (MOC) — semantic links between thesis drafts and code | Deep architecture research |
| `CREDITS.md` | Atribusi Lisensi & Kredit Open-Source — Penghargaan terhadap perkakas pihak ketiga | Audit lisensi atau pemeriksaan kepatuhan kode |

---

## 📂 `supportFiles/`

### 🔧 Configuration & Project Management

| File | Purpose | Read When |
|---|---|---|
| `FILE_INDEX.md` | **This file** — Central registry of all project files | Start of session |
| `GLOSSARY.md` | Official definitions: AIA, BWT, KDE, τ, etc. | Before using any technical term |
| `open_questions.md` | Unresolved technical & academic questions | Before major decisions |
| `decisions_log.md` | All design decisions + training results log | Cross-checking design choices |
| `revision_progress_tracker.md` | Chapter-level revision checklist (Bab 1–4) | Tracking writing progress |
| `pending_references.md` | Citations flagged as pending/unverified | Before finalizing references |
| `walkthrough.md` | **Activity Log** — Cumulative history of sessions, changes, and key accomplishments | Start of session or audit |
| `word_sync_config.json` | **Word Sync Configuration** — OneDrive and local paths for document synchronization | Before syncing Word drafts |
| `schedule_penelitian.md` | **Thesis Schedule (Gantt Chart)** — 4-month week-by-week timeline for thesis activities | Drafting or revising Bab 3 schedule |

### 📚 Academic Writing & Thesis Drafts

| File | Purpose | Read When |
|---|---|---|
| `DRAFT_PRASKRIPSI_BAB12_ID.md` | Full draft Bab 1 & 2 in Indonesian | Cross-referencing Indonesian context |
| `thesis_writing_guide.md` | Style guide for academic prose (anti-AI-isms) | Before drafting thesis sections |
| `thesis_defense_cheatsheet.md` | Quick reference for seminar/sidang defense | Before proposal defense |
| `thesis_technical_faq.md` | Q&A on technical methodology details | Answering examiner-style questions |
| `Panduan_Sidang_Proposal.md` | Defense presentation guide | Before sempro preparation |
| `audit_proposal_vs_implementation.md` | Discrepancy tracker: proposal draft vs. actual code | Before any cross-chapter alignment |
| `audit_bab3_methodology.md` | Academic review notes for Chapter 3 | Editing Bab 3 methodology |
| `audit_proposal_parameters_v2.md` | Full parameter audit matrix (old → new SOTA values) | Parameter consistency checks |
| `naskah_presentasi_sempro.md` | Naskah panduan (speaker notes) presentasi Sempro | Latihan dan eksekusi sidang Sempro |

### 🧠 Deep-Dive Research Notes

| File | Purpose | Read When |
|---|---|---|
| `deepdive_incremental_learning.md` | Selected IL strategy + scientific rationale | Answering IL methodology questions |
| `deepdive_human_feedback.md` | HITL feedback mechanism, trigger τ, noise handling | Editing HITL-related sections |
| `il_formulas_and_definitions.md` | Mathematical formulas from 3 core papers | Writing formulas in Bab 2/3 |
| `bab2_previous_research_table.md` | Table of 8 papers for Chapter 2 | Drafting 2.1 Previous Research |
| `ground_statement_taxonomy.md` | Ground truth for 7-class taxonomy justification | Taxonomy dispute resolution |
| `DeepDive_Bab2_Sidang.md` | Deep dive analysis for Bab 2 defense context | Bab 2 revision or defense prep |

### 📊 Training & Experiment Reports

| File | Purpose | Read When |
|---|---|---|
| `session_report_yolo_6class.md` | Final YOLOv8n baseline results (6-class) | Referencing Stage 1 metrics |
| `session_report_mobilenetv3_6class.md` | Final MobileNetV3 training report | Referencing Stage 2 metrics |
| `ABLATION_STUDY_FINAL_DOCUMENTATION.md` | Ablation study results and analysis | Writing Bab 4 (Results) |
| `FINAL_VERIFICATION_CONTRASTIVE_LOSS.md` | Verification of contrastive loss implementation | Methodology validation |
| `BAB3_REVISI_BRAIN.md` | Bab 3 revision notes from Brain-Global-Center | Editing Bab 3 |
| `advisor_progress_report_2026_03_30.md` | Advisor meeting notes (2026-03-30) | Tracking advisor feedback |

### 🔄 Sync & Infrastructure

| File | Purpose | Read When |
|---|---|---|
| `ANTIGRAVITY_SYNC_GUIDE.md` | Guide for Antigravity ↔ project sync | Setup or sync troubleshooting |
| `GRAPHRAG_GUIDE.md` | Guide for using Graphify/GraphRAG | Running graph queries |
| `SYNC_GUIDE.md` | General sync procedures | Onboarding or reconnecting |
| `DOCX_SYNC_GUIDE.md` | Word document sync protocol (OneDrive) | Before generating .docx |
| `ANTI_HALLUCINATION.md` | Rules to prevent AI hallucinations in thesis | Quality control review |
| `PROMPT_TEMPLATE.md` | Prompt templates for recurring agent tasks | Writing custom prompts |
| `notebooklm_mcp_setup.md` | Guide for setting up, authenticating, and troubleshooting notebooklm-mcp | Setting up or using NotebookLM integration |
| `.agents/workflows/sync-audit-proposal.md` | Instruction-only manual sync & visual-cognitive proposal audit workflow | Performing manual sync and thesis checks |

---

## 📂 `supportFiles/handoff/`

> **Note:** This directory contains chapter-specific draft snapshots and metadata. It is NOT a project config directory.

| File | Purpose | Read When |
|---|---|---|
| `00_metadata.md` | Metadata and specific information extracted from proposal draft | Cross-checking proposal structure details |
| `01_introduction.md` | Bab 1 draft (original) | Comparing pre/post revision |
| `01_introduction_revised.md` | Bab 1 draft (revised, SOTA-aligned) | Active working draft for Bab 1 |
| `02_literature_review.md` | Bab 2 full draft | Active working draft for Bab 2 |
| `03_methodology.md` | Bab 3 full draft | Active working draft for Bab 3 |
| `03_methodology_revised_SOTA.md` | Bab 3 SOTA revision notes | Parameter update reference for Bab 3 |
| `05_sync_notes_chapters_1_3.md` | Sync notes for Chapters 1–3 alignment | Cross-chapter consistency |
| `09_bibliography.md` | Bibliography / references list | Reference management |
| `thesis_analysis.md` | Holistic analysis of thesis structure | Structural review |
| `surgical_word_update.md` | Precise Word document update instructions | Before editing the .docx manually |


---

## 📂 `supportFiles/extracted_pdfs/`

> Auto-generated `.txt` extractions from PDFs in `references/`. Used for AI context retrieval.

| File Pattern | Source |
|---|---|
| `[Author_Year]_extracted.txt` | Full text from corresponding PDF |

---

## 📂 Scripts & Notebooks (Root-level)

| File | Purpose | Read When |
|---|---|---|
| `scripts/sync_word.ps1` | Sync Word .docx from OneDrive to local path | Before working with .docx files |
| `scripts/sync_project.py` | Semantic auto-linker (draft ↔ code) | Architecture research |
| `.agents/skills/graphify/scripts/sync_brain_comprehensive.py` | Comprehensive GraphRAG + AST sync orchestrator | After any significant file creation |

---

## 📝 Indexing Template (Use This for New Files)

When registering a new file, append a row to the relevant table above using this format:

```markdown
| `path/to/new_file.ext` | [One-line purpose description] | [Trigger condition for reading] |
```

And include this block **inside the new file itself** (placed at the very top, or directly below the YAML frontmatter if the file requires one, such as workflows under `.agents/workflows/`):

```markdown
## 🔍 File Properties (Inline Index Block)
- **File Path:** `relative/path/to/file.ext`
- **Purpose:** [What this file does]
- **Functions & Roles:** [Key responsibilities]
- **Upstream Dependencies:** [Files this file depends on]
- **Downstream Dependencies:** [Files/processes that consume this file]
```
