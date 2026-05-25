# Changelog — Template Research 🚀

Semua perubahan penting pada infrastruktur riset ini akan dicatat di file ini.

## [v1.0.7] — 2026-05-25

### Added
- **Academic Literature Search Skills**: Menambahkan *skills* riset ilmiah global `literature-search-arxiv`, `literature-search-openalex`, dan `science_skills_common` secara lokal ke dalam repositori.
- **Advanced Support Guides**: Mengintegrasikan 5 dokumen pendukung generik berstandar tinggi ke folder `supportFiles/` (`thesis_writing_guide.md`, `UNIVERSAL_THESIS_AI_GUIDE.md`, `GRAPHRAG_GUIDE.md`, `DOCX_SYNC_GUIDE.md`, `FILE_INDEX.md`).
- **Venv-First Path Activation**: Menyelaraskan seluruh path eksekusi skrip sinkronisasi dan Word agar merujuk ke *virtual environment* terpusat `$HOME\thesis_venv` sesuai dengan alur kerja asli `setup_env.ps1`.

### Fixed
- **Universal Sanitization**: Melakukan pembersihan menyeluruh secara mandiri untuk menghapus data pribadi (Syahril, NIM, Kelas) dan spesifik proyek (EcoBin, MobileNet, YOLOv8) dari seluruh file yang baru disalin.

## [v1.0.6] — 2026-05-23

### Added
- **Local Ingestion of pptx & xlsx**: Memindahkan seluruh berkas *skill* global `pptx` dan `xlsx` ke direktori lokal `.agents/skills/` agar terintegrasi penuh ke dalam repositori riset portabel.
- **Dynamic Skill Junctioning SOP**: Pembersihan otomatis tanda pengenal pribadi serta pembuatan *Directory Junction* Windows (`/j`) untuk mengarahkan 11 berkas *skills* global ke versi lokal secara terintegrasi secara *real-time*.

### Fixed
- **Docx Validation Hotfix**: Injeksi parameter `encoding="utf-8"` saat pembacaan berkas XML di validator untuk mencegah kegagalan *decoding* `'charmap'` pada Windows default codepage.
- **Generic Docx Skill Sync**: Sinkronisasi penuh seluruh skrip pengaman Word (`pack.py`, `unpack.py`, `sync_check.py`, `extract_docx.py`) dalam bentuk generik ke repositori lokal.
- **Sterile Documentation Sync**: Mengintegrasikan `SKILL.md` generik baru yang bersih dari *path* pribadi dan tersemat dengan otomatisasi interpretasi virtual environment (*Dynamic Setup Protocol*).

## [v1.0.5] — 2026-05-23

### Added
- **Dynamic Setup Protocol**: Implementasi sistem deteksi environment virtual otomatis untuk Agent. Memungkinkan penyesuaian path Python secara lokal tanpa merusak standarisasi repositori publik.
- **Agent-Led Environment Configuration**: Instruksi baru yang mewajibkan Agent melakukan scanning (`.venv`, `.venv_ecobin`, dll) dan menawarkan opsi interpreter kepada user jika terdeteksi placeholder `[PYTHON_PATH_PLACEHOLDER]`.

### Changed
- **Universal Sanitization**: Pembersihan total informasi sensitif dan path hardcoded (e.g., nama user lokal, venv spesifik) dari skill `docx` untuk keamanan distribusi publik.
- **Docx Skill Synchronization**: Integrasi perbaikan kritis pada `ImageRun` (mandatory type extension) dan penanganan *File Lock* via *Shadow Packaging* (Word Desktop compatibility).

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
