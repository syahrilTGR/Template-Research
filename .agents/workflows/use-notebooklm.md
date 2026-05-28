---
description: Panduan kolaborasi hibrida dan terintegrasi MCP antara Antigravity (lokal) dan Google NotebookLM (cloud) untuk analisis riset tingkat lanjut.
---

# 🤖 Workflow: Google NotebookLM Integration (Hybrid & MCP Direct)

Workflow ini digunakan untuk memperluas pencarian literatur menggunakan fitur pencarian mendalam cloud dari Google NotebookLM, lalu menyelaraskan hasilnya dengan basis pengetahuan lokal Anda.

Pilih salah satu metode penggunaan di bawah ini berdasarkan kebutuhan riset Anda:

---

## ⚡ Opsi A: Integrasi Langsung via Server MCP (Rekomendasi Instan)
Jika Anda sudah melakukan setup pada berkas [notebooklm_mcp_setup.md](file:///g:/Project/Template/supportFiles/notebooklm_mcp_setup.md), asisten dapat berinteraksi secara langsung dengan notebook cloud Anda dari chat ini.

### 🛠️ Langkah-Langkah:
1. **[AI ACTION] List & Identify**: Asisten akan mencari UUID notebook riset Anda menggunakan perkakas `notebook_list`.
2. **[USER ACTION] Konfirmasi Sasaran**: Tentukan notebook mana yang ingin dianalisis atau ditambahkan referensinya.
3. **[AI & USER ACTION] Direct Query / Ingestion**: 
   - Ajukan pertanyaan langsung lintas paper via `notebook_query`.
   - Tambahkan artikel/URL baru secara otomatis via `source_add`.

---

## 🔄 Opsi B: Alur Kerja Hibrida Manual (Untuk Deep Research Skala Besar)
Gunakan opsi ini jika Anda ingin merumuskan prompt pencarian eksternal yang kompleks dan memindahkan berkas PDF secara manual untuk menjaga keaslian file sumber:

### 🛠️ Langkah-Langkah:
1. **[AI ACTION] Analisis Kebutuhan**: Asisten mendeteksi celah (*gap*) riset Anda, lalu merumuskan **Prompt Deep Research** yang sangat tajam untuk Anda salin.
2. **[USER ACTION] Menjalankan Deep Research**: Salin prompt tersebut, buka Google NotebookLM Web, lalu jalankan pencarian mendalam.
3. **[USER ACTION] Ekspor & Download**:
   - Salin teks ringkasan sintesis yang dihasilkan dari obrolan cloud.
   - Unduh (*harvest*) seluruh file PDF sumber ilmiah yang direkomendasikan NotebookLM.
4. **[USER ACTION] Import Lokal**:
   - Pindahkan berkas PDF hasil unduhan ke dalam folder `references/`.
   - Tempelkan (*paste*) ringkasan sintesis sebagai berkas `.md` baru di folder `intelligence/catatan_notebooklm/`.
5. **[AI ACTION] Eksekusi & Integrasi**: Beri tahu asisten: *"Saya sudah memasukkan bahan dari NotebookLM."* Asisten akan otomatis melahap data baru, mengekstrak metrik numerik (`/extract-metrics`), dan merajutnya ke dalam `handoff` serta Wiki.
