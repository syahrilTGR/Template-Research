---

## 🗺️ Peta Mental: Memahami Struktur Folder
Agar tidak tersesat, bayangkan folder di sini seperti sebuah kantor riset:
- **`references/`**: Lemari arsip (Tempat kamu menaruh semua jurnal PDF).
- **`supportFiles/handoff/`**: Meja tulis (Tempat draf bab 1, 2, dll dikerjakan).
- **`intelligence/`**: Otak proyek (Wiki Obsidian yang mencatat semua hubungan teori).
- **`.agents/`**: Tim asisten (Instruksi dan "otak" bagi asisten AI Antigravity).
- **`scripts/`**: Alat bantu (Robot pembersih, mesin ekstraksi, dan pengaudit tulisan).

---

## ⚙️ Langkah 0: Konfigurasi IDE Marketplace

To switch the Google Antigravity IDE extension marketplace from Open VSX to the official VS Code Marketplace, you must configure two specific URLs in your settings:

- **Marketplace Item URL**: `https://marketplace.visualstudio.com/items`
- **Marketplace Gallery URL**: `https://marketplace.visualstudio.com/_apis/public/gallery`

### Setup Instructions:
1. Open your Antigravity IDE.
2. Open Settings using `Ctrl + ,` (or `Cmd + ,` on Mac).
3. Navigate to **Editor settings**.
4. Locate the marketplace fields and input the URLs provided above.
5. Restart the IDE completely for the changes to take effect.

---

## 🛠️ Langkah 1: Persiapan Environment
Pilih salah satu cara untuk menyiapkan "nyawa" pendukung asisten AI di komputer Anda:

### Opsi A: One-Click Setup (Sangat Direkomendasikan - Windows)
Buka **Terminal Antigravity** di folder ini dan jalankan perintah sakti ini:
```powershell
# Jalankan skrip ini untuk cek Python, buat venv, dan instal dependensi otomatis
powershell -ExecutionPolicy Bypass -File .\scripts\setup_env.ps1
```

### 🆘 Pertolongan Pertama (Troubleshooting)
| Masalah | Solusi |
|---|---|
| **Error: Permission Denied** | Jalankan `Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process` di PowerShell-mu, lalu coba lagi. |
| **Python not found** | Pastikan Python sudah terinstal (download di python.org) dan centang **"Add Python to PATH"** saat instalasi. |
| **Scripts cannot be loaded** | Ini biasanya karena Windows memblokir skrip. Gunakan perintah **Opsi A** di atas (pakai Bypass). |

### 🔗 Mendaftarkan Venv ke Ekstensi Python
Setelah setup selesai, pastikan ekstensi Python di IDE Anda bisa mendeteksi *virtual environment* tersebut secara otomatis:
1. Buka Settings IDE menggunakan `Ctrl + ,` (atau `Cmd + ,` di Mac).
2. Cari pengaturan: **`Python: Venv Path`** di kolom pencarian.
3. Masukkan folder **Home** Anda ke dalam isian tersebut, contoh:
   - **Windows**: `C:\Users\NamaUserAnda`
   - **Mac/Linux**: `/Users/NamaUserAnda` (atau `~`)
4. Setelah itu, tekan `Ctrl + Shift + P` (atau `Cmd + Shift + P`), ketik **Python: Select Interpreter**, dan pilih environment riset Anda (misalnya `thesis_venv`).

---

## ⚡ Langkah 2: Sesi Pertama (Audit & Bootstrap)
Buka chat asisten AI kamu (Antigravity) dan pastikan dia tahu aturan mainnya:

1.  **Audit Awal:** Ketik *"Halo, tolong lakukan audit wajib terhadap file `gemini.md` dan `ACTION_PLAN.md` saya."*
2.  **Hasil Audit:** Jika AI bilang "Audit Bersih", tandanya kamu siap tempur. Jika tidak, ikuti instruksi perbaikan dari AI.

---

## 📚 Langkah 3: Ingest Literatur (Masukan Bahan Baku)
AI hanya akan sepintar bahan baku yang kamu berikan.

