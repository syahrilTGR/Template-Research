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

## Step 2: Eksekusi Update (Comprehensive System Audit)

Asisten WAJIB melakukan audit menyeluruh antara folder lokal dan folder `.agents/_bridge_update_`. 

**Aturan Grafting (Pencangkokan):**

1.  **Infrastructure Sync (OVERWRITE IF NEWER)**: 
    - Seluruh isi folder `.agents/` (Skills, Workflows, Plugins).
    - Seluruh isi folder `scripts/`.
    - Seluruh file utility di root (e.g., `*.ps1`, `*.py`, `.antigravityignore`).
2.  **Research Guard (DO NOT OVERWRITE)**:
    - `references/` (PDF Jurnal user).
    - `supportFiles/handoff/` (Draf tulisan user).
    - `intelligence/` (Catatan penelitian).
    - `example/` (Kecuali jika user meminta update template contoh).
3.  **Identity Preservation**: 
    - Pada `gemini.md`, hanya perbarui bagian **AI AUDITOR** (v1.0.x dll). 
    - **JANGAN** menyentuh bagian `## 🎯 Project Identity` dan `## 💻 Environment & Technical Context`. Itu adalah data pribadi user.

**Instruksi untuk Agent:**
> *"Lakukan audit perbandingan folder antara proyek ini dan `.agents/_bridge_update_`. Ganti/tambahkan file infrastruktur (Skills, Workflows, Scripts, Root Files) dengan versi terbaru. JANGAN hapus atau modifikasi folder draf/riset (handoff, references, intelligence). Laporkan ringkasan 'What's New' berdasarkan CHANGELOG.md terbaru."*

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
