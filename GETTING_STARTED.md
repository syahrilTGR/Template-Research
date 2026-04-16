# 🚀 PANDUAN MULAI CEPAT (GET STARTED)

Selamat! Kamu baru saja meng-clone **Universal AI Research Template**. Ikuti langkah-langkah di bawah ini untuk mengubah repositori ini menjadi asisten riset pribadimu dalam waktu kurang dari 5 menit.

---

## 🛠️ Langkah 1: Persiapan Environment
Pilih salah satu cara untuk menyiapkan "nyawa" pendukung asisten AI di komputer Anda:

### Opsi A: One-Click Setup (Sangat Direkomendasikan - Windows)
Buka PowerShell di folder ini dan jalankan skrip otomatis:
```powershell
# Skrip ini akan cek Python, buat venv di folder Home, dan instal dependensi otomatis
.\scripts\setup_env.ps1
```
Setelah selesai, aktifkan environment dengan menjalankan path yang muncul di layar (biasanya `~\thesis_venv\Scripts\Activate.ps1`).

### Opsi B: Setup Manual (Linux/macOS atau Jaga-jaga)
1. Buat venv di folder Home: `python -m venv ~/thesis_venv`
2. Aktivasi: `~/thesis_venv/Scripts/Activate.ps1` (Windows) atau `source ~/thesis_venv/bin/activate` (UNIX)
3. Instal library: `pip install -r requirements.txt`

> [!NOTE]
> Fitur penulisan Word profesional di repositori ini berbasis **Python Standalone**. Anda juga bisa melakukan "bedah" Word secara manual menggunakan `scripts/docx_surgery.py`.

---

## ⚡ Langkah 2: Sesi Pertama (Audit & Bootstrap)
Pastikan AI siap bekerja dengan prosedur yang benar:

1.  Buka chat asisten AI kamu.
2.  **Ketik Prompt:** *"Halo, saya ingin mulai menggunakan Universal Research Template. Tolong lakukan audit wajib terhadap file `gemini.md` dan `ACTION_PLAN.md` saya sebelum kita mulai bekerja."*

> [!IMPORTANT]
> **AI Auditor Aktif**: Jika **Phase 0: Infrastructure** belum terceklis `[x]`, AI akan menolak tugas akademik dan meminta Anda melengkapi profil terlebih dahulu.

---

## 📚 Langkah 3: Beri AI "Makan" (Knowledge Injection)
Agar AI pintar dan tidak berhalusinasi, beri dia bahan bacaan:

1.  **Draf Lama:** Taruh file `.docx` proposal lama/contoh di folder `example/`.
    *   **Ketik Prompt:** *"Pelajari draf lama saya di folder example agar kamu bisa meniru gaya penulisan akademik yang ada."*
2.  **Jurnal/Paper:** Taruh PDF referensi di folder `papers/`.
    *   **Ketik Prompt:** *"Tolong ekstrak semua PDF di folder papers dan masukkan ke daftar referensi valid di `ANTI_HALLUCINATION.md`. Setelah itu, tolong ganti nama (rename) semua file tersebut menjadi format `PENULIS_TAHUN_JUDUL.pdf` agar rapi."*
3.  **Tambah Paper Baru:** (Kapan pun Anda punya referensi baru nanti)
    *   **Ketik Prompt:** *"Saya baru saja menambah paper baru ke folder papers. Tolong ulangi proses ekstraksi dan update daftar referensi saya."*

---

## ✍️ Langkah 4: Mulai Menulis & Riset
Sekarang AI sudah kenal gayamu dan punya referensi. Pilih tugasmu:

- **Menulis Subbab:** 
    *   **Ketik Prompt:** *"/write-subsection Bab 1 bagian Latar Belakang berdasarkan paper [Author_Year] yang sudah kita ekstrak."*
- **Analisis Paper:** 
    *   **Ketik Prompt:** *"/extract-metrics untuk membandingkan metode dari paper yang ada di folder papers."*

---

## 🔄 Langkah 5: Sinkronisasi & Simpan Ingatan
Jangan biarkan kerja kerasmu hilang:

1.  **Sinkron dari Word:** (Setelah Anda mengedit file di Word OneDrive)
    *   **Ketik Prompt:** *"Saya baru saja melakukan update di file Word OneDrive saya, tolong sinkronkan draf tersebut kembali ke Markdown (Handoff)."*
2.  **Update Handoff Akhir Sesi:**
    *   **Ketik Prompt:** *"/update-handoff. Rangkum progres kita hari ini dan catat apa saja yang perlu kita kerjakan besok."*

---

### 📌 Catatan Penting:
- **`supportFiles/handoff.md`**: Ini adalah "Otak" sekaligus muara tunggal seluruh tulisanmu. AI akan selalu membaca draf di sini agar konteks tetap terjaga.
- **`papers/`**: Tempat kamu menaruh PDF literatur.

*Selamat meneliti, semoga skripsimu cepat selesai!* 🚀✨
