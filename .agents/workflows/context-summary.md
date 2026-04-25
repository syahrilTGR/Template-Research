---
description: Trigger automatically if the user says 'start a new session' or 'berikan ringkasan proyek'. Load full thesis context at start of every session.
---

# Workflow: Context Summary & Sync

Workflow ini memastikan asisten memiliki konteks penelitian terbaru, termasuk draf tulisan, referensi, dan file proposal fisik di OneDrive.

**Script Utama**: `scripts/sync_word.ps1` (Jika dikonfigurasi)

---

## Step 1: Inisialisasi Konteks (Handoff & Metadata)

Baca file-file berikut untuk memahami status riset terbaru:
1.  Read `supportFiles/handoff/00_metadata.md` (Timeline & Versi).
2.  Read `supportFiles/handoff/` (Draf aktif per bab).
3.  Read `supportFiles/pending_references.md` (Antrean referensi).

---

## Step 2 (Opsional): Sinkronisasi OneDrive

Jika Anda mengelola file `.docx` utama di OneDrive, jalankan sinkronisasi untuk menarik update manual yang Anda lakukan di Word ke folder proyek lokal.

// turbo
```powershell
# Jalankan script sinkronisasi (Pastikan path di dalam script sudah disesuaikan)
rtk powershell -c "scripts/sync_word.ps1"
```

---

## Step 3: Verifikasi Progres & Onboarding

Laporkan kembali ke user dengan ringkasan:
- **Status Sekarang**: ["Sedang menulis Bab 3.2", "Menunggu konversi 5 referensi", dll.]
- **Next Task**: ["Melanjutkan subbab 3.3", "Mengekstrak tabel dari Paper A", dll.]
- **Integrity Check**: ["Semua draf sinkron dengan Word", atau "Perlu audit sinkronisasi"]

---

## Step 4: Interaksi

Tanyakan kepada user:
*"Saya sudah siap. Ingin lanjut menulis subbab berikutnya, atau ada paper baru yang perlu kita bedah?"*
