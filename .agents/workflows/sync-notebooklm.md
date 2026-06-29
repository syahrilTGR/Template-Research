---
description: Workflow wajib untuk menjaga keselarasan referensi antara folder lokal dan Primary Notebook di NotebookLM.
---

# 🔄 Workflow: NotebookLM Bi-directional Reference Sync

Workflow ini memandu asisten untuk membandingkan isi folder lokal `references/` dengan sumber-sumber (sources) yang sudah terdaftar di Primary Notebook Anda (di Google NotebookLM).

> **Pemicu (Trigger):** Otomatis dipicu ketika ada file PDF baru ditambahkan ke `references/`, atau dipanggil secara manual menggunakan perintah `/sync-notebooklm`.

---

## 📋 Langkah-Langkah Eksekusi (Untuk Asisten AI)

### 1. 🔍 [AI ACTION] Identifikasi Konteks
1. Baca **Primary Notebook ID** dari bagian *Project Identity* di `gemini.md`.
2. Lakukan `list_dir` pada folder `references/` untuk mendapatkan daftar file PDF lokal beserta ukuran dan tanggal modifikasinya.
3. Gunakan *tool* `notebook_get` (atau `notebook_describe` tergantung ketersediaan di MCP) dengan target ID tersebut untuk mengambil detail metadata notebook, termasuk daftar *sources* yang saat ini ada di cloud.

### 2. ⚖️ [AI ACTION] Komparasi Dua Arah (*Diffing*)
Lakukan pencocokan (mencari irisan) antara daftar PDF lokal dan daftar sumber di NotebookLM berdasarkan nama file/judul referensi. 
Pisahkan hasilnya ke dalam dua daftar:
* **Missing in Cloud (Lokal -> Cloud):** File ada di lokal tapi tidak ada di NotebookLM.
* **Missing in Local (Cloud -> Lokal):** File ada di NotebookLM tapi tidak ada di folder `references/`.

### 3. 📤 [AI & USER ACTION] Sinkronisasi Lokal ke Cloud
Untuk setiap file yang masuk kategori **Missing in Cloud**:
1. Beri tahu pengguna daftar file yang akan diunggah.
2. Gunakan *tool* `source_add` (atau alat unggah MCP lain yang relevan) secara otomatis untuk mengunggah berkas-berkas PDF tersebut ke Primary Notebook.

### 4. 📥 [USER ACTION] Sinkronisasi Cloud ke Lokal
Untuk setiap file yang masuk kategori **Missing in Local**:
1. Karena asisten mungkin tidak bisa men-download PDF mentah secara langsung dari NotebookLM, buatlah daftar tabel (File Name, URL/Source) yang jelas.
2. Instruksikan pengguna untuk mencari file aslinya dan meletakkannya kembali ke dalam folder `references/` agar integritas data kutipan (Citation Guard) lokal tetap terjaga.

### 5. ✅ [AI ACTION] Laporan Final
Setelah sinkronisasi selesai, centang `[x] 0.10 Initial Bi-directional Reference Sync` di `supportFiles/ACTION_PLAN.md` jika ini adalah eksekusi orientasi pertama. Buatkan ringkasan singkat dari proses sinkronisasi ini.
