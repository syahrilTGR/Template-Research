# 🧼 CLEAN REPOSITORY SCRIPT
# This script resets the template to a blank state for a new project.
# IT DELETES ALL REFERENCES, EXAMPLES, AND DRAFTS!

$Confirmation = Read-Host "⚠️ WARNING: This will delete ALL references, example drafts, and reset your modular handoff. Are you sure? (y/n)"
if ($Confirmation -ne 'y') {
    Write-Host "Reset cancelled."
    exit
}

Write-Host "Cleaning repository..." -ForegroundColor Yellow

# 1. Clear References
$refsPath = "references/*.pdf", "references/*.bib"
Remove-Item -Path $refsPath -Force -ErrorAction SilentlyContinue
Write-Host "- References cleared."

# 2. Clear Examples
$examplePath = "example/*.docx", "example/*.md"
Remove-Item -Path $examplePath -Force -ErrorAction SilentlyContinue
Write-Host "- Examples cleared."

# 3. Reset Modular Handoff
$handoffDir = "supportFiles/handoff"
if (Test-Path $handoffDir) {
    # Keep metadata template but reset others
    Remove-Item -Path "$handoffDir/01_introduction.md", "$handoffDir/02_literature_review.md", "$handoffDir/03_methodology.md", "$handoffDir/09_bibliography.md" -Force -ErrorAction SilentlyContinue
    
    # Re-create empty prose files
    "# CHAPTER I INTRODUCTION" | Set-Content -Path "$handoffDir/01_introduction.md"
    "# CHAPTER II LITERATURE REVIEW" | Set-Content -Path "$handoffDir/02_literature_review.md"
    "# CHAPTER III METHODOLOGY" | Set-Content -Path "$handoffDir/03_methodology.md"
    "# REFERENCE" | Set-Content -Path "$handoffDir/09_bibliography.md"
    
    Write-Host "- Modular Handoff reset to blank chapters."
}

# 4. Clear Extracted Files
$extractedPath = "supportFiles/extracted_pdfs/*", "supportFiles/extracted_tables/*"
Remove-Item -Path $extractedPath -Recurse -Force -ErrorAction SilentlyContinue
Write-Host "- Extracted PDF assets cleared."

# 5. Clear Intelligence
$intelPath = "intelligence/ringkasan_paper/*.md", "intelligence/catat_notebooklm/*.md"
Remove-Item -Path $intelPath -Force -ErrorAction SilentlyContinue
Write-Host "- Intelligence summaries cleared."

Write-Host "✨ Repository is now CLEAN and ready for a new project!" -ForegroundColor Green
