# Session Start Prompt Template

Gunakan template ini saat memulai atau mereset sesi AI agar asisten kembali ke konteks proyek.

```markdown
Hai, jalankan `/context-summary`. 

**Audit Wajib Sebelum Mulai:**
1. Cek `ACTION_PLAN.md`: Apakah Phase 0 sudah [x]? 
2. Cek `gemini.md` & `SKILL.md`: Apakah masih ada placeholder [TBD]?

Jangan lakukan tugas akademik sebelum status audit di atas 'CLEAN'.
```

## 🆕 Sesi Pertama (Bootstrap)
Gunakan ini saat baru pertama kali melakukan clone repositori:
```markdown
Halo! Saya baru saja melakukan clone repositori template ini. Tolong jalankan protokol onboarding/bootstrap sesuai instruksi di `gemini.md` dan `custom_project_skill/SKILL.md`. Bantu saya mengisi profil riset saya.
```

---

## 🛠️ Command Cheat Sheet (Siap Copy-Paste)

### 1. Knowledge Injection (Beri AI "Makan")
*   **Belajar Gaya Bahasa:** `"Pelajari draf lama saya di folder example agar kamu bisa meniru gaya penulisan akademik saya."`
*   **Ekstrak & Rapikan Paper:** `"Tolong ekstrak semua PDF di folder papers dan masukkan ke daftar referensi valid di supportFiles/ANTI_HALLUCINATION.md. Setelah itu, tolong ganti nama (rename) semua file tersebut menjadi format PENULIS_TAHUN_JUDUL.pdf agar rapi."`
*   **Tambah Paper Baru:** `"Saya baru saja menambah paper baru ke folder papers. Tolong ulangi proses ekstraksi dan update daftar referensi saya."`

### 2. Drafting & Riset (Mulailah Menulis)
*   **Tulis Subbab:** `"/write-subsection Bab 1 bagian Latar Belakang berdasarkan paper [Author_Year] yang sudah kita ekstrak."`
*   **Tabel Komparasi:** `"/extract-metrics untuk membandingkan metode dari paper-paper yang ada di folder papers."`
*   **Analisis Cepat:** `"Tolong bantu ringkas temuan utama dari paper [Author_Year] dan hubungkan dengan metodologi penelitian saya."`

### 3. Synchronization (Simpan & Sinkron)
*   **Tarik dari Word:** `"Saya baru saja melakukan update di file Word OneDrive saya, tolong sinkronkan draf tersebut kembali ke Markdown (Handoff)."`
*   **Update Progres:** `"/context-summary. Berikan rangkuman status draf saya saat ini."`
*   **Tutup Sesi:** `"/update-handoff. Rangkum progres kita hari ini dan catat apa saja yang perlu kita kerjakan besok."`
