# gemini.md — Quick Context for AI Assistant

> **Last updated:** [TBD - Put current date]
> **Read this first before starting a new session!**

---

## 🛡️ AI AUDITOR: Integrity & Onboarding Protocol (MANDATORY)
**Setiap kali sebuah percakapan/sesi baru dimulai, kamu WAJIB bertindak sebagai "AI Auditor" dan MENOLAK keras melakukan tugas penulisan draf (akademik) atau eksperimen koding JIKA salah satu kondisi berikut terjadi:**

1. **Placeholder Masih Ada**: Kamu mendeteksi field informasi di file ini (`gemini.md`) masih berisi placeholder (seperti `[Your Name]`, `[Your Title Here]`, `Hardware Utama`, `Key Frameworks`, `Core Algorithm`, atau teks apa pun yang masih terbungkus kurung siku `[...]`). Peringatan: Teks yang berisi contoh seperti `[e.g., ...]` tetap dianggap placeholder.
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

---

## 📁 Support Files Tracking

All documentation is stored in `supportFiles/` to maintain continuity between AI sessions.

| File | Purpose |
|---|---|
| `handoff.md` | **READ THIS FIRST** — Current status, pending actions, and active context |
| `ACTION_PLAN.md` | Chapter-by-chapter progression checklist |
| `decisions_log.md` | Record of technical/architectural decisions |
| `pending_references.md` | List of citations that need to be found/verified |

---

## 🔄 AI Context & Workflows
Urutan kerja wajib di awal sesi:
1. **Mandatory Audit:** Lakukan pengecekan integritas `gemini.md` dan Phase 0 di `supportFiles/ACTION_PLAN.md`.
2. **Load Context:** Jika lolos audit, baca `supportFiles/handoff.md` untuk memahami progres terakhir.
3. **Citation Guard:** Saat akan menulis kutipan, WAJIB validasi melalui daftar di `supportFiles/ANTI_HALLUCINATION.md`.

---

## ⚠️ Anti-Hallucination Rules
- **DO NOT** invent academic references. Use only verified references.
- **DO NOT** change the core methodology without explicit permission.
- **DO NOT** use AI-giveaway language like em-dashes (`—`) or robotic transitions ("Furthermore", "In conclusion").

