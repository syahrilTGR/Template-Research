---
name: custom_project_skill
description: >
  Skill template untuk mendefinisikan arsitektur sistem, batasan logika, dan konteks paper untuk AI assistant di proyek baru.
  Gunakan file ini sebagai ruang untuk "mengajari" AI tentang proyek spesifik Anda.
---

# Custom Project Skill

## Deskripsi Proyek

Referensikan file `gemini.md` untuk identitas mahasiswa, judul skripsi, dan institusi.

---

Each time a new AI session begins, the MANDATORY first step is to follow the **Hybrid Context Protocol**:

1. Read **`supportFiles/PROMPT_TEMPLATE.md`** for the session start sequence.
2. Load **`supportFiles/handoff.md`** to understand the latest project state and prose drafts.
3. Cross-reference **`papers/index.md`** and **`supportFiles/ANTI_HALLUCINATION.md`** for valid technical citations.

Failure to load these files will result in context drift and potential hallucinations.

---

## ⚠️ Mandatory Integrity & Onboarding Check
**Setiap kali sesi dimulai, AI WAJIB melakukan pengecekan integritas berikut sebelum melakukan tugas teknis apa pun:**

1.  **Placeholder Check**: Periksa apakah `gemini.md` masih mengandung `[Nama Anda]`, atau `scripts/sync_word.ps1` masih mengandung `[PASTE_...]`.
2.  **Infrastructure Check**: Baca **`supportFiles/ACTION_PLAN.md`**. Periksa apakah semua item di **"Phase 0: Infrastructure"** (termasuk poin 0.5 dan 0.6) sudah terceklis `[x]`.
3.  **Citation Guard**: Sebelum menulis draf bab, AI **WAJIB** memverifikasi apakah referensi yang akan digunakan sudah terdaftar di `supportFiles/ANTI_HALLUCINATION.md`.

**Protokol Pemblokiran:**
- Jika poin 1 atau 2 belum terpenuhi secara nyata (cek isi filenya!), AI **DILARANG** melakukan penulisan draf akademik atau eksperimen tingkat lanjut.
- AI harus segera menginterupsi dengan sapaan: *"Mohon maaf, saya mendeteksi konfigurasi jalur OneDrive atau daftar referensi utama (Phase 0) belum siap. Mari kita tuntaskan konfigurasi di `sync_word.ps1` dan `ANTI_HALLUCINATION.md` terlebih dahulu."*

**Otomasi Onboarding:** Jika AI mendeteksi file `.docx` atau `.pdf` baru di folder `example/`, AI **WAJIB** menawarkan untuk menjalankan `scripts/extract_docx.py` atau `scripts/extract_pdfs.py` untuk mempelajari gaya bahasa user.

---

## 🗺️ Smart Auto-Routing System (WAJIB DIIKUTI)

Ketika user **TIDAK menyebut nama file tujuan secara eksplisit**, AI **wajib** menggunakan tabel routing di bawah ini untuk menentukan ke mana konten harus ditulis atau disimpan. Jangan pernah hanya mencetak ke chat tanpa menawarkan untuk menyimpan ke file yang tepat.

### Intent-to-File Routing Table

