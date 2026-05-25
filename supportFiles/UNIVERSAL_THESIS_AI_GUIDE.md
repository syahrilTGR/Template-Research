# 🎓 Panduan Kolaborasi AI untuk Segala Topik Skripsi
> **Template**: Universal Thesis-AI Framework
> **Tujuan**: Memastikan AI (Agen Coding/Riset) memiliki konteks penuh terhadap riset Anda, apa pun jurusannya.

Panduan ini berisi cara mengatur file dan sistem agar AI bisa bekerja sebagai "Partner Peneliti" yang tidak pernah lupa konteks.

---

## 📂 1. Struktur File "Otak Luar" AI
Agar AI tidak "asbun" (asal bunyi), berikan dia file teks (`.md`) yang berisi aturan dan data riset Anda. Simpan di folder khusus, misalnya `supportFiles/`.

| Nama File (Contoh) | Fungsi Utama | Isi yang Disarankan |
| :--- | :--- | :--- |
| **`MASTER_CONTEXT.md`** | **Pintu Masuk Utama** | Judul skripsi, latar belakang singkat, metodologi yang dipakai, dan aturan penulisan. |
| **`PROGRESS_TRACKER.md`** | **Buku Harian Proyek** | Daftar bab (Bab 1-5). Tandai mana yang sudah selesai, mana yang sedang dikerjakan (In-Progress). |
| **`DECISION_LOG.md`** | **Catatan Keputusan** | Kenapa Anda memilih teori A? Apa hasil observasi B? Biar AI paham alur pemikiran Anda. |
| **`DEFINITIONS.md`** | **Kamus Istilah/Rumus** | Kumpulan istilah teknis, rumus, atau landasan teori utama agar AI menggunakan istilah yang sama. |
| **`LITERATURE_BASE.md`** | **Ringkasan Pustaka** | Ringkasan jurnal-jurnal utama yang Anda sitasi. Ini bahan baku buat AI menyusun Bab 2. |
| **`CHAT_SUMMARY.md`** | **Memori Sesi** | Ringkasan tiap kali Anda selesai chat. Gunakan untuk memulai sesi chat di hari berikutnya. |

---

## 🛠️ 2. Alat Penggerak (AI Infrastructure)
AI yang Anda gunakan (seperti Antigravity/Gemini) bekerja lebih baik jika dihubungkan dengan alat ini:

### A. MCP (Model Context Protocol)
*   **Fungsi**: Sebagai "tangan" AI untuk memegang file Anda.
*   **Contoh**: `antigravity-nb` (untuk mengelola Jupyter Notebook/Data), atau akses langsung ke folder Windows Anda (filesystem).

### B. Skills & Workflows (Automasi Perintah)
Anda bisa membuat "Skill" atau "Workflow" (perintah `/slash`) khusus, misalnya:
*   `/cek-sitasi`: AI mengecek format APA/IEEE pada tulisan Anda.
*   `/buat-subbab`: AI membuat draf sub-bab berdasarkan data di `LITERATURE_BASE.md`.

---

## 🧠 3. Knowledge Items (AI's Long-term Memory)
Setiap kali Anda membahas hal rumit, suruh AI menyimpannya sebagai **Knowledge Item (KI)**.
*   **Fungsi**: AI akan mengingat poin-poin penting tersebut secara permanen tanpa perlu Anda jelaskan ulang di masa depan.

---

## 💡 Tips Rahasia Kolaborasi AI yang Efektif
1.  **Berikan Konteks Dulu, Kerjakan Kemudian**: Sebelum minta AI menulis, katakan: *"Tolong baca file `MASTER_CONTEXT.md` dan `LITERATURE_BASE.md` agar paham arah penelitianku."*
2.  **Gunakan File `Handoff`**: Di akhir setiap sesi, katakan: *"Update file `PROGRESS_TRACKER.md` mengenai apa yang kita capai hari ini."*
3.  **Cross-Check Teori**: Jangan percaya 100% pada AI untuk teori yang sangat spesifik. Selalu sediakan teks asli jurnal di dalam folder `supportFiles/extracted_texts/` agar AI merujuk ke sana.
4.  **Tanyakan 'Saran Berikutnya'**: Sering-seringlah bertanya: *"Berdasarkan status saat ini di `PROGRESS_TRACKER.md`, apa langkah logis berikutnya yang harus aku lakukan?"*

---

## 🔧 4. Kompensasi Mode AI Flash (Flash/Fast Models)
Jika asisten AI terasa mulai "pelupa" atau sering berhalusinasi (asbun), terapkan kompensasi berikut:

*   **`PROMPT_TEMPLATE.md`**: Buat file yang berisi instruksi wajib setiap awal sesi (mewajibkan AI membaca Master Context).
*   **`ANTI_HALLUCINATION.md`**: Buat daftar putih (whitelist) jurnal yang valid. Larang AI mengutip di luar daftar tersebut.
*   **`CHAT_SUMMARY.md` Template**: Simpulan harus mencatat **"Kalimat terakhir yang ditulis"** agar alur penulisan tetap menyambung sempurna.
*   **Batasan Eksplisit**: Masukkan seksi "⛔ BATASAN" di Master Context untuk mengontrol gaya penulisan secara ketat.

---
*Dibuat oleh Assistant untuk mempermudah riset lintas disiplin ilmu.*
