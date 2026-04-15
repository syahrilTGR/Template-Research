---
name: custom_project_skill
description: >
  Skill template untuk mendefinisikan arsitektur sistem, batasan logika, dan konteks paper untuk AI assistant di proyek baru.
  Gunakan file ini sebagai ruang untuk "mengajari" AI tentang proyek spesifik Anda.
---

# Custom Project Skill

## Deskripsi Proyek

Proyek skripsi: **[Judul Proyek Anda]**

Mahasiswa: **[Nama Anda]** | Program Studi: [Prodi Anda], [Universitas Anda]

---

Each time a new AI session begins, the MANDATORY first step is to follow the **Hybrid Context Protocol**:

1. Read **`supportFiles/PROMPT_TEMPLATE.md`** for the session start sequence.
2. Load **`supportFiles/handoff.md`** to understand the latest project state and prose drafts.
3. Cross-reference **`papers/index.md`** and **`supportFiles/ANTI_HALLUCINATION.md`** for valid technical citations.

Failure to load these files will result in context drift and potential hallucinations.

---

## 🗺️ Smart Auto-Routing System (WAJIB DIIKUTI)

Ketika user **TIDAK menyebut nama file tujuan secara eksplisit**, AI **wajib** menggunakan tabel routing di bawah ini untuk menentukan ke mana konten harus ditulis atau disimpan. Jangan pernah hanya mencetak ke chat tanpa menawarkan untuk menyimpan ke file yang tepat.

### Intent-to-File Routing Table

| Jika user meminta... | Kata kunci / Trigger | Tulis ke file ini | Aksi setelah menulis |
|---|---|---|---|
| Latar belakang / Background | "buat latar belakang", "tulis background", "rumusan masalah", "tujuan penelitian" | `thesis_bureau/bab1_pendahuluan.md` | Update status di `supportFiles/handoff.md` |
| Tinjauan pustaka / Landasan teori | "landasan teori", "kajian pustaka", "tulis bab 2", "previous research" | `thesis_bureau/bab2_tinjauan_pustaka.md` | Update status di `supportFiles/handoff.md` |
| Metodologi / Metode penelitian | "metodologi", "tulis metode", "diagram alir sistem", "bab 3" | `thesis_bureau/bab3_metodologi.md` | Update status di `supportFiles/handoff.md` |
| Hasil & Pembahasan | "hasil", "pembahasan", "analisis hasil", "bab 4" | `thesis_bureau/bab4_hasil.md` | Update status di `supportFiles/handoff.md` |
| Kesimpulan & Saran | "kesimpulan", "saran", "bab 5" | `thesis_bureau/bab5_kesimpulan.md` | Update status di `supportFiles/handoff.md` |
| Keputusan teknis baru | "kita pakai X", "saya putuskan", "ganti metode", "gunakan Y" | `supportFiles/decisions_log.md` | Konfirmasi ke user |
| Ringkasan sesi / Progres hari ini | "rangkum sesi", "update progres", "simpan ingatan" | `supportFiles/handoff.md` | Konfirmasi ke user |
| Paper / Referensi baru | "cek paper ini", "tambah referensi", "paper tentang X" | `papers/index.md` + `supportFiles/ANTI_HALLUCINATION.md` | Assign REF-ID sementara |
| Kode / Script baru | "bikin script", "tulis kode untuk X", "buat fungsi" | `scripts/[nama_relevan].py` | Konfirmasi nama file ke user |
| Notebook eksperimen | "bikin notebook", "coba eksperimen", "eksplorasi data" | `notebooks/[nama_relevan].ipynb` | Konfirmasi nama file ke user |
| Pertanyaan teknis terbuka | "belum tahu cara X", "perlu cari tahu", "masih ragu" | `supportFiles/open_questions.md` | Catat sebagai item open question |

### Aturan Routing

1. **Sebelum menulis**, konfirmasi dengan cepat: _"Saya akan menyimpan ini ke `[nama file]`. Lanjut?"_
2. **Jika file belum ada**, buat file baru sesuai tabel di atas — jangan tulis di chat saja.
3. **Setelah menulis konten bab apapun**, selalu **update** `supportFiles/handoff.md` bagian status bab.
4. **Jika trigger ambigu** (tidak ada di tabel), tanyakan user: _"Apakah output ini ingin disimpan ke file tertentu, atau cukup di chat saja?"_
5. **TIDAK BOLEH** hanya mencetak prose akademik di chat tanpa menawarkan untuk menyimpan ke file.

---

## Arsitektur Proyek (Wajib Diingat)

```
Pipeline Utama:
[Modul A] ──→ [Modul B]
```

| Komponen | Detail |
|---|---|
| Algoritma / Model Utama | [Isi model Anda, misalnya: YOLO, ResNet, dsb] |
| Dataset baseline | [Deskripsi dataset awal] |
| Metode / Pendekatan | [Metode yang diusulkan] |
| Framework | **[Misal: PyTorch / TensorFlow]** |
| Hardware target | [Misal: Laptop / Colab / Edge Device] |

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

---

## 🛠️ Script Helper & Utilities (WAJIB TAHU)

Berikut adalah daftar skrip alat bantu yang sudah tertanam di `scripts/`. AI **wajib** menawarkan atau langsung mengeksekusi skrip ini menggunakan `run_command` jika konteks percakapan sesuai:

| Nama Skrip | Kapan AI harus menggunakannya? | Perintah Terminasi (Gunakan `rtc` atau `python`) |
|---|---|---|
| `scripts/extract_pdfs.py` | Saat user punya file `.pdf` baru di folder `papers/` dan meminta AI membacanya. Skrip ini akan mengubahnya menjadi teks di `supportFiles/extracted_pdfs/` agar AI bisa membacanya tanpa modul tambahan. | `rtk python scripts/extract_pdfs.py` |
| `scripts/extract_docx.py` | Jika user ingin membedah file Word (`.docx`) menjadi susunan Markdown untuk dibaca AI atau diproses sebagai draf. | `rtk python scripts/extract_docx.py [file.docx] [file.md]` |
| `scripts/sync_word.ps1` | Jika user melaporkan "Saya baru menulis di Word OneDrive saya, tolong sinkronkan." Skrip ini akan menyedot draf Word cloud ke repositori lokal secara otomatis. | `powershell scripts/sync_word.ps1` |
| `scripts/convert_citations.py` | Jika user ingin merapikan draf `handoff.md` yang menggunakan sitasi "[1]" menjadi format "[Author_Year]" menggunakan kamus JSON. Format wajib sebelum dipublish! | `rtk python scripts/convert_citations.py` |

---

## Kontak & Konteks

- **Mahasiswa:** [Nama Anda]
- **Hardware utama:** [Hardware dev]
- **Bahasa komunikasi:** Bahasa Indonesia (percakapan), Python + matematika (kode/formula)