| Jika user meminta... | Kata kunci / Trigger | Tulis ke file ini | Aksi setelah menulis |
|---|---|---|---|
| Latar belakang / Background | "buat latar belakang", "tulis background", "rumusan masalah" | `supportFiles/handoff.md` | Tulis draf ke section Bab 1 di handoff |
| Tinjauan pustaka / Landasan teori | "landasan teori", "kajian pustaka", "tulis bab 2" | `supportFiles/handoff.md` | Tulis draf ke section Bab 2 di handoff |
| Metodologi / Metode penelitian | "metodologi", "tulis metode", "bab 3" | `supportFiles/handoff.md` | Tulis draf ke section Bab 3 di handoff |
| Hasil & Pembahasan | "hasil", "pembahasan", "bab 4" | `supportFiles/handoff.md` | Tulis draf ke section Bab 4 di handoff |
| Kesimpulan & Saran | "kesimpulan", "saran", "bab 5" | `supportFiles/handoff.md` | Tulis draf ke section Bab 5 di handoff |
| Keputusan teknis baru | "kita pakai X", "saya putuskan", "ganti metode", "gunakan Y" | `supportFiles/decisions_log.md` | Konfirmasi ke user |
| Ringkasan sesi / Progres hari ini | "rangkum sesi", "update progres", "simpan ingatan" | `supportFiles/handoff.md` | Konfirmasi ke user |
| Paper / Referensi baru | "cek paper ini", "tambah referensi", "paper tentang X" | `papers/index.md` + `supportFiles/ANTI_HALLUCINATION.md` | Assign REF-ID sementara |
| Kode / Script baru | "bikin script", "tulis kode untuk X", "buat fungsi" | `scripts/[nama_relevan].py` | Konfirmasi nama file ke user |
| Notebook eksperimen | "bikin notebook", "coba eksperimen", "eksplorasi data" | `notebooks/[nama_relevan].ipynb` | Konfirmasi nama file ke user |
| Pertanyaan teknis terbuka | "belum tahu cara X", "perlu cari tahu", "masih ragu" | `supportFiles/open_questions.md` | Catat sebagai item open question |

### Aturan Routing

1. **Sebelum menulis**, konfirmasi dengan cepat: _"Saya akan menyimpan ini ke `[nama file]`. Lanjut?"_
2. **Jika file belum ada**, buat file baru sesuai tabel di atas — jangan tulis di chat saja.
3. **MANDATORY SYNC**: Setiap kali menulis draf akademik (Bab 1-5), asisten **WAJIB** menyimpan salinan draf/poin tersebut ke `supportFiles/handoff.md` di bawah section `## Current Text Drafts`. Ini krusial agar memori aktif tetap terjaga antar sesi.
4. **Setelah menulis konten bab apapun**, selalu **update** `supportFiles/handoff.md` bagian status bab.
5. **TIDAK BOLEH** hanya mencetak draf di chat. Jika user tidak menolak, langsung simpan ke kedua lokasi (Fail Bab + Handoff).
6. **Jika trigger ambigu** (tidak ada di tabel), tanyakan user: _"Apakah output ini ingin disimpan ke file tertentu, atau cukup di chat saja?"_

---

## Arsitektur Proyek (Wajib Diingat)

```
Pipeline Utama:
[Modul A] ──→ [Modul B]
```

| Komponen | Detail |
|---|---|
| Algoritma / Model Utama | Lihat `gemini.md` |
| Dataset baseline | Lihat `gemini.md` |
| Metode / Pendekatan | Lihat `gemini.md` |
| Framework | Lihat `gemini.md` |
| Hardware target | Lihat `gemini.md` |

---

## Core Project Logic

| Feature | Mandatory Specification |
|---|---|
| **Task Focus** | [Fokus penelitian utama proyek ini] |
| **Trigger Mechanism** | [Logika khusus jika ada] |

---

## Aturan & Batasan Penting (Wajib Dipatuhi)

### ⚠️ Constraints Utama
- ❌ **TIDAK** menggunakan metode di luar scope: [Cakupan Batasan].
- ❌ **TIDAK** menggunakan framework lain selain yang disepakati.

### 📝 Hybrid Language & Writing Standards
- **Language Protocol**:
    - **English (🇬🇧)**: All AI-facing instructions, technical definitions, and thesis prose drafts.
    - **Indonesian (🇮🇩)**: Summary logs, user-facing guides, and general communication.
- **Prose Standards**:
    - **Citation**: Strict IEEE `[n]` at the end of sentences.
    - **Typography**: Strictly NO em-dash (`—`). Use LaTeX for math.

---

## Referensi Paper Utama

