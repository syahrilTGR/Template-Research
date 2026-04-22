# Skill: Graphify Knowledge Mapping

Skill untuk memetakan arsitektur riset, hubungan antarkomponen koding, dan draf tesis ke dalam Knowledge Graph terintegrasi (GraphRAG).

## 🛡️ Self-Healing & Guardrails

1. **Auto-Dependency Check**: Setiap kali user memanggil `/graphify`, agen WAJIB melakukan pengecekan library:
   - Cek apakah `graphifyy` (double 'y') terpasang di interpreter yang digunakan.
   - Jika hilang, tawarkan: *"Saya mendeteksi `graphifyy` belum terpasang. Ingin saya pasang sekarang ke environment Anda?"*
2. **Context Integrity**: Pastikan perintah dijalankan dari root proyek agar folder `graphify-out/` tercipta di lokasi yang benar.

## 🛠️ Execution Commands

- **Update Graph**: `rtk graphify update .` (Gunakan setelah modifikasi besar pada kode atau draf).
- **Audit Knowledge**: `rtk graphify audit` (Untuk mendeteksi konsep-konsep yang terisolasi/orphan nodes).

## 🤖 Interaction Protocol

AI bertindak sebagai pengelola basis pengetahuan:
- Saat user bertanya *"Bagaimana hubungan komponen A dan B?"*, AI akan membaca `graphify-out/GRAPH_REPORT.md` atau query via MCP Graphify (jika aktif).
- AI akan menyarankan update graph secara proaktif jika mendeteksi banyak file baru yang belum dipetakan.

Ketik: *"Gunakan /graphify untuk memetakan progres riset saya hari ini."*
