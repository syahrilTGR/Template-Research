---
description: Sinkronisasi otomatis infrastruktur repo dari Template-Research pusat
---

# Workflow: Update Infrastructure (Self-Healing)

Workflow ini akan menarik update terbaru dari repository pusat tanpa merusak draf tulisan atau identitas riset Anda.

---

## Step 1: Clone Independent (Temp)

Kita akan melakukan clone dari repository pusat ke folder sementara, bahkan jika proyek Anda bukan folder Git.

// turbo
```powershell
rtk git clone https://github.com/syahrilTGR/Template-Research .agents/_bridge_update_
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

**2. Smart Audit (Instruksi untuk Agent):**
Agen wajib melakukan perbandingan antara folder lokal dan `.agents/_bridge_update_`.
> *"Bandingkan file-file di folder `.agents/` dan `scripts/`. Tampilkan daftar file yang memiliki perbedaan konten (DIFF) kepada user. Tanyakan persetujuan user sebelum menimpa file, terutama untuk file Workflow (.md) yang mungkin sudah dimodifikasi kustom oleh user."*

**3. Selective Grafting:**
- File **Sistem/Script** (`.py`, `.ps1`) yang bersifat *engine* disarankan untuk diperbarui.
- File **Workflow** (`.md`) disarankan untuk ditinjau ulang agar modifikasi kustom user tidak hilang.

---

## Step 3: Cleanup & Setup

Setelah file diperbarui, asisten wajib menghapus folder temporary dan menjalankan setup ulang environment.

// turbo
```powershell
rtk powershell -c "Remove-Item -Path '.agents/_bridge_update_' -Recurse -Force ; scripts/setup_env.ps1 ; scripts/setup_docx_infra.ps1"
```

---

## Step 4: Post-Update Integrity Audit

Asisten WAJIB melakukan audit ulang secara mandiri untuk memastikan fitur baru aktif.

// turbo
```powershell
# Pemicu Audit (Lihat aturan di gemini.md)
rtk powershell -c "echo 'Update Complete. Starting Re-Audit...'"
```
*(Asisten akan otomatis membaca gemini.md kembali dan melakukan verifikasi total).*

## ⚠️ Perhatian
Jika Anda memiliki modifikasi kustom pada file sistem, buat backup terlebih dahulu atau commit perubahan Anda sebelum menjalankan workflow ini.
