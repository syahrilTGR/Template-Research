## 🔍 File Properties (Inline Index Block)
- **File Path:** `supportFiles/notebooklm_mcp_setup.md`
- **Purpose:** Technical guide for setup, authentication, troubleshooting, and tool usage of the `notebooklm-mcp` integration.
- **Functions & Roles:** Provides step-by-step instructions for developers, setup prerequisites, direct venv and path activation, troubleshooting common errors, and usage examples of the MCP server tools.
- **Upstream Dependencies:** None
- **Downstream Dependencies:** `supportFiles/FILE_INDEX.md`, `.agents/workflows/use-notebooklm.md`

---

# 📘 Panduan Teknis Setup & Penggunaan Google NotebookLM MCP

Panduan ini mendokumentasikan secara lengkap langkah setup, autentikasi, penyelesaian masalah (troubleshooting), serta cara penggunaan server **`notebooklm-mcp`** pada sistem operasi Windows. Dokumentasi ini disusun agar integrasi asisten lokal dengan ekosistem Google NotebookLM berjalan optimal untuk aktivitas riset tingkat lanjut.

---

## 1. Pendahuluan & Prerequisites

**`notebooklm-mcp`** adalah jembatan programatis berbasis Model Context Protocol (MCP) yang menghubungkan asisten kecerdasan buatan (seperti Antigravity) ke Google NotebookLM secara langsung. Melalui integrasi ini, asisten dapat mengakses dokumen, membaca ringkasan, membuat catatan, dan menanyakan informasi di dalam notebook Anda tanpa perlu membuka antarmuka web secara manual.

Untuk memastikan kelancaran operasional, pastikan detail arsitektur lingkungan pengembangan Anda memenuhi spesifikasi dasar berikut:

### ⚙️ Konfigurasi Lingkungan Sistem

| Parameter Lingkungan | Deskripsi / Lokasi Sistem |
| :--- | :--- |
| **Sistem Operasi** | Windows (PowerShell 5.1 atau PowerShell 7+) |
| **Virtual Environment Utama** | `%USERPROFILE%\.venv_ecobin` (Python 3.12.x) |
| **Versi Paket CLI** | `notebooklm-mcp-cli` versi `0.6.13` (terinstall di dalam venv aktif) |
| **Executable CLI Utama (`nlm`)** | `%USERPROFILE%\.venv_ecobin\Scripts\nlm.exe` |
| **Konfigurasi MCP IDE** | `%USERPROFILE%\.gemini\config\mcp_config.json` |

> [!NOTE]
> `%USERPROFILE%` adalah variabel lingkungan Windows yang biasanya merujuk pada `C:\Users\<username>`. Pastikan Anda menyesuaikan `<username>` dengan nama pengguna aktif di komputer Anda.

---

## 2. Panduan Autentikasi (Langkah demi Langkah)

Proses autentikasi awal membutuhkan login interaktif menggunakan akun Google Anda yang memiliki akses ke layanan Google NotebookLM. Layanan ini akan membuka jendela browser eksternal untuk verifikasi akun dan menyimpan token autentikasi secara lokal di komputer Anda.

Terdapat dua metode eksekusi untuk menjalankan perintah login:

### ⚡ Metode A: Aktivasi Virtual Environment Terlebih Dahulu
Metode ini direkomendasikan jika Anda bekerja secara interaktif langsung dari dalam terminal PowerShell untuk memastikan semua variabel lingkungan mengarah ke virtual environment yang tepat.

1. Buka terminal PowerShell.
2. Jalankan skrip aktivasi virtual environment:
   ```powershell
   & "$env:USERPROFILE\.venv_ecobin\Scripts\Activate.ps1"
   ```
3. Eksekusi perintah login:
   ```powershell
   nlm login
   ```
4. Jendela Chrome akan otomatis terbuka. Lakukan login menggunakan akun Google Anda, kemudian tunggu hingga proses di terminal menyatakan autentikasi selesai.

### 🎯 Metode B: Eksekusi Jalur Langsung (Direct Path)
Metode ini sangat berguna jika Anda ingin menjalankan login secara instan tanpa harus mengubah status shell atau sesi terminal aktif Anda saat ini.

1. Buka terminal PowerShell.
2. Panggil executable `nlm` secara langsung dari virtual environment menggunakan operator call (`&`):
   ```powershell
   & "$env:USERPROFILE\.venv_ecobin\Scripts\nlm.exe" login
   ```
3. Selesaikan proses login interaktif pada jendela browser yang terbuka.

---

## 3. Troubleshooting Penting (Critical Fixes)

Berikut adalah ringkasan masalah kritis yang umum ditemui beserta solusi praktis untuk menyelesaikannya:

