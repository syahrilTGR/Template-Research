# DOCX Synchronization Tool Guide

Panduan ini mendokumentasikan alur kerja otomatis untuk menyinkronkan konten dari **Thesis Handoff (Markdown)** ke dalam **Proposal Skripsi (DOCX)** menggunakan skrip penyuntikan XML khusus.

---

## 🚀 Cara Menjalankan Sinkronisasi

### 1. Persiapan Environment
Selalu jalankan perintah di bawah dalam virtual environment (`thesis_venv`):
```powershell
# Aktivasi environment (jika belum - lokasi default setup_env.ps1)
$HOME\thesis_venv\Scripts\Activate.ps1
```

### 2. Unpack Dokumen (Wajib jika ada perubahan struktur Docx)
Jika file Word asli kamu berubah (tambah gambar/header baru), bongkar dulu file tersebut:
```powershell
python .agents/skills/docx/scripts/office/unpack.py "example\my_proposals\[Your_Thesis_Document].docx" example\my_proposals\unpacked_docx
```

### 3. Jalankan Injection Script
Gunakan skrip ini untuk memasukkan isi dari file Markdown di folder `handoff/` ke dalam folder XML Word.

**Mode Interaktif (Pilih Bab -> Pilih Subbab):**
```powershell
python scripts/inject_docx_xml.py
```

**Mode Cepat (Inject Bab tertentu, misal Bab 03, Semua Subbab):**
```powershell
python scripts/inject_docx_xml.py 03 all
```

**Mode Selektif (Inject Bab 03, Subbab 1 dan 3 saja):**
```powershell
python scripts/inject_docx_xml.py 03 1,3
```

### 4. Re-pack Menjadi DOCX
Setelah XML disuntik, bungkus kembali menjadi file Word baru. **Pastikan file `.docx` sedang tidak dibuka di Word!**
```powershell
python .agents/skills/docx/scripts/office/pack.py example/my_proposals/unpacked_docx/ example/my_proposals/[Your_Thesis_Document]_SYNCED.docx --validate false --original "example/my_proposals/[Your_Thesis_Document].docx"
```

---

## 📊 Memahami Laporan Injeksi
Skrip akan menampilkan tabel setelah selesai:
- **Found & Injected**: Header ditemukan di Word dan konten berhasil diperbarui.
- **SKIPPED**: Kamu tidak memilih subbab tersebut.
- **FAILED**: Judul di Markdown tidak cocok dengan Judul (Heading) di file Word. Pastikan teks di `## Judul` Markdown sama persis dengan yang ada di Word.

## 🛠️ Tips Post-Sync di Microsoft Word
Setelah membuka `[Your_Thesis_Document]_SYNCED.docx`:
1. **Konversi Tabel**: Blok teks tabel (dengan pemisah `|`), pilih menu `Insert > Table > Convert Text to Table`.
2. **Formula LaTeX**: Formula akan muncul sebagai `$$ ... $$`. Kamu bisa membiarkannya atau memasukkannya ke dalam boks Equation Word.
