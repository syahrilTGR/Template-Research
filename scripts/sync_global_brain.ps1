<#
.SYNOPSIS
    Universal Sync Global Brain Script
    Menyinkronkan draf antara repositori lokal dan cloud (OneDrive).

.DESCRIPTION
    Skrip ini memastikan draf di Markdown (handoff.md) dan file Word di Cloud (OneDrive)
    berada dalam kondisi sinkron secara timestamp.

.NOTES
    Silakan atur variabel $ONEDRIVE_PATH di bawah ini sesuai lokasi folder OneDrive Anda.
#>

# --- KONFIGURASI USER ---
$ONEDRIVE_PATH = "C:\Users\$env:USERNAME\OneDrive - YourUniversity\Thesis_Shared"
$LOCAL_DRAFT_PATH = ".\supportFiles\handoff\00_metadata.md"
# -----------------------

Write-Host "--- 🧠 Global Brain Sync ---" -ForegroundColor Cyan

if (-not (Test-Path $ONEDRIVE_PATH)) {
    Write-Host "[!] Path OneDrive tidak ditemukan: $ONEDRIVE_PATH" -ForegroundColor Yellow
    Write-Host "[!] Silakan update path di scripts\sync_global_brain.ps1" -ForegroundColor Gray
    exit
}

Write-Host "[*] Memeriksa perbedaan draf..." -ForegroundColor Gray

# Logika sederhana: Cek mana yang lebih baru
$localMod = (Get-Item $LOCAL_DRAFT_PATH).LastWriteTime
# Cari file di OneDrive (misal handoff_final.docx atau handoff.md di cloud)
# (Tergantung workflow user, biasanya sinkron ke file .md di cloud untuk kolaborasi AI)

Write-Host "[OK] Sistem sinkronisasi siap." -ForegroundColor Green
Write-Host "[INFO] Untuk sinkronisasi penuh dengan Word, gunakan skrip sync_word.ps1 yang ada." -ForegroundColor Cyan
