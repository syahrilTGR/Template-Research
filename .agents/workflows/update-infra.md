---
description: Sinkronisasi otomatis infrastruktur repo dari Template-Research pusat
---

# Workflow: Update Infrastructure (Self-Healing & Auto-Config)

Workflow ini akan menarik update terbaru dari repository pusat tanpa merusak draf tulisan atau identitas riset Anda.

---

## Step 1: Clone Independent (Temp)

Asisten wajib menarik pembaruan infrastruktur langsung dari repositori pusat template.

> [!IMPORTANT]
> **Protokol Pemantauan Aktif (MANDATORI)**:
> Saat mengunduh via ZIP Fallback, proses ini memakan waktu (bergantung pada koneksi internet). Asisten **DILARANG** menghentikan pemantauan atau menyatakan pembaruan selesai secara prematur. Asisten **WAJIB** memantau progress secara aktif dengan membaca keluaran baris log (`Write-Host`) secara bertahap hingga seluruh proses pembersihan sampah selesai.

// turbo
```powershell
# Hapus sisa folder update lama jika ada untuk mencegah konflik klon
if (Test-Path ".agents/_bridge_update_") {
    Write-Host "[1/5] Membersihkan folder jembatan lama..." -ForegroundColor Cyan
    Remove-Item ".agents/_bridge_update_" -Recurse -Force
}

$repoUrl = "https://github.com/syahrilTGR/Template-Research"
if (Get-Command git -ErrorAction SilentlyContinue) {
    Write-Host "[2/5] Git terdeteksi. Memulai klon repositori..." -ForegroundColor Green
    git clone $repoUrl .agents/_bridge_update_
} else {
    Write-Host "[2/5] Git TIDAK ditemukan. Mengaktifkan Self-Healing Fallback..." -ForegroundColor Yellow
    Write-Host "-> Mengunduh arsip ZIP dari GitHub..." -ForegroundColor Yellow
    $zipUrl = "$repoUrl/archive/refs/heads/main.zip"
    $zipPath = Join-Path $HOME "template_update.zip"

    # Hapus sisa ekstraksi lama jika ada (mencegah Expand-Archive gagal)
    if (Test-Path ".agents/temp_update") {
        Write-Host "   [Cleanup] Membersihkan folder temp_update lama..." -ForegroundColor DarkYellow
        Remove-Item ".agents/temp_update" -Recurse -Force
    }

    Invoke-WebRequest -Uri $zipUrl -OutFile $zipPath
    
    Write-Host "[3/5] Mengekstrak paket ZIP pembaruan..." -ForegroundColor Yellow
    Expand-Archive -Path $zipPath -DestinationPath ".agents/temp_update" -Force
    
    Write-Host "[4/5] Memindahkan berkas ke folder jembatan..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path ".agents/_bridge_update_" -Force | Out-Null
    Copy-Item ".agents/temp_update/Template-Research-main/*" ".agents/_bridge_update_" -Recurse -Force
    
    Write-Host "[5/5] Membersihkan berkas arsip sementara..." -ForegroundColor Yellow
    Remove-Item ".agents/temp_update", $zipPath -Recurse -Force
    Write-Host "-> Persiapan berkas pembaruan selesai!" -ForegroundColor Green
}
```

---

## Step 1.5: Pivot to New Workflow (MANDATORI)

Untuk memastikan kelancaran pembaruan, asisten **WAJIB** beralih menggunakan alur kerja pembaruan infrastruktur yang baru saja diunduh di folder jembatan sementara:

> [!IMPORTANT]
> **Protokol Pivoting**:
> 1. Segera baca file `.agents/_bridge_update_/.agents/workflows/update-infra.md`.
> 2. JIKA file tersebut ada, **abaikan langkah-langkah berikutnya di dokumen lokal ini** dan segera beralih mengikuti instruksi terbaru mulai dari **Step 2** di berkas baru tersebut.
> 3. JIKA file tidak ada (fallback), lanjutkan menggunakan instruksi di dokumen lokal ini.

---

## Step 2: Eksekusi Update (Safe Smart-Audit)

Asisten WAJIB melakukan backup infrastruktur saat ini dan melakukan audit manual sebelum melakukan pembaruan.

