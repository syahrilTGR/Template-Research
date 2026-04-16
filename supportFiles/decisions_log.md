# Decisions Log

Catat setiap keputusan teknis atau arsitektur utama di sini agar terekam rekam jejak risetnya.

| Tanggal | Masalah / Isu | Keputusan / Solusi | Alasan Teknis |
|---|---|---|---|
| Tanggal | Masalah / Isu | Keputusan / Solusi | Alasan Teknis |
|---|---|---|---|
| 2026-04-16 | Redundansi folder drafting (`thesis_bureau`) | Migrasi ke alur **Handoff-Centric** | Memusatkan seluruh draf di `supportFiles/handoff.md` untuk efisiensi konteks AI. |
| 2026-04-16 | Privasi & Portabilitas Gaya Word | Implementasi **Sterile Templates** | Mengekstrak hanya 'DNA' penomoran tanpa isi teks asli pengguna. Menjamin file asli bisa dihapus dengan aman. |
| 2026-04-16 | Onboarding untuk Pengguna Baru | Skrip **`setup_env.ps1`** otomatis | Memudahkan teman-teman pengguna melakukan setup Python + venv dengan satu klik. |
| 2026-04-16 | Keterbatasan Editing Word | Integrasi **Advanced Docx Surgery** | Menyediakan akses langsung ke `unpack`/`pack` XML untuk perbaikan format manual yang kompleks. |
