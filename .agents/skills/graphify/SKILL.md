# Skill: Graphify (Project Local Orchestrator)

Skill ini adalah adaptasi lokal dari global graphify skill, yang didesain khusus untuk mengelola Knowledge Graph riset proyek ini secara komprehensif.

## 🚀 Orchestrator Utama
Lokasi: `.agents/skills/graphify/scripts/sync_brain_comprehensive.py`

### Kegunaan
Berbeda dengan standar `graphify update`, orkestrator ini melakukan:
1.  **Full Re-detection**: Memastikan file `.md` di `intelligence/` dan logs di `supportFiles/` selalu terdeteksi.
2.  **AST Update**: Melakukan ekstraksi struktur kode program.
3.  **Global Sink**: Otomatis memicu push data ke `Brain-Global-Center`.

## 🛠️ Cara Penggunaan
Selalu gunakan workflow `/sync-global-brain` untuk menjalankan sinkronisasi. Jangan menjalankan `graphify update` secara manual jika ingin menyertakan draf dokumen research.

---
**Author:** Antigravity AI (Research Bureau)
**Last Updated:** 2026-04-25 12:35
