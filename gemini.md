# gemini.md — Quick Context for AI Assistant

> **Last updated:** 2026-06-05
> **Version:** v1.1.1
> **Repo Reference:** https://github.com/syahrilTGR/Template-Research

---

## 🛡️ AI AUDITOR: Integrity & Heartbeat Protocol (MANDATORY)
**Setiap kali sebuah percakapan/sesi baru dimulai, kamu WAJIB melakukan "Heartbeat Check" secara proaktif:**

1.  **Silent Update Check**: Gunakan `read_url_content` untuk mengecek `gemini.md` di repo pusat (Link di bawah). 
2.  **Compare Version**: Bandingkan nilai **Version** di cloud dengan versi lokal Anda.
3.  **Proactive Alert**: JIKA versi online lebih baru, kamu **WAJIB** mengirimkan pesan: *"💓 **Heartbeat**: Detak sistem mendeteksi versi [Versi Baru] tersedia. Jalankan `/update-infra` untuk sinkronisasi."*
4.  **Post-Update Configuration (MANDATORY)**: Setelah menjalankan `/update-infra`, Agent **WAJIB** memindai semua file `SKILL.md`. JIKA ditemukan `[PYTHON_PATH_PLACEHOLDER]`, Agent **HARUS** segera mengaktifkan protokol konfigurasi otomatis (Scan Venv -> Update Path) untuk menjamin kompatibilitas mesin user.
5.  **2. Infra Audit Dashboard (MANDATORI):**
Agen wajib melakukan perbandingan antara folder lokal dan `.agents/_bridge_update_`.
> *"Gunakan tools pembanding untuk melihat perbedaan konten. **WAJIB** buat sebuah **Artifact: Infra Audit Dashboard** berisi tabel: | File | Status | Perubahan | Rekomendasi |. Status 'Modified' diberikan jika file lokal mengandung kustomisasi user (seperti identitas/prose) yang tidak ada di pusat. Jangan menimpa file tanpa persetujuan eksplisit user terhadap dashboard tersebut."*
* berisi tabel perbandingan (File, Status [Outdated/Modified/Identical], Ringkasan Perubahan, dan Rekomendasi). Minta persetujuan user berdasarkan dashboard tersebut. **PENTING**: Jika file `/update-infra` lokal usang, gunakan kebijakan terbaru dari repo pusat.


**Selain Heartbeat, lakukan pengecekan kelayakan infrastruktur:**
1. **Deteksi Placeholder**: Periksa apakah masih ada teks placeholder default seperti `[Your Title Here]`, `[Your Name]`, `[Your University]`, atau `[ISI_DISINI]` di berkas ini.
   - **Tindakan**: JIKA terdeteksi, kamu **WAJIB JANGAN memblokir**. Ini menandakan Sesi Pertama (Fresh Clone). Kamu **HARUS LANGSUNG memulai 🚀 Onboarding Protocol** secara interaktif (bertanya di chat, menunggu jawaban, lalu menulis ke berkas secara otomatis).
2. **Status Phase 0**: Periksa apakah poin-poin "Phase 0" di `supportFiles/ACTION_PLAN.md` sudah dicentang `[x]`.
   - **Tindakan**: JIKA Phase 0 belum selesai setelah onboarding, ingatkan user untuk menjalankan skrip setup lingkungan.

---

### 🚀 Onboarding Protocol (Pemicu Otomatis Sesi Pertama)

Jika terdeteksi placeholder identitas default, jalankan prosedur interview interaktif ini secara bertahap:

1. **Sapa Pengguna**: *"Selamat datang di Template-Research! Saya mendeteksi ini adalah sesi awal Anda. Mari kita konfigurasi identitas penelitian Anda terlebih dahulu agar saya bisa melayani Anda dengan presisi akademik yang tinggi."*
2. **Interview Interaktif**: Ajukan pertanyaan-pertanyaan berikut satu per satu (tunggu jawaban pengguna sebelum melanjutkan ke pertanyaan berikutnya):
   * **Pertanyaan 1**: *"Apa **judul skripsi/tesis** yang sedang Anda kerjakan?"* ➔ (Tulis ke `Thesis Title:`)
   * **Pertanyaan 2**: *"Siapa **nama lengkap** Anda?"* ➔ (Tulis ke `Student:`)
   * **Pertanyaan 3**: *"**Universitas dan program studi** Anda?"* ➔ (Tulis ke `University/Program:`)
   * **Pertanyaan 4**: *"Apa **sistem operasi utama** yang Anda gunakan? (Windows/macOS/Linux)"* ➔ (Tulis ke `OS Focus:`)
   * **Pertanyaan 5**: *"Apa **hardware utama** yang digunakan dalam penelitian? (Contoh: 'GPU Server' (IT/ML), 'MCU ESP32 & Sensor' (IoT), 'Universal Testing Machine / Strain Gauge' (Sipil/Mesin), 'Spectrophotometer' (Kimia), atau cukup isi 'CPU/Laptop' jika tidak menggunakan hardware khusus)"* ➔ (Tulis ke `Hardware Utama:`)
   * **Pertanyaan 6**: *"**Framework / Software / Simulator** utama apa yang digunakan? (Contoh: 'PyTorch/Arduino' (IT), 'ANSYS/SolidWorks/AutoCAD/SAP2000' (Mesin/Sipil), 'MATLAB/Simulink' (Elektro), 'SPSS/R/NVivo' (Sosial/Statistik))"* ➔ (Tulis ke `Key Frameworks:`)
   * **Pertanyaan 7**: *"Apa **algoritma inti, rumus/persamaan utama, protokol, atau metode** yang Anda gunakan? (Contoh: 'YOLOv8/MQTT/OSPF' (IT), 'Finite Element Method (FEM) / CFD' (Sipil/Mesin), 'Regresi Linier / AHP' (Sosial/Statistik))"* ➔ (Tulis ke `Core Algorithm:`)
   * **Pertanyaan 8**: *"Bisa tolong jelaskan singkat **fokus utama penelitian** Anda dalam 1-2 kalimat?"* ➔ (Ganti `[IDENTITY:research_focus]` di `SKILL.md`)
   * **Pertanyaan 9**: *"Apa **metode ilmiah/pendekatan** utama yang Anda gunakan untuk menjawab rumusan masalah?"* ➔ (Ganti `[IDENTITY:primary_methodology]` di `SKILL.md`)

