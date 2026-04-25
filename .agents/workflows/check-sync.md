---
description: Audit sinkronisasi antara draf Markdown (Ground Truth) dengan dokumen Word/Master MD
---

# Workflow: Check Sync Audit

Workflow ini mendeteksi apakah data teknis (Parameter) dan konten tulisan (Prose) di dokumen produksi (Word/Master MD) sudah sesuai dengan draf terbaru di folder `handoff`.

**Script Utama**: `scripts/audit_prose_sync.py`

---

## Step 1: Jalankan Audit Proyek

Lakukan pengecekan konsistensi parameter (misal: jumlah kelas, nilai threshold) dan kemiripan teks (similarity) antarseksi.

// turbo
```powershell
rtk powershell -c "python scripts/audit_prose_sync.py"
```

---

## Step 2: Analisis Laporan

Baca hasil audit yang baru saja dibuat untuk melihat bagian mana yang *Out-of-Sync*.

```powershell
rtk powershell -c "Get-Content 'supportFiles/SYNC_AUDIT_REPORT.md'"
```

---

## Step 3: Tindakan Perbaikan (Surgery)

Jika ditemukan ketidaksinkronan, pilih salah satu tindakan:

### Opsi A: Update Manual ke Word
1. Buka file Word.
2. Update parameter atau teks manual berdasarkan temuan di laporan.

### Opsi B: Re-generate via Skill Docx
Gunakan skill `docx` untuk men-generate ulang bab yang bermasalah menggunakan draf terbaru dari handoff sebagai input.

---

## Step 4: Finalisasi

Setelah diperbaiki, jalankan Step 1 kembali untuk memastikan status menjadi **✅ SYNCED**.
