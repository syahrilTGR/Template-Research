# 🚀 Panduan Update Infrastruktur (Semua Versi)

Dokumen ini berisi **prompt siap pakai** yang bisa Anda berikan ke agen AI Anda untuk melakukan pembaruan infrastruktur secara manual dari versi apapun ke versi terbaru.

Gunakan panduan ini jika: `scripts/update_infra.py` belum ada, sudah usang, atau gagal dijalankan otomatis.

---

## Prompt untuk Agen AI

*Copy-paste seluruh teks di bawah ini ke chat agen AI Anda:*

---

```
Tolong lakukan pembaruan infrastruktur repositori ini secara manual dari GitHub ke versi terbaru.

**LANGKAH-LANGKAH:**

1. Unduh arsip repositori terbaru dari GitHub:
   URL: https://github.com/syahrilTGR/Template-Research/archive/refs/heads/main.zip
   Simpan ke file sementara `template_update.zip` di root proyek.

2. Ekstrak isi ZIP tersebut ke folder sementara `.agents/temp_update/`.

3. Pindahkan folder hasil ekstraksi (`Template-Research-main`) ke `.agents/_bridge_update_/`.

4. Terapkan pembaruan dengan aturan berikut untuk SETIAP file di dalam `.agents/_bridge_update_/`:

   **[REPLACE] — Timpa langsung, file ini adalah engine/infrastruktur:**
   - Seluruh isi `.agents/skills/` (semua subfolder dan isinya)
   - Seluruh isi `.agents/workflows/`
   - Seluruh isi `.agents/plugins/`
   - Seluruh isi `.agents/rules/`
   - Seluruh isi `scripts/` (KECUALI file yang tidak ada di bridge — pertahankan)
   - `requirements.txt`
   - `CHANGELOG.md`
   - `GETTING_STARTED.md`
   - `HOW_TO_USE_ANTIGRAVITY.md`
   - `OPTIONAL_GRAPHIFY.md`
   - `CREDITS.md`
   - `update_prompt.md`

   **[SMART MERGE] — JANGAN timpa langsung, gabungkan dengan aman:**
   - `gemini.md`:
     Pertahankan seluruh blok `## 🎯 Project Identity` dan `## 💻 Environment & Technical Context` dari file LOKAL pengguna.
     Ambil semua bagian LAIN (protokol, instruksi AI, versi, dll.) dari file BARU (bridge).
     Caranya: Baca kedua file, ekstrak blok identitas dari lokal, sisipkan ke posisi yang sama di file baru, lalu tulis hasilnya.

   **[PERTAHANKAN] — JANGAN sentuh sama sekali, milik user:**
   - `supportFiles/handoff/` (seluruh draf tesis aktif)
   - `supportFiles/ACTION_PLAN.md` (hanya buat jika belum ada)
   - `supportFiles/decisions_log.md`
   - `supportFiles/open_questions.md`
   - `supportFiles/walkthrough.md`
   - `supportFiles/revision_progress_tracker.md`
   - `supportFiles/citations_map.json`
   - `supportFiles/ANTI_HALLUCINATION.md`
   - `supportFiles/extracted_pdfs/` (hasil ekstraksi PDF)
   - `references/` (semua PDF jurnal)
   - `dataset/`, `results/`, `models/`, `intelligence/` (data penelitian)
   - `.agents/backups/` (cadangan sebelumnya)

   **[BUAT JIKA BELUM ADA] — File konfigurasi opsional:**
   - `supportFiles/word_sync_config.json` (hanya buat jika belum ada)

5. Tampilkan isi bagian pertama dari `.agents/_bridge_update_/CHANGELOG.md` (entri versi terbaru saja) sebagai ringkasan "Apa yang baru?"

6. Hapus semua file sementara: `template_update.zip`, `.agents/temp_update/`, `.agents/_bridge_update_/`.

7. Laporkan ringkasan: berapa file yang di-replace, file apa yang di-merge, dan konfirmasi bahwa data penelitian saya aman tidak tersentuh.
```

---

> [!NOTE]
> Prompt di atas dirancang agar agen AI dapat memahami setiap keputusan pembaruan secara eksplisit, tanpa bergantung pada versi `scripts/update_infra.py` yang terpasang. Cocok digunakan saat melakukan pembaruan pertama kali (*fresh clone*) atau saat skrip otomatis gagal.
