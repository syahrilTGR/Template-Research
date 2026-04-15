# WARNING: UPDATE THESE PATHS BEFORE RUNNING
$sourcePath = 'C:\Users\YourName\OneDrive\Thesis_Draft.docx'
$destPath   = 'f:\YourProject\example\Thesis_Draft.docx'
$txtPath    = 'f:\YourProject\example\Thesis_Draft.md'

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
