# WARNING: UPDATE THESE PATHS BEFORE RUNNING
$sourcePath = '[PASTE_YOUR_ONEDRIVE_DOCX_PATH_HERE]'        # e.g., C:\Users\Name\OneDrive\Thesis.docx
$destPath   = '[PASTE_YOUR_LOCAL_FOLDER_HERE]\Thesis.docx' # e.g., f:\Project\example\Thesis.docx
$txtPath    = '[PASTE_YOUR_LOCAL_FOLDER_HERE]\Thesis.md'   # e.g., f:\Project\example\Thesis.md

# Check for placeholders
if ($sourcePath -like "*[PASTE_*") {
    Write-Host "⛔ ERROR: Silakan atur path OneDrive Anda di file ini terlebih dahulu!" -ForegroundColor Red
    return
}

# 1. Sync Word Document
if (Test-Path -Path $sourcePath) {
    Write-Host "Syncing from OneDrive: $sourcePath"
    
    $destDir = Split-Path $destPath
    if (!(Test-Path $destDir)) {
        New-Item -ItemType Directory -Force -Path $destDir
    }

    Copy-Item -Path $sourcePath -Destination $destPath -Force
    Write-Host "Copy successful."
    
    # 2. Extraction
    Write-Host "Extracting Word document to Markdown..."
    python scripts/extract_docx.py "$destPath" "$txtPath"
    Write-Host "Sync Complete!"
} else {
    Write-Error "Source file not found: $sourcePath"
}
