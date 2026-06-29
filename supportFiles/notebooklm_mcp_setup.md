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
| **Virtual Environment Utama** | `$HOME\thesis_venv` (Python 3.12.x, opsional untuk kebutuhan lain) |
| **Versi Paket CLI** | `notebooklm-mcp-cli` versi `0.7.7` atau terbaru (via `uv tool`) |
| **Executable CLI Utama (`nlm`)** | `%USERPROFILE%\.local\bin\nlm.exe` |
| **Konfigurasi MCP IDE** | `%USERPROFILE%\.gemini\config\mcp_config.json` |

> [!NOTE]
> `%USERPROFILE%` adalah variabel lingkungan Windows yang biasanya merujuk pada `C:\Users\<username>`. Pastikan Anda menyesuaikan `<username>` dengan nama pengguna aktif di komputer Anda.

---

## 2. Opsi Instalasi Paket CLI

Sebelum masuk ke tahap autentikasi, paket CLI `notebooklm-mcp-cli` versi `0.6.13` harus sudah terinstall di dalam virtual environment (`thesis_venv`). Terdapat dua metode untuk menyelesaikannya:

### 🤖 Opsi A: Instalasi Otomatis via Asisten AI (Agentic Setup)
Metode ini adalah cara tercepat dan termudah. Anda cukup menyalin perintah/prompt di bawah ini dan mengirimkannya ke obrolan asisten AI (seperti Antigravity) untuk mengotomatiskan seluruh proses instalasi serta konfigurasi `mcp_config.json`.

> **Salin Prompt Ini ke Chat Asisten:**
> ```text
> Hai Antigravity! Tolong bantu saya menyiapkan integrasi Google NotebookLM MCP secara otomatis. Silakan lakukan:
> 1. Verifikasi dan instal paket CLI 'notebooklm-mcp-cli' secara global menggunakan perintah `uv tool install notebooklm-mcp-cli`.
> 2. Bantu tambahkan konfigurasi server 'notebooklm-mcp' secara otomatis pada berkas '%USERPROFILE%\.gemini\config\mcp_config.json' menggunakan command `uvx` dengan args `["--from", "notebooklm-mcp-cli", "notebooklm-mcp"]`.
> ```

---

### 💻 Opsi B: Instalasi Manual (Manual Setup)
Jika Anda memilih untuk mengelolanya sendiri via terminal PowerShell, ikuti langkah berikut:

1. Buka terminal PowerShell (tidak perlu mengaktifkan virtual environment karena kita menggunakan `uv`).
2. Jalankan perintah instalasi paket CLI secara global menggunakan `uv`:
   ```powershell
   uv tool install notebooklm-mcp-cli
   ```
3. Verifikasi instalasi dengan mengecek versi CLI yang terpasang:
   ```powershell
   nlm --version
   ```
   *(Output yang diharapkan: `0.7.7` atau yang lebih baru)*

---

## 3. Panduan Autentikasi (Langkah demi Langkah)

Proses autentikasi awal membutuhkan login interaktif menggunakan akun Google Anda yang memiliki akses ke layanan Google NotebookLM. Layanan ini akan membuka jendela browser eksternal untuk verifikasi akun dan menyimpan token autentikasi secara lokal di komputer Anda.

Terdapat dua metode eksekusi untuk menjalankan perintah login:

### ⚡ Metode A: Eksekusi via Command Line (Global)
Karena kita menggunakan `uv tool`, perintah `nlm` sudah tersedia secara global di PowerShell Anda.

1. Buka terminal PowerShell.
2. Eksekusi perintah login:
   ```powershell
   nlm login
   ```
3. Jendela Chrome akan otomatis terbuka. Lakukan login menggunakan akun Google Anda, kemudian tunggu hingga proses di terminal menyatakan autentikasi selesai.

### 🎯 Metode B: Eksekusi Jalur Langsung (Direct Path)
Jika terminal Anda belum mendeteksi `nlm` di *Path*, Anda bisa memanggil *executable*-nya secara langsung dari direktori instalasi `uv`:

1. Buka terminal PowerShell.
2. Panggil executable `nlm` secara langsung menggunakan operator call (`&`):
   ```powershell
   & "$env:USERPROFILE\.local\bin\nlm.exe" login
   ```
3. Selesaikan proses login interaktif pada jendela browser yang terbuka.

---

## 4. Konfigurasi Server MCP di IDE (mcp_config.json)

Agar asisten AI di IDE Anda (seperti VS Code, Cursor, atau editor berkemampuan MCP lainnya) dapat menggunakan perkakas Google NotebookLM secara langsung, Anda wajib mendaftarkan server `notebooklm` ke dalam berkas konfigurasi MCP IDE Anda (`mcp_config.json`).

