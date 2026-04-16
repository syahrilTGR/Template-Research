# 🧼 CLEAN REPOSITORY SCRIPT
# This script resets the template to a blank state for a new project.
# IT DELETES ALL PAPERS, EXAMPLES, AND DRAFTS!

$Confirmation = Read-Host "⚠️ WARNING: This will delete ALL papers, example drafts, and reset your handoff. Are you sure? (y/n)"
if ($Confirmation -ne 'y') {
    Write-Host "Reset cancelled."
    exit
}

Write-Host "Cleaning repository..." -ForegroundColor Yellow

# 1. Clear Papers
$papersPath = "papers/*.pdf"
if (Test-Path $papersPath) {
    Remove-Item -Path $papersPath -Force
    Write-Host "- Papers cleared."
}

# 2. Clear Examples
$examplePath = "example/*.docx", "example/*.md"
if (Test-Path $examplePath) {
    Remove-Item -Path $examplePath -Force
    Write-Host "- Examples cleared."
}

# 3. Reset Handoff.md
$handoffPath = "supportFiles/handoff.md"
if (Test-Path $handoffPath) {
    $blankHandoff = @"
# Global Handoff & Project State

## Status Overview
| Stage | Status | Progress |
|---|---|---|
| Phase 0: Infrastructure | [x] | 100% |
| Chapter 1: Intro | [ ] | 0% |

## Current Text Drafts
*(Drafts will appear here)*

---
## Last Session Summary
(Session has not started)
"@
    Set-Content -Path $handoffPath -Value $blankHandoff -Force
    Write-Host "- Handoff reset to blank."
}

# 4. Clear Extracted Files
$extractedPath = "supportFiles/extracted_pdfs/*"
if (Test-Path $extractedPath) {
    Remove-Item -Path $extractedPath -Force
    Write-Host "- Extracted PDFs cleared."
}

# 5. Reset Action Plan (Phase 0 stays checked)
# (Optional: User can do this manually)

Write-Host "✨ Repository is now CLEAN and ready for a new project!" -ForegroundColor Green