| Paper | Kontribusi ke Proyek |
|---|---|
| [Paper 1] | [Kontribusi] |
| [Paper 2] | [Kontribusi] |

---

## Terminologi yang Benar

| ❌ Jangan Tulis | ✅ Tulis Ini | Alasan |
|---|---|---|
| "[Kata Salah]" | "[Kata Benar]" | [Alasan koreksi] |

---

## Pengelolaan Support Files

### Update Wajib Setelah Setiap Sesi

Setelah menyelesaikan pekerjaan signifikan, AI **wajib** memperbarui:
1. **`handoff.md`** — update status stage, pending actions, last session summary
2. **`decisions_log.md`** — tambahkan keputusan baru yang dibuat dalam sesi ini

### Template Update handoff.md
```markdown
## Last Session Summary (YYYY-MM-DD)

- [Apa yang dikerjakan]
- [Hasil yang dicapai]
- [File yang dibuat/dimodifikasi]
```

### ✨ Academic Document Standards (MANDATORY)

Setiap kali melakukan ekspor ke format Word (.docx), asisten **WAJIB** menggunakan file template berikut sebagai basis (Seed Document) untuk menjaga konsistensi penomoran BAB dan Sub-bab:

- **Template Path**: `.agents/resources/academic_template.docx`
- **Aturan Pemetaan Gaya**:
    - **BAB / Judul Bab** ➔ Gunakan gaya `Heading 1` (Format otomatis: BAB I, BAB II, dst).
    - **Sub-bab (Level 1)** ➔ Gunakan gaya `Heading 2` (Format otomatis: 1.1, 1.2, dst).
    - **Sub-bab (Level 2)** ➔ Gunakan gaya `Heading 3` (Format otomatis: 1.1.1, dst).
    - **Isi Draf** ➔ Gunakan gaya `Normal`.
    - **Tabel** ➔ Gunakan gaya tabel `Table Grid`.

---

## 🛠️ Script Helper & Utilities (WAJIB TAHU)

Berikut adalah daftar skrip alat bantu yang sudah tertanam di `scripts/`. AI **wajib** menawarkan atau langsung mengeksekusi skrip ini menggunakan `run_command` jika konteks percakapan sesuai:

| Nama Skrip | Kapan AI harus menggunakannya? | Perintah Terminasi (Gunakan `rtc` atau `python`) |
|---|---|---|
| `scripts/extract_pdfs.py` | Saat user punya file `.pdf` baru di folder `papers/` dan meminta AI membacanya. Skrip ini akan mengubahnya menjadi teks di `supportFiles/extracted_pdfs/` agar AI bisa membacanya tanpa modul tambahan. | `python scripts/extract_pdfs.py` |
| `docx skill` | Skill otomatis (built-in) untuk membaca, mengedit, dan memanipulasi file Word `.docx` secara profesional. | Otomatis aktif saat membahas file `.docx` |
| `scripts/docx_surgery.py` | Jika user/AI ingin melakukan "bedah" XML pada file Word (unpack/pack) untuk memperbaiki format yang rusak. | `python scripts/docx_surgery.py` |
| `scripts/extract_docx.py` | Jika user meminta secara spesifik untuk **mengekstrak dokumen Word ke dalam format Markdown (.md)**. | `python scripts/extract_docx.py [file.docx] [file.md]` |
| `scripts/sync_word.ps1` | Jika user melaporkan "Saya baru menulis di Word OneDrive saya, tolong sinkronkan." Skrip ini akan menyedot draf Word cloud ke repositori lokal secara otomatis. | `powershell scripts/sync_word.ps1` |
| `scripts/convert_citations.py` | Jika user ingin merapikan draf `handoff.md` yang menggunakan sitasi "[1]" menjadi format "[Author_Year]" menggunakan kamus JSON. Format wajib sebelum dipublish! | `python scripts/convert_citations.py` |

---

## Kontak & Konteks
- Lihat `gemini.md` untuk detail identitas mahasiswa, hardware, dan bahasa komunikasi.
