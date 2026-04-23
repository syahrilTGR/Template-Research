---
description: Mengekstrak metode utama dan metrik hasil dari paper jurnal ke dalam bentuk tabel komparasi
---

1. Jalankan `python scripts/extract_pdfs.py` untuk mensinkronkan hasil ekstraksi terbaru dari folder `references/`.
2. Identifikasi file hasil ekstraksi di folder `supportFiles/extracted_pdfs/` (TEKS) dan `supportFiles/extracted_tables/` (TABEL/EXCEL).
3. Baca dan analisis bagian **Abstract**, **Methodology**, dan **Results/Conclusion** pada paper tersebut menggunakan file teks tersebut.
3. Ekstrak informasi berikut untuk setiap paper:
   - Penulis & Tahun
   - Topik/Tujuan Penelitian
   - Metode/Arsitektur Utama (misalnya: ResNet50, YOLOv8)
   - Dataset yang Digunakan (jika disebutkan)
   - Metrik Kinerja/Hasil Eksperimen (Akurasi, F1-Score, BWT, dll.)
4. Susun hasil ekstraksi ke dalam bentuk **Tabel Markdown** yang rapi.
5. Jalankan protokol **Obsidian Vault Maintenance**:
   - Simpan draf ringkasan detail ke file baru di `intelligence/ringkasan_paper/` dengan format penamaan `PENULIS_TAHUN_JUDUL.md`.
   - Tambahkan YAML Frontmatter di bagian awal file.
   - Perbarui `intelligence/ringkasan_paper/_INDEX_PAPER.md` dengan menambahkan link ke file baru tersebut menggunakan `[[Wikilinks]]`.
   - Masukkan baris ringkasan tersebut ke dalam tabel komparasi di `supportFiles/handoff/01_literature_review.md` jika diminta untuk keperluan draf Thesis.
6. Pastikan tidak ada data yang difabrikasi; jika suatu metrik tidak disebutkan di paper, tulis "N/A" atau "Tidak Disebutkan".
