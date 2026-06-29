---
name: revision-tracker
description: Parse and manage thesis revision notes, cross-reference them with the tracker, and generate an execution priority plan.
---

# 🔄 Revision Tracker Workflow

## Trigger Conditions
Use this workflow automatically when the user explicitly triggers `/revision-tracker` or asks to manage/plan their thesis or project revisions.

## Workflow Steps

### 1. Ingest Revision Notes
Ask the user to paste the raw revision notes (from examiners or advisors). Wait for their input.

### 2. Parse & Cross-Reference
Once the user provides the notes, perform the following cognitive analysis:
- **Parse**: Break down the notes into distinct, actionable items.
- **Cross-Reference**: Read `supportFiles/revision_progress_tracker.md` to understand the current state of the document and which chapters/sections are affected.
- **Identify Dependencies**: Determine if fixing one item requires fixing another (e.g., changing taxonomy in Chapter 3 requires updates in Chapter 1 & 2).

### 3. Generate Categorized Priority Queue
Classify the parsed items into three priority levels:
- **🔴 CRITICAL PRIORITY**: Structural changes, methodology flaws, metric corrections, or anything affecting the core validity of the research (e.g., changes to Chapter 3).
- **🟡 MEDIUM PRIORITY**: Literature review additions, background narrative adjustments, or theoretical explanations (e.g., Chapter 1 & 2 narrative).
- **🟢 LOW PRIORITY**: Formatting, typos, citations formatting, or minor visual diagram tweaks.

### 4. Propose Action Plan
Output an interactive plan using markdown. For each priority item, provide:
- The exact files that need to be modified.
- The proposed strategy/change.
- An offer to execute the fix automatically.

**Important Rule**: ALWAYS ask for the user's confirmation before executing any code changes or writing new drafts. Do not execute the entire plan at once; ask "Which item should we tackle first?"