1.  **Taruh PDF:** Masukkan semua jurnal referensimu ke folder `references/`.
2.  **Ekstraksi:** Ketik prompt: *"/extract-metrics untuk membedah semua PDF di folder references."*
    - **Hasilnya:** AI akan membuatkan ringkasan di folder `intelligence/ringkasan_paper/` dan tabel metrik otomatis.

---

## ✍️ Langkah 4: Siklus Kerja (Ingest -> Process -> Write)
Selalu gunakan alur ini agar tulisanmu berkualitas tinggi:

1.  **Ingest:** Pastikan referensi sudah diekstrak (Langkah 3).
2.  **Process:** Minta AI melakukan brainstorming atau audit draf lama.
3.  **Write:** Gunakan perintah `/write-subsection` untuk menulis draf baru.
    *   *Tips:* Selalu sebutkan nama paper dalam kurung siku, misal: *"Tolong tulis Latar Belakang berdasarkan paper [Author_Year]."*

---

## 🔄 Langkah 5: Sinkronisasi & Penutup Sesi
Agar progresmu aman dan bisa dilanjutkan di HP atau komputer lain (via cloud):

1.  **Sync Word:** Gunakan `scripts/sync_word.ps1` untuk menarik editan dari Word OneDrive ke repositori ini.
2.  **Handoff:** Di akhir setiap sesi, **WAJIB** ketik `/update-handoff`. 
    - Ini akan mengisi file `supportFiles/handoff/00_metadata.md` dengan status terbaru agar besok AI tidak lupa apa yang sudah dikerjakan.

---

## 🚀 Common Research Workflows

Setelah instalasi selesai, berikut adalah beberapa tugas umum yang bisa Anda lakukan:

### 1. Menambah & Mengekstrak Referensi Baru
Jika Anda memiliki paper jurnal baru (.pdf) yang ingin dimasukkan ke dalam riset:
1. Simpan file PDF di folder `references/`.
2. Berikan prompt ini ke Antigravity:
   > *"Saya baru saja menambahkan paper baru di folder references. Tolong jalankan /extract-metrics untuk mengekstrak metrik kinerjanya, buatkan ringkasannya di folder intelligence, dan perbarui tabel komparasi literatur saya."*

### 2. Membuat Diagram / Flowchart (Draw.io)
Pembuatan diagram arsitektur atau alur riset harus menggunakan aplikasi open-source agar metadatanya tetap tersimpan di repositori Anda.
- Silakan baca panduan lengkap pembuatannya di **`supportFiles/SOP_DIAGRAMS.md`**.
- Platform pilihan: [app.diagrams.net](https://app.diagrams.net)

### 3. Sinkronisasi Tulisan (Word <-> Markdown)
Gunakan `/context-summary` di awal setiap sesi untuk memastikan asisten memiliki konteks draf terbaru Anda yang ada di OneDrive/Word.

---

## 🛠️ Maintenance & Updates
Repositori ini dirancang untuk terus berkembang. Agar Anda selalu mendapatkan fitur terbaru (seperti ekstraktor PDF yang lebih cerdas atau skill baru), lakukan update secara berkala.

### Cara Melakukan Update:
Cukup berikan perintah sederhana ini kepada Antigravity:
> *"Tolong cek apakah ada update infrastruktur terbaru di repo pusat. Jika ada, jalankan /update-infra sekarang."*

### Apa yang Terjadi Saat Update?
1. **Pencangkokan Aman**: Asisten akan menarik kode terbaru tanpa menyentuh draf tulisan, pdf referensi, atau identitas proyek Anda.
2. **Self-Healing**: Sistem akan mendeteksi file yang rusak atau hilang dan memperbaikinya secara otomatis.
3. **Konfigurasi Ulang**: Environment virtual Anda akan diperbarui jika ada library baru yang dibutuhkan.

---

## 🆘 Butuh Bantuan?
Jika Anda bingung atau terjadi error, tanyakan kepada asisten:
- *"Bagaimana cara kerja workflow X?"*
- *"Tolong audit repositori saya, apakah sudah sesuai standar?"*

*"Build smarter, write faster, research deeper."* 🚀
