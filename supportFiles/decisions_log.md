# Decisions Log

Catat setiap keputusan teknis atau arsitektur utama di sini agar terekam rekam jejak risetnya.

| Tanggal | Masalah / Isu | Keputusan / Solusi | Alasan Teknis |
|---|---|---|---|
| Tanggal | Masalah / Isu | Keputusan / Solusi | Alasan Teknis |
|---|---|---|---|
| 2026-04-16 | Redundansi folder drafting (`thesis_bureau`) | Migrasi ke alur **Handoff-Centric** | Memusatkan seluruh draf di `supportFiles/handoff/` untuk efisiensi konteks AI. |
| 2026-04-16 | Privasi & Portabilitas Gaya Word | Implementasi **Sterile Templates** | Mengekstrak hanya 'DNA' penomoran tanpa isi teks asli pengguna. Menjamin file asli bisa dihapus dengan aman. |
| 2026-04-16 | Onboarding & Identitas Tersebar | **Sentralisasi ke `gemini.md`** | Mengumpulkan identitas & profil teknologi di satu titik untuk memudahkan **AI Auditor** dan user. |
| 2026-04-16 | Sinkronisasi Referensi Word | Sitasi **`[Name_Year]`** | Memilih format tag nama untuk draf agar tetap stabil saat diolah oleh Mendeley/Zotero di Word. |
