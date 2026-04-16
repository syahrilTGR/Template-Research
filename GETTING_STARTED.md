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
Buka chat asisten AI kamu dan tempelkan kalimat "sakti" dari **[PROMPT_TEMPLATE.md](file:///f:/ML_Project/Template/supportFiles/PROMPT_TEMPLATE.md)** bagian Sesi Pertama.

> [!IMPORTANT]
> **AI Auditor Aktif**: Segera setelah Anda menyapa, AI akan melakukan **Audit Wajib** terhadap file `gemini.md` dan `supportFiles/ACTION_PLAN.md`. 
> Jika **Phase 0: Infrastructure** belum terceklis `[x]`, AI akan menolak tugas akademik dan meminta Anda melengkapi profil terlebih dahulu.

**Aksi Kamu Agar Lolos Audit:** 
- Isi identitas, hardware, dan teknologi di **`gemini.md`**. (Cukup edit file ini saja untuk semua profil proyek).
- Jalankan setup environment (Langkah 1).
- Pastikan semua poin di **Phase 0** pada `supportFiles/ACTION_PLAN.md` sudah Anda centang `[x]`.

---

## 📚 Langkah 3: Beri AI "Makan" (Knowledge Injection)
Agar AI pintar dan tidak berhalusinasi, beri dia bahan bacaan:

1.  **Draf Lama:** Jika kamu sudah punya draf proposal/skripsi lama, taruh filenya di folder `example/`. AI akan otomatis menawarkan diri untuk mengekstrak gaya bahasamu.
2.  **Jurnal/Paper:** Taruh PDF referensi di folder `papers/`.
3.  **Jalankan Ekstraksi:** Katakan pada AI: *"Tolong ekstrak semua PDF di folder papers dan proposal di folder example."*

---

## ✍️ Langkah 4: Mulai Menulis & Riset
Sekarang AI sudah kenal gayamu dan punya referensi. Kamu bisa mulai bekerja:

- **Menulis Bab:** `/write-subsection` (AI akan otomatis menyimpan draf langsung ke `supportFiles/handoff.md`).
- **Analisis Paper:** `/extract-metrics` (Untuk membuat tabel perbandingan metode dari paper).
- **Diskusi Bebas:** Tanyakan apa saja tentang metodologimu.

---

## 🔄 Langkah 5: Sinkronisasi & Simpan Ingatan
Jangan biarkan kerja kerasmu hilang:

1.  **Sinkron ke Word:** Jalankan skrip `scripts/sync_word.ps1` (setelah memasukkan path OneDrive) untuk memindahkan tulisan dari Word kembali ke Markdown agar bisa dipelajari AI.
2.  **Update Handoff:** Di setiap akhir sesi, ketik `/update-handoff`. Ini krusial agar AI tidak "amnesia" saat kamu kembali besok.

---

### 📌 Catatan Penting:
- **`supportFiles/handoff.md`**: Ini adalah "Otak" sekaligus muara tunggal seluruh tulisanmu. AI akan selalu membaca draf di sini agar konteks tetap terjaga.
- **`papers/`**: Tempat kamu menaruh PDF literatur.

*Selamat meneliti, semoga skripsimu cepat selesai!* 🚀✨
