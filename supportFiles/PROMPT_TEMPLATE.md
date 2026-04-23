# 📋 Prompt Templates & Cheat Sheet

Gunakan templat di bawah ini untuk berinteraksi dengan asisten AI secara efisien. Anda bisa menyalin kalimat di bawah ini atau merujuk pada tabel perintah cepat di bagian akhir.

---

## 1. Bootstrapping & Persiapan
- **Audit Awal:** `"Halo, saya ingin mulai menggunakan Universal Research Template. Tolong lakukan audit wajib terhadap file gemini.md dan ACTION_PLAN.md saya sebelum kita mulai bekerja."`
- **Injeksi Gaya Bahasa:** `"Pelajari draf lama saya di folder example agar kamu bisa meniru gaya penulisan akademik yang ada."`
- **Ekstraksi Literatur:** `"Tolong ekstrak semua PDF di folder references dan masukkan ke daftar referensi valid di ANTI_HALLUCINATION.md. Setelah itu, tolong ganti nama (rename) semua file tersebut menjadi format PENULIS_TAHUN_JUDUL.pdf agar rapi."`

## 2. Research & Drafting
- **Tulis Subbab:** `"/write-subsection Bab 1 bagian Latar Belakang berdasarkan paper [Author_Year] yang sudah kita ekstrak."`
- **Analisis Mendalam:** `"/extract-metrics untuk membandingkan metode dari paper-paper yang ada di folder references."`
- **Sintesis Konsep:** `"Tolong bantu ringkas temuan utama dari paper [Author_Year] dan hubungkan dengan metodologi penelitian saya."`
- **Deep Research:** `"Saya ingin melakukan riset mendalam soal topik X. Tolong gunakan /use-notebooklm untuk buatkan prompt-nya."`

## 3. Sinkronisasi & Penanganan Word
- **Tarik dari Word:** `"Saya baru saja melakukan update di file Word OneDrive saya, tolong sinkronkan draf tersebut kembali ke Markdown (Handoff)."`
- **Audit Kualitas:** `"Audit tulisan saya di handoff menggunakan prose_auditor apakah sudah sesuai standar akademik?"`
- **Update Progres:** `"/update-handoff. Rangkum progres kita hari ini dan catat apa saja yang perlu kita kerjakan besok."`

---

## 🚀 Command Cheat Sheet (Tabel Referensi Cepat)

| Jenis Tugas | Perintah / Prompt | Deskripsi |
|---|---|---|
| **Onboarding** | *Audit infrastruktur* | Memeriksa apakah `gemini.md` dan `ACTION_PLAN.md` sudah siap. |
| **Riset** | `/extract-metrics` | Mengekstrak metrik dari PDF di folder `references/` ke Wiki. |
| **Drafting** | `/write-subsection` | Menulis draf bab dengan format akademik formal. |
| **Deep Research**| `/use-notebooklm` | Kolaborasi dengan NotebookLM untuk mencari gap literatur & import PDF. |
| **Quality Audit** | `python scripts/prose_auditor.py` | Mengecek karakter "robot" AI (em-dash) dan keabsahan sitasi. |
| **Syncing** | `powershell scripts/sync_word.ps1` | Menarik draf terbaru dari Word OneDrive ke Markdown. |
| **Cleanup** | `.\scripts\clean_repo.ps1` | Membersihkan repositori untuk memulai proyek baru. |

---

> [!TIP]
> **Selalu periksa [00_metadata.md](file:///f:/ML_Project/Template/supportFiles/handoff/00_metadata.md)** dalam setiap awal sesi baru agar AI mengingat draf terakhir dan arah penelitian Anda.
