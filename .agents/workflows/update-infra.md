---
description: Sinkronisasi otomatis infrastruktur repo dari Template-Research pusat
---

# Workflow: Update Infrastructure (Self-Healing & Auto-Config)

Workflow ini akan menarik update terbaru dari repository pusat tanpa merusak draf tulisan atau identitas riset Anda.

---

## Step 1: Eksekusi Update Engine (Python-Native)

Asisten wajib menjalankan skrip pembaruan infrastruktur berbasis Python. Skrip ini secara otomatis memverifikasi versi online, membuat cadangan pengaman (*safety backup*), melakukan penggabungan cerdas (*smart grafting*), menyelaraskan konfigurasi environment, dan menjalankan rangkaian Smoke Test kelayakan.

// turbo
```powershell
[PYTHON_PATH_PLACEHOLDER] scripts/update_infra.py
```

---

## Step 2: Post-Update Handshake

Setelah pembaruan selesai, asisten **WAJIB**:
1. Memindai file `SKILL.md` (docx). Jika ditemukan placeholder `[PYTHON_PATH_PLACEHOLDER]`, asisten **HARUS SEGERA** menjalankan **Dynamic Setup Protocol** (Scan venv -> Ask User -> Update Path) untuk menambal path interpreter Python lokal.
2. Membaca kembali berkas `gemini.md` untuk melakukan verifikasi total. Jika berkas `gemini.md` ter-reset menjadi template kosong, asisten **WAJIB** menawarkan untuk memicu **🚀 Onboarding Protocol** secara interaktif.
3. Menyarankan pengguna untuk membaca berkas [CHANGELOG.md](../../CHANGELOG.md) guna memahami daftar penambahan *skills*, perbaikan, dan cara penggunaan fitur-fitur baru.

## ⚠️ Perhatian
Jika Anda memiliki modifikasi kustom pada file sistem, buat backup terlebih dahulu atau commit perubahan Anda sebelum menjalankan workflow ini.
