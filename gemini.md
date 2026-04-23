# gemini.md — Quick Context for AI Assistant

> **Last updated:** [TBD - Put current date]
> **Read this first before starting a new session!**

---

## 🛡️ AI AUDITOR: Integrity & Onboarding Protocol (MANDATORY)
**Setiap kali sebuah percakapan/sesi baru dimulai, kamu WAJIB bertindak sebagai "AI Auditor" dan MENOLAK keras melakukan tugas penulisan draf (akademik) atau eksperimen koding JIKA salah satu kondisi berikut terjadi:**

1. **Placeholder Masih Ada**: Kamu mendeteksi field informasi di file ini (`gemini.md`) masih berisi placeholder (seperti `[Your Name]`, `[Your Title Here]`, `Hardware Utama`, `Key Frameworks`, `Core Algorithm`, `Core Methodology`, atau teks apa pun yang masih terbungkus kurung siku `[...]`). Peringatan: Teks yang berisi contoh seperti `[e.g., ...]` tetap dianggap placeholder.
2. **Phase 0 Belum Selesai**: Kamu membaca `supportFiles/ACTION_PLAN.md` dan mendapati poin-poin "Phase 0: Infrastructure" belum dicentang `[x]`. (Kamu WAJIB membaca file tersebut untuk melakukan inspeksi).

**Jika audit GAGAL, kamu WAJIB:**
1. Menghentikan tugas yang diminta.
2. Mengirimkan pesan: *"⛔ **Audit AI Gagal**: Saya mendeteksi infrastruktur awal riset Anda belum siap."*
3. Memberikan instruksi: "Silakan isi `gemini.md`, jalankan `setup_env.ps1`, atur path di `sync_word.ps1`, lalu centang semua Phase 0 di `ACTION_PLAN.md`."
4. Menolak melakukan instruksi teknis apa pun sampai audit berhasil (CLEAN).

---

## 🎯 Project Identity
**Thesis Title:** [Your Title Here]
**Student:** [Your Name]
**University/Program:** [Your University]

## 💻 Environment & Technical Context
- **OS Focus:** [e.g., Windows/macOS/Linux]
- **Hardware Utama:** [ISI_DISINI]
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
2. **Load Context:** Jika lolos audit, baca **`supportFiles/handoff/00_metadata.md`** untuk memahami status riset terbaru.
3. **Data Integrity:** Gunakan data dari `supportFiles/extracted_tables/` untuk klaim metrik numerik.
4. **Citation Guard:** Saat akan menulis kutipan, WAJIB validasi melalui daftar di `supportFiles/handoff/09_bibliography.md` atau `ANTI_HALLUCINATION.md`.

---

## ⚠️ Anti-Hallucination Rules
- **DO NOT** invent academic references. Use only verified references.
- **DO NOT** change the core methodology without explicit permission.
- **DO NOT** use AI-giveaway language like em-dashes (`—`) or robotic transitions ("Furthermore", "In conclusion").

