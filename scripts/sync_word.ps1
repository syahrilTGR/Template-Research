# WARNING: UPDATE THESE PATHS BEFORE RUNNING
$sourcePath = '[PASTE_YOUR_ONEDRIVE_DOCX_PATH_HERE]'        # e.g., C:\Users\Name\OneDrive\Thesis.docx
$destPath   = '[PASTE_YOUR_LOCAL_FOLDER_HERE]\Thesis.docx' # e.g., f:\Project\example\Thesis.docx
$txtPath    = '[PASTE_YOUR_LOCAL_FOLDER_HERE]\Thesis.md'   # e.g., f:\Project\example\Thesis.md

# Diagram Sync Configuration
$sourceDiagramDir = '[PASTE_YOUR_ONEDRIVE_FOLDER_HERE]'     # e.g., C:\Users\Name\OneDrive\Diagrams
$destDiagramDir   = '[PASTE_YOUR_LOCAL_FOLDER_HERE]'        # e.g., f:\Project\example\

# Check for placeholders
if ($sourcePath -like "*[PASTE_*") {
    Write-Host "⛔ ERROR: Silakan atur path OneDrive Anda di file ini terlebih dahulu!" -ForegroundColor Red
    return
}

# 1. Sync Word Document
if (Test-Path -Path $sourcePath) {
    $lastSave = (Get-Item $sourcePath).LastWriteTime
    Write-Host "--- Syncing from OneDrive: $sourcePath ---"
    Write-Host "Last saved: $lastSave"
    
    $destDir = Split-Path $destPath
    if (!(Test-Path $destDir)) { New-Item -ItemType Directory -Force -Path $destDir }

    Copy-Item -Path $sourcePath -Destination $destPath -Force
    Write-Host "Docx Copy successful."
    
    # 2. Sync Draw.io Diagrams (Optional)
    if (Test-Path $sourceDiagramDir) {
        Write-Host "Syncing Draw.io diagrams..."
        Get-ChildItem -Path "$sourceDiagramDir\*.drawio" | Copy-Item -Destination $destDiagramDir -Force
        Write-Host "Diagram sync complete."
    }

    # 3. Extraction
    Write-Host "Extracting text to Markdown..."
    python scripts/extract_docx.py "$destPath" "$txtPath"
    Write-Host "Sync Complete: $txtPath"
} else {
    Write-Error "Source file not found: $sourcePath"
}