**1. Create Safety Backup:**
// turbo
```powershell
# Backup folder .agents dan scripts ke folder timestamp
$timestamp = Get-Date -Format "yyyyMMdd_HHmm"
$backupDir = ".agents/backups/infra_pre_update_$timestamp"
New-Item -ItemType Directory -Path $backupDir -Force
robocopy ".agents" "$backupDir/.agents" /E /XD "backups" "_bridge_update_" /TBD /NP
robocopy "scripts" "$backupDir/scripts" /E /TBD /NP
# Robocopy mengembalikan exit code 1-7 untuk penyalinan sukses. Setel ulang ke 0 agar runner tidak menganggapnya error.
if ($LASTEXITCODE -le 7) { $global:LASTEXITCODE = 0 }
echo "Backup saved to $backupDir"
```

**2. Infra Audit Dashboard (MANDATORI):**
Agen wajib melakukan perbandingan antara folder lokal dan `.agents/_bridge_update_`.
> *"Gunakan tools pembanding untuk melihat perbedaan konten. **WAJIB** buat sebuah **Artifact: Infra Audit Dashboard** berisi tabel: | File | Status | Perubahan | Rekomendasi |. Status 'Modified' diberikan jika file lokal mengandung kustomisasi user (seperti identitas/prose) yang tidak ada di pusat. Jangan menimpa file tanpa persetujuan eksplisit user terhadap dashboard tersebut."*

**3. Selective Grafting & Conflict Handling:**
- **Engine Files** (`.py`, `.ps1`, `.js`): Overwrite langsung setelah backup.
- **Skill Files** (`SKILL.md`): Overwrite untuk mendapatkan protokol terbaru.
- **Identity Files** (`gemini.md`, `ACTION_PLAN.md`): **Dilarang Overwrite**. Lakukan *Smart Merge* (perbarui versi dan instruksi sistem, tapi tetap pertahankan [Project Identity] milik user).

---

## Step 3: Cleanup & Auto-Configuration

Setelah file diperbarui, asisten wajib menghapus folder temporary dan menjalankan rutinitas setup.

// turbo
```powershell
# Hapus folder jembatan sementara
Remove-Item -Path '.agents/_bridge_update_' -Recurse -Force
# Jalankan setup environment (Python + venv)
powershell -ExecutionPolicy Bypass -File scripts/setup_env.ps1
# Jalankan setup infrastruktur docx (Node.js)
powershell -ExecutionPolicy Bypass -File scripts/setup_docx_infra.ps1
```

**MANDATORY POST-UPDATE HANDSHAKE:**
Setelah update selesai, asisten **WAJIB** memindai file `SKILL.md` (docx). Jika ditemukan placeholder `[PYTHON_PATH_PLACEHOLDER]`, asisten **HARUS SEGERA** menjalankan **Dynamic Setup Protocol** (Scan venv -> Ask User -> Update Path) tanpa menunggu perintah tambahan dari user.

---

## Step 4: Post-Update Integrity Audit

Asisten WAJIB melakukan audit ulang secara mandiri untuk memastikan fitur baru aktif dan identitas riset Anda tetap aman.

// turbo
```powershell
# Pemicu Audit (Lihat aturan di gemini.md)
powershell -c "echo 'Update Complete. Starting Re-Audit...'"
```
*(Asisten akan otomatis membaca gemini.md kembali dan melakukan verifikasi total).*

> [!IMPORTANT]
> **Deteksi Ulang Identitas (Onboarding Guard)**:
> Jika berkas `gemini.md` Anda sempat ter-reset/tertimpa menjadi template kosong selama update, asisten **WAJIB** langsung menawarkan untuk memicu **🚀 Onboarding Protocol** secara interaktif untuk memulihkan identitas riset Anda dengan cepat.

> [!IMPORTANT]
> **Rekomendasi Rilis Baru**: 
> Setelah pembaruan selesai, asisten **WAJIB** menyarankan pengguna untuk membaca berkas [CHANGELOG.md](../../CHANGELOG.md) guna memahami seluruh daftar penambahan *skills*, perbaikan, dan cara penggunaan fitur-fitur baru.

## ⚠️ Perhatian
Jika Anda memiliki modifikasi kustom pada file sistem, buat backup terlebih dahulu atau commit perubahan Anda sebelum menjalankan workflow ini.
