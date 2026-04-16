# 📖 Panduan Penggunaan AI Antigravity

Proyek ini terintegrasi dengan **Antigravity**, asisten AI yang dirancang untuk membantu pengerjaan riset dan koding secara profesional.

---

## 🚀 Perintah Cepat (Workflows)

Ketik perintah berikut di chat untuk memicu asisten melakukan tugas spesifik:

| Perintah | Deskripsi |
|---|---|
| `/context-summary` | AI akan meringkas progres terakhir dan memberikan laporan status saat ini. |
| `/write-subsection` | Meminta AI menulis draf subbab laporan/jurnal dengan gaya bahasa akademik formal. |
| `/check-references` | Mengecek kualitas paper yang baru di-upload (tahun terbit, relevansi, dll). |
| `/update-handoff` | Digunakan di akhir sesi kerja untuk menyimpan "ingatan" AI agar sesi berikutnya bisa nyambung. |
| `/extract-metrics` | Mengekstrak metode utama dan metrik hasil dari paper jurnal ke dalam bentuk tabel komparasi. |

---

## 🛠️ Cara Kerja

1.  **Konteks Global**: AI membaca aturan inti kamu (identitas, aturan optimasi) dari `gemini.md`.
2.  **Konteks Lokal**: AI membaca file di folder `.agents/` untuk memahami keahlian tambahan yang harus ia gunakan (Skills dan Workflows).
3.  **Handoff**: AI menyimpan progres kerja dan seluruh draf tulisan dalam `supportFiles/handoff.md`. Pastikan file ini diperbarui setiap akhir sesi dengan `/update-handoff`.
4.  **Riset**: AI bisa membaca file-file di folder `papers/` untuk membantu Anda membuat tinjauan pustaka.

---

## ✨ Kemampuan Canggih (Power User)

Selain menulis teks, Anda bisa meminta asisten melakukan hal-hal kompleks berikut:

- **Professional Word Formatting**: Meminta AI membuat dokumen Word `.docx` profesional (dengan TOC, gaya Heading, dll) secara mandiri. Ini menggunakan pustaka Python, **bukan** butuh Microsoft Word terinstal.
- **Track Changes Audit**: Meminta AI menganalisis perubahan (tracked changes) dalam dokumen Word dengan membongkar struktur XML internalnya secara langsung.
- **Image Extraction**: Mengekstrak gambar dari dokumen Word secara otomatis ke folder `media/` tanpa butuh aplikasi visual.

---

## 🛠️ Bedah DOCX Mandiri (Docx Surgery)

Jika Anda atau teman Anda mengalami masalah format Word yang "aneh" (misal: penomoran tidak mau urut, spasi bandel), Anda bisa menggunakan alat bedah internal kami:

1.  **Membongkar (Unpack)**: Mengubah `.docx` menjadi folder berisi file XML yang rapi.
    ```bash
    python scripts/docx_surgery.py unpack draf.docx folder_bedah/
    ```
2.  **Operasi XML**: Buka file XML di dalam `folder_bedah/word/` dengan teks editor (VS Code) untuk memperbaiki isi secara manual.
3.  **Membungkus (Pack)**: Mengembalikan folder menjadi file `.docx` yang valid.
    ```bash
    python scripts/docx_surgery.py pack folder_bedah/ draf_fixed.docx --original draf.docx
    ```

---

## 💡 Tips Berkolaborasi

- **Keep it Focused**: Berikan satu instruksi spesifik per pesan (misal: "Tulis subbab Metodologi bagian pengumpulan data").
- **Gunakan File .md**: AI paling lancar membaca dan mengedit file markdown. Ubah file PDF riset menjadi teks/markdown jika ingin AI menganalisisnya secara mendalam.

---
*Siap untuk "gas" skripsimu? Selamat berkarya!*
