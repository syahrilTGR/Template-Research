# WARNING: UPDATE THESE PATHS BEFORE RUNNING
$sourcePath = '[PASTE_YOUR_ONEDRIVE_DOCX_PATH_HERE]'        # e.g., C:\Users\Name\OneDrive\Thesis.docx
$destPath   = '[PASTE_YOUR_LOCAL_FOLDER_HERE]\Thesis.docx' # e.g., f:\Project\example\Thesis.docx
$txtPath    = '[PASTE_YOUR_LOCAL_FOLDER_HERE]\Thesis.md'   # e.g., f:\Project\example\Thesis.md

# Check if source exists
if (Test-Path -Path $sourcePath) {
    Write-Host "Syncing from OneDrive: $sourcePath"
    
    # Ensure destination directory exists
    $destDir = Split-Path $destPath
    if (!(Test-Path $destDir)) {
        New-Item -ItemType Directory -Force -Path $destDir
    }

    Copy-Item -Path $sourcePath -Destination $destPath -Force
    Write-Host "Copy successful."
    
    # Run Python extraction script
    Write-Host "Extracting Word document to Markdown..."
    python scripts/extract_docx.py "$destPath" "$txtPath"
    Write-Host "Sync Complete!"
} else {
    Write-Error "Source file not found: $sourcePath"
}
