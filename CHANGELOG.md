# Changelog — Template Research 🚀

Semua perubahan penting pada infrastruktur riset ini akan dicatat di file ini.

## [v1.0.4] — 2026-04-29

### Added
- **Surgical XML Math Equation Insertion**: Panduan teknis baru untuk injeksi rumus matematika (`OMath`) secara presisi ke dalam struktur XML Word menggunakan font **Cambria Math**.
- **LaTeX-to-XML Mapping SOP**: Standar operasional untuk konversi manual notasi matematika kompleks (superscript, subscript, fraction) ke format OOXML.
- **Interactive Math Workflow**: Protokol keamanan 2-tahap (Draft -> Verify -> Surgical Convert) untuk mencegah kerusakan file saat melakukan injeksi rumus matematika.
- **Infra Audit Dashboard**: Protokol mandatori untuk transparansi update infrastruktur via tabel perbandingan otomatis.

## [v1.0.3] — 2026-04-28

### Added
- **Precise Code Extraction**: Penambahan skrip `extract_code.py` untuk ekstraksi blok kode karakter-per-karakter dari XML Word secara presisi.
- **High-Fidelity Docx SOP**: Sinkronisasi skill `docx` dengan standar global (Audit-Draft-Build-Verify).
- **Safe-Grafting Hotfix**: Injeksi protokol keamanan update-infra langsung ke `gemini.md` untuk menjamin backup otomatis.
- **Infra Audit Dashboard**: Sistem pelaporan update interaktif via Artifact untuk transparansi penuh sebelum melakukan overwriting file.

### Changed
- Hardening workflow `/update-infra` dengan protokol **Smart Audit & Backup** untuk melindungi kustomisasi user.

## [v1.0.2] — 2026-04-26

### Added
- **Smart Extractor V2.5 (High-Octane Parallel)**: Arsitektur baru menggunakan `ProcessPoolExecutor` untuk pemanfaatan 100% CPU core saat ekstraksi PDF massal.
- **Markdown Data Appendix**: Seluruh ekstraksi tabel kini dikonversi otomatis menjadi tabel Markdown yang disisipkan di akhir file `.md` hasil ekstraksi.
- **Dual-Mirror Renaming**: Protokol penamaan identik antara PDF di `references/` dan asisten `.md` di `supportFiles/extracted_pdfs/`.

### Changed
- Refaktor workflow `/extract-metrics` untuk menggunakan sistem `DATA APPENDIX` yang lebih presisi (Zero Hallucination logic).
- Menghapus skrip ekstraksi single-thread yang usang.

## [v1.0.1] — 2026-04-25

### Added
- **Heartbeat Protocol**: Prosedur pengecekan update otomatis yang proaktif setiap kali sesi dimulai.
- **Agentic Initiative**: Implementasi semantic triggers pada seluruh skill/persona.
- **Universal Sterilization**: Pembersihan total kode spesifik agar repo 100% template-agnostik.
- **Draw.io Workflow**: Penomoran SOP Diagram baru (`supportFiles/SOP_DIAGRAMS.md`).

## [v1.0.0] — 2026-04-25

### Added
- **Auto-Update System**: Integrasi AI Auditor di `gemini.md` untuk cek update otomatis via URL GitHub.
- **Workflow /update-infra**: Sistem pencangkokan (grafting) infrastruktur mandiri (Git-less friendly).
- **Comprehensive Audit**: Workflow `/check-sync` untuk deteksi inkonsistensi parameter riset antara Markdown vs Word.
- **Enhanced Global Brain**: Skrip `update_global_brain.py` dengan deteksi folder dinamis (`Path.home`).
- **New Utility Scripts**: `apply_obsidian_colors.py`, `official_vault_export.py`, dan `audit_prose_sync.py`.

### Changed
- **Modular Skills**: Local Skill `graphify` dipindahkan ke `.agents/skills/graphify/` agar lebih portabel.
- **AI Audit Protocol**: Pengetatan aturan onboarding di `gemini.md` (mandatori `setup_docx_infra.ps1`).

### Fixed
- Menghapus referensi skrip usang `inject_docx_xml.py` dan beralih ke sistem `docx` Node.js yang lebih stabil.
- Memperbaiki path hardcoded agar 100% sterile untuk distribusi pengguna baru.

---

*"Build smarter, write faster, research deeper."*
