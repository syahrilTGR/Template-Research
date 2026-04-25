# 📝 SOP: Sinkronisasi Skill `docx` & Optimasi Global NPM (Windows)

Dokumen ini adalah standar operasional untuk memastikan pembuatan dokumen Word (.docx) berjalan secara premium, stabil, dan efisien di lingkungan Windows.

---

## 1. Standar Akademik (Academic Standard)
Semua dokumen yang dihasilkan oleh AI Antigravity WAJIB mengikuti aturan styling berikut:

- **Font Utama**: *Times New Roman*
  - **Body**: 12pt (`size: 24` di docx-js)
  - **Heading**: 14pt (`size: 28` di docx-js)
- **Alignment**: *Justified* (`AlignmentType.JUSTIFIED`) untuk semua paragraf naratif.
- **Visual Callouts**: Gunakan komponen `noteBox` (tabel dengan border tebal kiri) untuk teori/rumus penting.
- **Data Iterasi**: Gunakan font monospace (*Courier New*) di dalam sel tabel agar angka desimal sejajar secara vertikal.

---

## 2. Optimasi Infrastruktur (Global NPM)
Untuk menghindari duplikasi `node_modules` di setiap folder proyek, gunakan instalasi global.

### A. Instalasi Library
Jalankan perintah berikut sekali di PowerShell:
```powershell
npm install -g docx
```

### B. Konfigurasi `NODE_PATH`
Agar Node.js dapat menemukan library global tersebut, daftarkan path-nya ke Environment Variable Windows:
```powershell
# Jalankan di PowerShell (Sesuaikan [Username] dengan nama user Windows Anda)
[System.Environment]::SetEnvironmentVariable("NODE_PATH", "C:\Users\[Username]\AppData\Roaming\npm\node_modules", "User")
```

---

## 3. Prosedur Refresh & Verifikasi
Setelah melakukan perubahan pada Environment Variable, sistem memerlukan "penyegaran":

1. **Restart PowerShell**: Tutup semua terminal aktif dan buka kembali.
2. **Restart Antigravity**: 
   - Keluar dari aplikasi Antigravity sepenuhnya (Quit dari Tray Area).
   - Jalankan kembali aplikasi agar memuat konteks `NODE_PATH` yang baru.
3. **Tes Koneksi**: Jalankan skrip pembangun dokumen. Jika berjalan tanpa error `MODULE_NOT_FOUND`, konfigurasi berhasil.

---

## 4. Alur Kerja Bedah Dokumen (Reverse Engineering)
Jika diminta memodifikasi dokumen yang sudah ada:
1. **Unpack**: Gunakan `scripts/office/unpack.py` untuk melihat XML asli.
2. **Analysis**: Pelajari `word/styles.xml` untuk mereplikasi format yang diinginkan user.
3. **Build/Edit**: Terapkan perubahan menggunakan skrip JS yang memanggil library global.

---
> [!IMPORTANT]
> SOP ini adalah rujukan utama bagi setiap Agen AI yang bekerja di repositori ini. Kegagalan mengikuti standar ini akan mengakibatkan dokumen terlihat tidak profesional (tidak akademik).
