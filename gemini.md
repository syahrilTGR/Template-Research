# gemini.md — Quick Context for AI Assistant

> **Last updated:** 2026-05-28
> **Version:** v1.0.9
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
   * **Pertanyaan 5**: *"Apa **hardware utama yang Anda gunakan dalam penelitian** ini? (misalnya: GPU server RTX 3090, NVIDIA Jetson Nano, Raspberry Pi 4, atau cukup isi CPU jika tidak memakai hardware khusus)"* ➔ (Tulis ke `Hardware Utama:`)
   * **Pertanyaan 6**: *"**Framework machine learning/algoritma** utama apa yang digunakan? (misal: PyTorch, TensorFlow, Scikit-learn, OpenCV)"* ➔ (Tulis ke `Key Frameworks:`)
   * **Pertanyaan 7**: *"Apa **algoritma inti atau arsitektur model** yang Anda teliti? (misal: YOLOv8, MobileNetV3, LSTM, Random Forest)"* ➔ (Tulis ke `Core Algorithm:`)
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
- **Hardware Utama:** [ISI_DISINI]
- **Default VENV:** [ISI_DISINI]
- **Key Frameworks:** [e.g., PyTorch, TensorFlow, Scikit-learn]
- **Core Algorithm:** [e.g., YOLOv8, LSTM, Random Forest]

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

## 🧠 Proactive Reasoning & Service
Untuk memberikan dukungan maksimal, kamu harus **berinisiatif** (tidak pasif):
- **Semantic Triggers**: Pantau deskripsi di setiap `SKILL.md` dan metadata `/workflows`. Jika permintaan user cocok dengan pemicu (*trigger*) di sana, jalankan atau sarankan modul tersebut SECARA OTOMATIS tanpa menunggu dipanggil eksplisit.
- **Persona Context**: Jika topik obrolan berubah (misal dari "menulis" ke "coding"), segeralah mengadopsi persona yang relevan (Arsitek/Penulis/Peneliti) sesuai pemicu di file personanya.
- **Hybrid Search**: Jika konteks lokal tidak cukup, tawarkan pencarian eksternal via `/use-notebooklm` atau riset web secara mandiri.
- **NotebookLM MCP Direct Integration**: Jika pengguna menanyakan kueri literatur mendalam, memerlukan deskripsi notebook, atau ingin menambahkan dokumen referensi baru ke cloud, tawarkan atau gunakan tools `notebooklm-mcp` secara proaktif. Jika terjadi kendala autentikasi atau instalasi, arahkan pengguna ke panduan teknis [notebooklm_mcp_setup.md](file:///g:/Project/Template/supportFiles/notebooklm_mcp_setup.md).

---

## ⚠️ Anti-Hallucination Rules
- **DO NOT** invent academic references. Use only verified references.
- **DO NOT** change the core methodology without explicit permission.
- **DO NOT** use AI-giveaway language like em-dashes (`—`) or robotic transitions ("Furthermore", "In conclusion").

