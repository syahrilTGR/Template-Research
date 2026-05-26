# Paths are dynamically loaded from supportFiles/word_sync_config.json to prevent them from being lost during updates.
$CONFIG_FILE = "supportFiles/word_sync_config.json"

# Create a default configuration file if it doesn't exist
if (-not (Test-Path $CONFIG_FILE)) {
    $defaultConfig = @{
        sourcePath = "[PASTE_YOUR_ONEDRIVE_DOCX_PATH_HERE]"
        destPath   = "[PASTE_YOUR_LOCAL_FOLDER_HERE]\Thesis.docx"
        txtPath    = "[PASTE_YOUR_LOCAL_FOLDER_HERE]\Thesis.md"
    }
    $defaultConfig | ConvertTo-Json | Out-File -FilePath $CONFIG_FILE -Encoding utf8
    Write-Host "⚙️ Inisialisasi: Berkas konfigurasi baru telah dibuat di $CONFIG_FILE" -ForegroundColor Cyan
    Write-Host "-> Silakan isi path OneDrive dan folder lokal Anda di berkas tersebut sebelum menjalankan sinkronisasi!" -ForegroundColor Yellow
    return
}

# Load the configuration
$config = Get-Content $CONFIG_FILE | ConvertFrom-Json
$sourcePath = $config.sourcePath
$destPath   = $config.destPath
$txtPath    = $config.txtPath

# Check for placeholders in all three config values
$hasPlaceholder = ($sourcePath -like "*PASTE_*") -or ($destPath -like "*PASTE_*") -or ($txtPath -like "*PASTE_*")
if ($hasPlaceholder) {
    Write-Host "⛔ ERROR: Konfigurasi belum lengkap di berkas $CONFIG_FILE" -ForegroundColor Red
    Write-Host "   -> sourcePath : $sourcePath" -ForegroundColor Yellow
    Write-Host "   -> destPath   : $destPath" -ForegroundColor Yellow
    Write-Host "   -> txtPath    : $txtPath" -ForegroundColor Yellow
    Write-Host "   Silakan isi semua path yang masih mengandung placeholder [PASTE_...] sebelum menjalankan sinkronisasi." -ForegroundColor Yellow
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
    $pythonExe = "python"
    $configPath = "supportFiles/.venv_config.txt"
    if (Test-Path $configPath) {
        $pythonExe = Get-Content $configPath -Raw
        $pythonExe = $pythonExe.Trim()
    }
    & $pythonExe scripts/extract_docx.py "$destPath" "$txtPath"
    Write-Host "Sync Complete!"
} else {
    Write-Error "Source file not found: $sourcePath"
}
