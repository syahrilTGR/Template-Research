# 🎓 Project Template: Collaborative Research & Coding

Selamat datang di workspace proyek ini! Directory ini telah disiapkan sebagai template standar untuk pengerjaan penelitian, skripsi (TA), atau proyek coding kolaboratif dengan bantuan AI Agent.

---

## 🚀 Quick Start (Windows)
Siapkan lingkungan riset Anda dalam satu klik:
```powershell
.\scripts\setup_env.ps1
```

## ✨ Fitur Unggulan
- **📝 Handoff-Centric Drafting**: Seluruh draf terkonsentrasi di satu titik (`supportFiles/handoff.md`) untuk meminimalkan halusinasi AI.
- **💉 Docx Surgery**: Bedah file Word yang rusak atau edit XML penomoran secara langsung via `scripts/docx_surgery.py`.
- **🧪 Sterile Word Templates**: Menghasilkan file Word akademik (BAB I, 1.1, dst) tanpa jejak data pribadi di repositori.
- **📄 AI-Driven Extraction**: Ekstraksi metrik dari jurnal PDF & gaya bahasa dari proposal lama secara otomatis.
- **🔄 Sync Power**: Sinkronisasi draf antara Markdown (AI) dan Word (OneDrive) dengan satu klik.

---

## 📂 Struktur Folder & Fungsi

**Last updated:** 2026-04-16

Berikut adalah penjelasan fungsi untuk tiap directory agar pengerjaan tetap rapi dan terorganisir:

| Directory | Fungsi | Contoh Isi |
|---|---|---|
| `notebooks/` | Eksperimen, eksplorasi data, dan riset interaktif. | `.ipynb` file |
| `scripts/` | Kode sumber utama, automation, dan utilitas (termasuk skrip sinkronisasi Word ke Markdown). | `.py`, `.ps1`, `.bat` |
| `models/` | Penyimpanan artefak hasil perhitungan, model, atau bobot utama. | `.pth`, `.pt`, `.onnx`, `.bin` |
| `results/` | Output evaluasi, metrik hasil, grafik visualisasi, dan file log. | `.csv`, `.png`, `.log` |
| `papers/` | Koleksi literatur utama (jurnal/prosiding) yang menjadi dasar riset. | `artikel.pdf` |
| `reference/` | Materi pendukung seperti dokumentasi, tutorial, atau potongan kode referensi. | `.pdf`, `.md`, `.txt` |
| `dataset/` | Data mentah (raw) atau data yang sudah diproses untuk riset. | `data/`, `images/`, `tables/` |
| `example/` | Demo singkat atau skrip "Hello World" untuk memastikan sistem berjalan. | `demo.py`, `test_env.py` |
| `image/` | Aset gambar untuk dokumentasi README, flowchart, atau diagram laporan. | `.jpg`, `.svg` |
| `intelligence/` | **LLM Wiki (Obsidian Vault)**: Pusat memori AI, glosarium, dan konsep. | `_INDEX.md`, `konsep/` |
| `supportFiles/` | Konfigurasi pendukung, database referensi, dan file draf aktif asisten AI. | `handoff.md`, `ACTION_PLAN.md` |
| `.agents/` | Pusat kontrol AI Antigravity (Aturan, Skill, dan Workflow otomatis). | `skills/`, `workflows/` |

---

## 🤖 Menggunakan AI Assistant (Antigravity)

Proyek ini dilengkapi dengan asisten AI yang bisa membantu menulis subbab laporan, menjelaskan kode, hingga melakukan riset otomatis.

- **Panduan Cepat**: Lihat file [HOW_TO_USE_ANTIGRAVITY.md](./HOW_TO_USE_ANTIGRAVITY.md) untuk mempelajari cara memanggil workflow asisten.
- **Support**: Asisten ini memahami konteks proyek melalui file-file di directory `.agents`.

---
*Developed with ❤️ as a Universal Research Template.*