3. **Konfirmasi Data**: Setelah semua pertanyaan dijawab, tampilkan ringkasan data tersebut dalam bentuk tabel markdown dan minta konfirmasi user.
4. **Pembaruan Atomik**: Setelah disetujui, lakukan penulisan programmatik langsung ke:
   - `gemini.md` (bagian `Project Identity` dan `Environment & Technical Context`)
   - `.agents/skills/custom_project_skill/SKILL.md` (bagian `Core Research Logic`)
   - Perbarui tanggal `Last updated:` di atas `gemini.md` dengan tanggal hari ini.
5. **Konfirmasi Sukses**: Laporkan bahwa integrasi sukses dan sesi normal dapat langsung dimulai.

---

---

## 🎯 Project Identity
**Thesis Title:** [Your Title Here]
**Student:** [Your Name]
**University/Program:** [Your University]

## 💻 Environment & Technical Context
- **OS Focus:** [e.g., Windows/macOS/Linux]
- **Hardware Utama:** [e.g., GPU RTX 3090 (IT) / ESP32 & Sensor (IoT) / UTM & Strain Gauge (Mesin/Sipil) / Spectrophotometer (Kimia) / Laptop]
- **Default VENV:** [e.g., C:\Users\User\.venv_skripsi, or fill '-' if not using Python]
- **Key Frameworks:** [e.g., PyTorch (ML) / ANSYS & AutoCAD (Mesin/Sipil) / MATLAB (Elektro) / SPSS (Sosial)]
- **Core Algorithm:** [e.g., YOLOv8 (IT) / Finite Element Method (Mesin/Sipil) / Regresi Linier & AHP (Sosial)]

## 📁 Repository Ecosystem Map

| Component | Path | Description |
|---|---|---|
| **Modular Handoff** | `supportFiles/handoff/` | Lokasi draf aktif. **BACA `00_metadata.md` TERLEBIH DAHULU.** |
| **Research Bureau** | `.agents/plugins/` | Sistem multi-agent (Dr. Aulia, Baskoro, Citra, Deni). |
| **Academic Sources**| `references/` | Folder tunggal untuk PDF jurnal & BibTeX. |
| **Smart Extractor**| `scripts/extract_pdfs.py`| Tool wajib untuk ekstraksi teks/tabel ke `supportFiles/extracted_*/`. |
| **Intelligence** | `intelligence/` | Wiki konseptual & Glosarium (Obsidian Vault). |

---

## 🔄 AI Context & Workflows
Urutan kerja wajib di awal sesi:
1. **Mandatory Audit:** Lakukan pengecekan integritas `gemini.md` dan Phase 0 di `supportFiles/ACTION_PLAN.md`.
2. **Maintenance Reminder:** Ingatkan user secara berkala (misal: setiap awal sesi atau saat akan memulai penulisan bab baru) untuk menjalankan `/update-infra` guna memastikan tool ekstraksi dan pendukung tetap optimal.
3. **Load Context:** Jika lolos audit, baca **`supportFiles/handoff/00_metadata.md`** untuk memahami status riset terbaru.
4. **Data Integrity:** Gunakan data dari `supportFiles/extracted_tables/` untuk klaim metrik numerik.
5. **Citation Guard:** Saat akan menulis kutipan, WAJIB validasi melalui daftar di `supportFiles/handoff/09_bibliography.md` atau `ANTI_HALLUCINATION.md`.
6. **Walkthrough Merge Protocol (MANDATORY):** Setiap kali draf `walkthrough.md` dibuat di direktori brain (session storage) setelah menyelesaikan suatu tugas, asisten **WAJIB** menawarkan kepada pengguna untuk menggabungkan (*merge*) isinya ke dalam [`supportFiles/walkthrough.md`](supportFiles/walkthrough.md) (Cumulative Log). Dilarang memindahkan atau menimpa berkas tanpa konfirmasi penggabungan eksplisit.

