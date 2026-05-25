# 🗺️ Definitive Guide: Knowledge Graph & GraphRAG ([Project_Name])

Dokumen ini adalah panduan operasional untuk mengelola "Otak Digital" skripsimu. Sistem ini menghubungkan **Kode (Python)**, **Naskah (Obsidian)**, dan **Literatur (PDF)** ke dalam satu graf pengetahuan yang saling terhubung.

---

## 🏗️ Arsitektur Sistem

Pengetahuanmu tersebar di tiga lokasi utama yang disatukan oleh **Graphify**:
1.  **Local Repo (`[Your_Project_Path]`)**: Berisi kode produksi, notebook eksperimen, dan dokumen pendukung (`supportFiles`).
2.  **Global Brain Center (`[Path_To_Your_Global_Brain_Center]`)**: "Source of Truth" naskah skripsi dalam format Obsidian MD.
3.  **Graphify-Out**: Output GraphRAG (JSON & HTML) yang dibaca oleh asisten AI untuk menjawab pertanyaanmu.

---

## 🔄 Cara Menjalankan Sinkronisasi (Update Otak)

Setiap kali ada perubahan pada kode atau kamu selesai menulis sub-bab baru di Obsidian, jalankan perintah ini di terminal:

```powershell
# Jalankan sinkronisasi semantik global
$HOME\thesis_venv\Scripts\python.exe [Path_To_Your_Global_Brain_Center]\scripts\sync_project.py
```

**Apa yang terjadi saat sinkronisasi?**
1.  **AST Extraction**: Mengekstrak struktur fungsi dan kelas dari Python.
2.  **Support Scanning**: Membaca `GLOSSARY.md` dan `decisions_log.md` untuk mencari keyword teknis.
3.  **Semantic Bridging**: Menghubungkan alur asinkron (MQTT) antara Edge dan Server.
4.  **Community Detection**: Mengelompokkan kode dan naskah ke dalam klaster topik (misal: klaster *Incremental Learning*).

---

## 🛠️ Kemampuan Utama (Apa yang Bisa Dilakukan?)

### 1. Architectural Tracing (Audit Trail)
Kamu bisa melacak bagaimana sebuah teori di naskah diimplementasikan di kode.
*   **Contoh**: *"Poin 3.2.1 di naskah saya diwakili oleh fungsi apa di kode?"*
*   **Hasil**: AI akan mencari kaitan antara teks metodologi di naskah dengan fungsi di `scripts/`.

### 2. Semantic Bridging (Lintas Sistem)
Sistem ini memahami alur data yang tidak terbaca oleh parser kode biasa (seperti MQTT).
*   **Jalur**: `feedback_trigger` (Edge) ➔ `mqtt_sync` ➔ `update_proto` (Server).

### 3. Glossary Authority
Setiap istilah teknis (AIA, BWT, KDE) memiliki "Kebenaran Tunggal" di `GLOSSARY.md`. AI tidak akan berhalusinasi mengarang definisi karena sudah terikat pada dokumen ini.

---

## 💡 Best Practices (Tips Agar Graf Tetap Pintar)

1.  **Gunakan Tag @thesis**: Di dalam komentar kode Python, gunakan tag `# @thesis:il` atau `# @thesis:hitl` untuk memberi tahu asisten bahwa baris tersebut krusial untuk skripsi.
2.  **Wikilinks di Obsidian**: Gunakan format `[[GLOSSARY#AIA]]` di dalam naskah Obsidian. Script sinkronisasi akan mendeteksi link ini dan memperkuat hubungan di graf.
3.  **Naming Consistency**: Pastikan istilah di `supportFiles/GLOSSARY.md` sama persis dengan yang kamu gunakan di naskah Word/Obsidian.

---

## 🔍 Alat Bantu (MCP Tools)

Jika asisten AI terlihat "lupa", kamu bisa memicu pencarian manual dengan:
*   `query_graph`: Mencari konteks luas tentang sebuah topik.
*   `get_node`: Melihat detail spesifik satu fungsi atau satu pasal di naskah.
*   `shortest_path`: Mencari "benang merah" antara dua konsep yang terasa jauh.

---

> [!TIP]
> **Visualisasi Visual**: Kamu bisa melihat bentuk fisik otak skripsimu dengan membuka file [graph.html](file:///[Path_To_Your_Global_Brain_Center]/graphify-out/graph.html) di browser.

*Dokumen ini diperbarui secara otomatis oleh Antigravity Assistant.*
