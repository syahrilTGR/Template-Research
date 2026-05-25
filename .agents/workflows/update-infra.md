---
description: Sinkronisasi otomatis infrastruktur repo dari Template-Research pusat
---

# Workflow: Update Infrastructure (Self-Healing & Auto-Config)

Workflow ini akan menarik update terbaru dari repository pusat tanpa merusak draf tulisan atau identitas riset Anda.

---

## Step 1: Clone Independent (Temp)

Asisten wajib menarik pembaruan infrastruktur langsung dari repositori pusat template.

// turbo
```powershell
$repoUrl = "https://github.com/syahrilTGR/Template-Research"
rtk git clone $repoUrl .agents/_bridge_update_
```

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
rtk powershell -c "Remove-Item -Path '.agents/_bridge_update_' -Recurse -Force ; scripts/setup_env.ps1 ; scripts/setup_docx_infra.ps1"
```

**MANDATORY POST-UPDATE HANDSHAKE:**
Setelah update selesai, asisten **WAJIB** memindai file `SKILL.md` (docx). Jika ditemukan placeholder `[PYTHON_PATH_PLACEHOLDER]`, asisten **HARUS SEGERA** menjalankan **Dynamic Setup Protocol** (Scan venv -> Ask User -> Update Path) tanpa menunggu perintah tambahan dari user.

---

## Step 4: Post-Update Integrity Audit

Asisten WAJIB melakukan audit ulang secara mandiri untuk memastikan fitur baru aktif.

// turbo
```powershell
# Pemicu Audit (Lihat aturan di gemini.md)
rtk powershell -c "echo 'Update Complete. Starting Re-Audit...'"
```
*(Asisten akan otomatis membaca gemini.md kembali dan melakukan verifikasi total).*

> [!IMPORTANT]
> **Rekomendasi Rilis Baru**: 
> Setelah pembaruan selesai, asisten **WAJIB** menyarankan pengguna untuk membaca dokumen pengumuman rilis resmi yang terletak di [supportFiles/announcement_v1.0.7.pdf](file:///g:/Project/Template/supportFiles/announcement_v1.0.7.pdf) (atau berkas PDF pengumuman rilis terbaru yang tersedia) guna memahami seluruh daftar penambahan *skills*, panduan penulisan bebas AI, dan cara penggunaan fitur-fitur baru.

## ⚠️ Perhatian
Jika Anda memiliki modifikasi kustom pada file sistem, buat backup terlebih dahulu atau commit perubahan Anda sebelum menjalankan workflow ini.