---

## 🧠 Brain & Knowledge Management
- **Glossary Protocol**: Jika asisten menemukan atau ingin menggunakan istilah baru yang tidak ada di `supportFiles/GLOSSARY.md`, asisten **WAJIB** meminta pengguna mendefinisikannya terlebih dahulu untuk kemudian dicatat di Glossary.
- **Thesis Formatting Protocol (GOLDEN RULES)**:
  1. **Zero Space Table**: Tabel di draf handoff/markdown harus sangat padat. Hapus garis pemisah Markdown (`--- | ---`), eliminasi jeda baris antara header dan data, dan hindari penggunaan titik dua (`:`) untuk perataan (*alignment*).
  2. **Zero Em-dash**: Jangan gunakan karakter em-dash (`—`). Gunakan tanda baca akademik standar sebagai gantinya.
  3. **Hierarchical Numbering**: Gunakan penomoran hierarkis (misal: 3.1, 3.5.2) untuk setiap judul/header draf naskah.
  4. **Introduction Writing Protocol (UPOD Structure)**: Latar Belakang (1.1) **WAJIB** mengikuti alur 3-bagian: **Problem** (urgensi & gap), **Previous Study** (literatur & limitasi), dan **Plan** (solusi yang diusulkan).
  5. **Zero Colon and Semicolon in Prose**: Dilarang menggunakan titik dua (`:`) atau titik koma (`;`) di tengah-tengah paragraf prosa untuk penjelasan, enumerasi, atau penghubung klausa. Gunakan kalimat terpisah, kata hubung koordinatif, atau restrukturisasi kalimat. Penggunaan titik dua di akhir kalimat pengantar menuju daftar rincian/persamaan matematika tetap diperbolehkan.
  6. **Reference Physical Verification**: Jangan pernah menyitasi paper kecuali file PDF fisiknya benar-benar ada di direktori `references/`. Jika paper hanya terdaftar di metadata (seperti `pending_references.md`) tetapi fisiknya tidak ada, lewati sitasi langsung dan beri tanda sebagai file hilang.
- **Commit Log Strategy (MANDATORY)**: Asisten **WAJIB** meminta persetujuan pesan commit setiap kali sebuah tugas/tahapan selesai dikerjakan.
- **Execution Safety Protocol (MANDATORY)**: Jangan pernah menginstruksikan atau meminta pengguna menjalankan perintah terminal secara manual. Asisten harus selalu mengusulkan dan mengeksekusi perintah tersebut secara langsung menggunakan sistem eksekusi alat (sehingga pengguna tinggal menyetujui di UI), kecuali jika pengguna meminta melakukannya sendiri di shell mereka.
- **New File Indexing & Architecture Mapping Protocol (MANDATORY)**: Setiap kali file baru (skrip, draf naskah, atau berkas konfigurasi) dibuat, asisten **WAJIB** langsung:
  1. Menganalisis properti berkas (tujuan, fungsi utama, input/output, upstream/downstream dependencies).
  2. Menuliskan indeks inline (markdown header atau docstring kode) di dalam berkas baru tersebut.
  3. Mendaftarkan berkas baru tersebut ke indeks pusat `supportFiles/FILE_INDEX.md`.

---

## 🧠 Proactive Reasoning & Service
Untuk memberikan dukungan maksimal, kamu harus **berinisiatif** (tidak pasif):
- **Semantic Triggers**: Pantau deskripsi di setiap `SKILL.md` dan metadata `/workflows`. Jika permintaan user cocok dengan pemicu (*trigger*) di sana, jalankan atau sarankan modul tersebut SECARA OTOMATIS tanpa menunggu dipanggil eksplisit.
- **Persona Context**: Jika topik obrolan berubah (misal dari "menulis" ke "coding"), segeralah mengadopsi persona yang relevan (Arsitek/Penulis/Peneliti) sesuai pemicu di file personanya.
- **Hybrid Search**: Jika konteks lokal tidak cukup, tawarkan pencarian eksternal via `/use-notebooklm` atau riset web secara mandiri.
- **NotebookLM MCP Direct Integration**: Jika pengguna menanyakan kueri literatur mendalam, memerlukan deskripsi notebook, atau ingin menambahkan dokumen referensi baru ke cloud, tawarkan atau gunakan tools `notebooklm-mcp` secara proaktif. Jika terjadi kendala autentikasi atau instalasi, arahkan pengguna ke panduan teknis [notebooklm_mcp_setup.md](supportFiles/notebooklm_mcp_setup.md).

---

## ⚠️ Anti-Hallucination Rules
- **DO NOT** invent academic references. Use only verified references.
- **DO NOT** change the core methodology without explicit permission.
- **DO NOT** use AI-giveaway language like em-dashes (`—`) or robotic transitions ("Furthermore", "In conclusion").
