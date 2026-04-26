---
description: Run this workflow if the user uploads a new journal paper and wants to know its accuracy/metrics. Mengekstrak metode utama dan metrik hasil dari paper jurnal ke dalam bentuk tabel komparasi.
---

1. **Jalankan Ekstraksi**: Jalankan workflow `/smart-extract` terlebih dahulu untuk mensinkronkan hasil ekstraksi terbaru ke dalam format Markdown.
2. **Identifikasi Sumber**: Buka file `.md` hasil ekstraksi di folder `supportFiles/extracted_pdfs/`.
3. **MANDATORY (Source of Truth)**: Untuk angka, metrik, atau tabel hasil eksperimen, **WAJIB** merujuk pada sub-bagian `## 📊 DATA APPENDIX` di bagian akhir file Markdown tersebut. Jangan melakukan halusinasi angka dari paragraf narasi jika ada tabel yang tersedia.
4. **Analisis Konten**: Baca bagian **Abstract**, **Methodology**, dan **Results** untuk mengekstrak:
   - Penulis & Tahun
   - Topik/Tujuan Penelitian
   - Metode/Arsitektur Utama (misalnya: YOLOv8, ResNet50)
   - Dataset yang Digunakan
   - Metrik Kinerja (Akurasi, F1, BWT, dll.)
5. **Obsidian Vault Maintenance**:
   - Simpan ringkasan detail ke `intelligence/ringkasan_paper/[FILE_NAME].md`.
   - Update `intelligence/ringkasan_paper/_INDEX_PAPER.md` dengan link baru.
   - Masukkan ringkasan ke dalam draf di `supportFiles/handoff/09_bibliography.md` atau lokasi relevan lainnya.
6. **Verifikasi**: Jika suatu metrik tidak ditemukan di tabel, tulis "N/A".