### 🚨 Masalah 1: Mismatch Jalur Python (Executable Not Found)
* **Gejala:** Muncul pesan kesalahan yang menyatakan bahwa interpreter python tidak ditemukan pada jalur lama seperti `[drive-letter]:\path\to\old\python.exe` (misalnya pada jalur miniconda atau instalasi Python lama yang sudah tidak aktif).
* **Penyebab:** Eksekusi perintah `nlm` secara global mendeteksi konfigurasi interpreter python lama dari variabel lingkungan Windows (PATH) atau instalasi global yang usang.
* **Solusi Praktis:**
  Hindari memanggil perintah `nlm` secara global tanpa spesifikasi lingkungan. Anda wajib memastikan salah satu dari dua tindakan berikut dilakukan sebelum memanggil CLI:
  1. Jalankan skrip aktivasi venv `.venv_ecobin` terlebih dahulu sebelum memanggil perintah `nlm` (Metode A).
  2. Panggil CLI menggunakan jalur absolut virtual environment yang aktif secara langsung (Metode B):
     ```powershell
     & "$env:USERPROFILE\.venv_ecobin\Scripts\nlm.exe" [perintah]
     ```

### 🚨 Masalah 2: Error Instan "Authentication Expired" saat Menjalankan `nlm login`
* **Gejala:** Jendela autentikasi langsung tertutup atau langsung menampilkan pesan kedaluwarsa sesaat setelah browser terbuka, sehingga gagal memperbarui kredensial.
* **Penyebab:** Tumpukan cookie atau sesi usang yang tersimpan dalam folder cache lokal profil autentikasi Chrome lokal mengalami konflik atau sudah tidak valid.
* **Solusi Praktis:**
  Jalankan perintah dengan parameter pembersih cache untuk membersihkan seluruh data autentikasi Chrome lokal lama dan memaksa pembukaan jendela autentikasi yang benar-benar bersih:
  * **Melalui shell aktif venv:**
    ```powershell
    nlm login --clear --force
    ```
  * **Melalui jalur absolut langsung:**
    ```powershell
    & "$env:USERPROFILE\.venv_ecobin\Scripts\nlm.exe" login --clear --force
    ```

---

## 4. Fitur Utama & Cara Penggunaan MCP

Setelah proses autentikasi berhasil, asisten kecerdasan buatan dapat memanggil berbagai perkakas (tools) MCP secara langsung untuk berinteraksi dengan Google NotebookLM Anda. 

Berikut adalah empat fungsionalitas utama yang sering digunakan beserta contoh parameter pemanggilannya:

### 📁 1. `notebook_list`
Mendapatkan daftar seluruh notebook aktif Anda beserta identifier uniknya (UUID). Identifier ini sangat penting karena digunakan sebagai referensi untuk seluruh perkakas lainnya.
* **Tujuan:** Menemukan `notebook_id` yang ingin digunakan.
* **Parameter:** Tidak memerlukan parameter tambahan.

### 📝 2. `notebook_describe`
Menghasilkan ringkasan deskriptif dari seluruh dokumen yang ada di dalam notebook tertentu.
* **Tujuan:** Mengetahui topik utama dan cakupan konten tanpa harus membaca satu per satu dokumen.
* **Parameter Utama:**
  * `notebook_id` (string UUID notebook)

### 💬 3. `notebook_query`
Mengajukan kueri atau pertanyaan berbasis seluruh dokumen di dalam notebook. Kueri ini berjalan langsung pada model NotebookLM dan tidak mengotori riwayat obrolan (chat history) web utama Anda.
* **Tujuan:** Melakukan analisis literatur lintas dokumen secara cerdas.
* **Parameter Utama:**
  * `notebook_id` (string UUID notebook)
  * `query` (pertanyaan atau instruksi analisis riset Anda)
* **Contoh Argumen:**
  ```json
  {
    "notebook_id": "123e4567-e89b-12d3-a456-426614174000",
    "query": "Jelaskan metode komparasi algoritma YOLOv8 dan MobileNetV3 berdasarkan dokumen yang diunggah."
  }
  ```

### ➕ 4. `source_add`
Menambahkan sumber referensi baru ke dalam notebook aktif. Sumber dapat berupa URL situs, teks mentah, Google Drive, atau file dokumen lokal.
* **Tujuan:** Melakukan perluasan basis pengetahuan notebook secara dinamis.
* **Parameter Utama:**
  * `notebook_id` (string UUID notebook)
  * `source_type` (pilihan: `url`, `text`, `drive`, atau `file`)
  * `file_path` / `url` / `text` (menyesuaikan dengan tipe sumber yang dipilih)
* **Contoh Argumen:**
  ```json
  {
    "notebook_id": "123e4567-e89b-12d3-a456-426614174000",
    "source_type": "url",
    "url": "https://arxiv.org/abs/2301.00001"
  }
  ```

---

> [!TIP]
> Jalankan perintah `nlm --help` atau hubungi asisten Anda jika membutuhkan bantuan mengenai parameter tingkat lanjut dari perkakas `notebooklm-mcp` lainnya.
