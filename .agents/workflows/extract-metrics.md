---
description: Mengekstrak metode utama dan metrik hasil dari paper jurnal ke dalam bentuk tabel komparasi
---

1. Identifikasi file paper (PDF/TXT) yang disebutkan oleh pengguna (biasanya di folder `papers/`).
2. Baca dan analisis bagian **Abstract**, **Methodology**, dan **Results/Conclusion** pada paper tersebut.
3. Ekstrak informasi berikut untuk setiap paper:
   - Penulis & Tahun
   - Topik/Tujuan Penelitian
   - Metode/Arsitektur Utama (misalnya: ResNet50, YOLOv8)
   - Dataset yang Digunakan (jika disebutkan)
   - Metrik Kinerja/Hasil Eksperimen (Akurasi, F1-Score, BWT, dll.)
4. Susun hasil ekstraksi ke dalam bentuk **Tabel Markdown** yang rapi.
5. Jika pengguna meminta untuk memasukkannya ke file tertentu (misalnya `supportFiles/previous_research_table.md` atau `bab2_previous_research_table.md`), perbarui file tersebut dengan menambahkan baris baru ke tabel yang sudah ada.
6. Pastikan tidak ada data yang difabrikasi; jika suatu metrik tidak disebutkan di paper, tulis "N/A" atau "Tidak Disebutkan".