### 📝 Cara Menambahkan Konfigurasi:

1. Buka berkas konfigurasi MCP IDE Anda yang berlokasi di:
   `%USERPROFILE%\.gemini\config\mcp_config.json`
2. Tambahkan entri baru `"notebooklm-mcp"` di dalam objek `"mcpServers"`. 
3. Berikut adalah contoh isi konfigurasi JSON yang benar:

```json
{
  "mcpServers": {
    "notebooklm-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "notebooklm-mcp-cli",
        "notebooklm-mcp"
      ]
    }
  }
}
```
> - Setelah menyimpan berkas `mcp_config.json`, lakukan **Restart** or **Reload Window** pada IDE Anda untuk memuat ulang server MCP.

---

## 5. Troubleshooting Penting (Critical Fixes)

Berikut adalah ringkasan masalah kritis yang umum ditemui beserta solusi praktis untuk menyelesaikannya:

### 🚨 Masalah 1: Mismatch Jalur Python (Executable Not Found)
* **Gejala:** Muncul pesan kesalahan yang menyatakan bahwa interpreter python tidak ditemukan pada jalur lama seperti `[drive-letter]:\path\to\old\python.exe` (misalnya pada jalur miniconda atau instalasi Python lama yang sudah tidak aktif).
* **Penyebab:** Eksekusi perintah `nlm` secara global mendeteksi konfigurasi interpreter python lama dari variabel lingkungan Windows (PATH) atau instalasi global yang usang.
* **Solusi Praktis:**
  Hindari memanggil perintah `nlm` secara global tanpa spesifikasi lingkungan. Anda wajib memastikan salah satu dari dua tindakan berikut dilakukan sebelum memanggil CLI:
  1. Jalankan skrip aktivasi venv `thesis_venv` terlebih dahulu sebelum memanggil perintah `nlm` (Metode A).
  2. Panggil CLI menggunakan jalur absolut virtual environment yang aktif secara langsung (Metode B):
     ```powershell
     & "$env:USERPROFILE\thesis_venv\Scripts\nlm.exe" [perintah]
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
    & "$env:USERPROFILE\thesis_venv\Scripts\nlm.exe" login --clear --force
    ```

---

## 6. Fitur Utama & Cara Penggunaan MCP

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

## 💡 Panduan Cepat: Contoh Interaksi Langsung dengan Asisten AI

Untuk membantu Anda langsung mulai menggunakan fitur ini tanpa memikirkan parameter JSON teknis, Anda dapat memberikan perintah dalam bahasa manusia biasa kepada asisten AI Anda. Asisten akan otomatis memetakan perintah Anda ke perkakas MCP yang sesuai.

Berikut adalah lembar sontekan (*cheat sheet*) perintah obrolan yang dapat Anda gunakan:

| Aktivitas Riset | Contoh Kalimat Obrolan yang Dapat Anda Gunakan | Perkakas MCP yang Bekerja |
| :--- | :--- | :--- |
| **Menampilkan Daftar Notebook** | *"Tolong tampilkan daftar notebook riset yang ada di Google NotebookLM saya."* | `notebook_list` |
| **Melihat Dokumen & Ringkasan** | *"Tolong buat ringkasan dokumen untuk notebook ID <UUID_Notebook>."* | `notebook_describe` |
| **Analisis & Kueri Cerdas** | *"Tanyakan ke notebook ID <UUID_Notebook> mengenai apa kesimpulan paper riset YOLOv8 di dalamnya."* | `notebook_query` |
| **Menambah Jurnal Baru (URL)** | *"Tolong masukkan referensi URL https://arxiv.org/pdf/2301.00001 ke dalam notebook ID <UUID_Notebook>."* | `source_add` (url) |
| **Menambah Teks Catatan** | *"Tolong tambahkan teks kesimpulan rapat riset ini ke dalam notebook ID <UUID_Notebook>."* | `source_add` (text) |

> [!TIP]
> - **Anda tidak perlu menghafal UUID notebook!** Jalankan perintah *tampilkan daftar notebook* terlebih dahulu, lalu selanjutnya Anda bisa merujuk notebook tersebut dengan namanya (misalnya: *"Tanyakan ke notebook Skripsi YOLOv8 saya mengenai..."*) dan asisten AI akan otomatis memetakan serta mencari UUID-nya untuk Anda!
> - Seluruh kueri model berjalan langsung di cloud Google NotebookLM, sehingga sangat hemat memori lokal komputer Anda dan memanfaatkan kapabilitas pencarian literatur tingkat tinggi dari Google secara real-time.

---

> [!TIP]
> Jalankan perintah `nlm --help` atau hubungi asisten Anda jika membutuhkan bantuan mengenai parameter tingkat lanjut dari perkakas `notebooklm-mcp` lainnya.
