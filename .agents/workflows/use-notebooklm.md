---
description: Panduan kolaborasi hibrida antara Antigravity (lokal) dan NotebookLM (cloud) untuk pencarian literatur tahap lanjut (Deep Research).
---

# 🤖 Hybrid Workflow: Antigravity x NotebookLM

Workflow ini digunakan untuk memperluas pencarian literatur menggunakan fitur **Deep Research** dari Google NotebookLM, lalu mentransfer hasilnya kembali ke repositori lokal.

### 🛠️ Langkah-Langkah (AI to User)

1. **[AI ACTION] Analisis Kebutuhan**: Asisten (Antigravity) akan memeriksa `handoff.md` dan struktur repositori untuk mendeteksi gap riset. Asisten kemudian merumuskan **Prompt Deep Research** yang sangat spesifik (berisi keywords, metode target, dan variabel) untuk Anda copy-paste.
2. **[USER ACTION] Menjalankan Deep Research**: Anda membuka situs NotebookLM, lalu mem-paste prompt dari asisten ke dalam fitur Deep Research.
3. **[USER ACTION] Ekspor & Download (Krusial!)**:
   - Simpan hasil pencarian tersebut ke dalam Notebook Anda di NotebookLM.
   - Buka bagian **"Sources"** di NotebookLM, lalu **Download file PDF referensinya** ke komputer lokal Anda.
   - **Copy teks Sintesis/Rangkuman** berformat markdown yang dihasilkan oleh chat NotebookLM.
4. **[USER ACTION] Import Lokal ke Workspace Ini**:
   - Pindahkan file PDF yang sudah didownload ke dalam folder `references/` di repositori ini.
   - Buat file `.md` baru di folder `intelligence/catatan_notebooklm/` dan tempelkan (paste) teks sintesis dari NotebookLM ke sana.
5. **[AI ACTION] Eksekusi & Integrasi**: Anda cukup memberi tahu asisten: *"Saya sudah memasukkan bahan dari NotebookLM."* Asisten akan otomatis melahap catatan tersebut, mengekstrak metrik dari PDF baru (`/extract-metrics`), dan merajut pengetahuan baru tersebut ke dalam `handoff.md` dan Wiki.
