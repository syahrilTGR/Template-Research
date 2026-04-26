---
description: Jalankan ekstraksi PDF massal menggunakan V2.5 Smart Extractor (Parallel) dan lakukan sinkronisasi identitas file (Dual-Mirror).
---

1. **Jalankan Ekstraksi**: 
   Jalankan perintah berikut di terminal:
   `python scripts/v2_smart_extractor.py all`

2. **Monitoring**: 
   Tunggu hingga muncul pesan `[SUCCESS] V2.5 Optimization complete.` di terminal.

3. **Fase Audit Agen (OTOMATIS)**:
   - Agen **wajib membaca** isi file `.md` hasil ekstraksi di `supportFiles/extracted_pdfs/`.
   - Agen mengidentifikasi metadata asli (Penulis, Tahun, Judul) dari isi konten.
   - Agen menyusun tabel proposal rename untuk disesuaikan dengan standar akademik.

4. **Eksekusi Dual-Mirror Renaming**:
   - Setelah persetujuan user, Agen melakukan **rename ganda**:
     - **PDF Asli**: `references/Lama.pdf` -> `references/[Nomor]_[Penulis]_[Tahun]_[Judul].pdf`
     - **File Markdown**: `supportFiles/extracted_pdfs/Lama.md` -> `supportFiles/extracted_pdfs/[Nomor]_[Penulis]_[Tahun]_[Judul].md`
   - Ini menjamin nama file PDF dan MD selalu **identik** (Zero Divergence).

5. **Final Respon**: 
   Laporkan ringkasan file yang berhasil di-extract dan di-rename.
