# Changelog — Template Research 🚀

Semua perubahan penting pada infrastruktur riset ini akan dicatat di file ini.

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
