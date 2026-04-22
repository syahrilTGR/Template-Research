# 🗺️ Panduan Instalasi Graphifyy (GraphRAG) - OPSIONAL

Fitur ini memungkinkan AI untuk memetakan hubungan antar file dan konsep dalam draf Anda ke dalam Knowledge Graph (Visualisasi HTML + JSON). Versi yang kita gunakan adalah versi Python yang sangat kuat untuk ekstraksi AST dan GraphRAG.

> [!NOTE]
> Fitur ini bersifat **OPSIONAL**. Kita menggunakan library **`graphifyy`** (dengan dua huruf 'y').

## 🛠️ Prasyarat (Prerequisites)
1. **Python**: Pastikan Python sudah terinstal (Direkomendasikan menggunakan venv atau Conda).
2. **RTK (Rust Token Killer)**: Disarankan menggunakan prefix `rtk` untuk penghematan token.

## ⚙️ Langkah Instalasi
Pilih interpreter Python yang Anda gunakan untuk proyek ini dan instal library-nya:

```powershell
# Menggunakan PIP standar
pip install graphifyy

# Jika menggunakan Conda (misal env: thesis_venv)
conda run -n thesis_venv pip install graphifyy
```

## 🚀 Cara Penggunaan
Setelah terinstal, Anda bisa menjalankan perintah berikut:

1. **Inisialisasi**: `rtk graphify init .`
2. **Update Graph**: `rtk graphify update .`
3. **Visualisasi**: Buka folder `graphify-out/` dan jalankan `graph.html` di browser Anda.

## 🤖 Fitur Auto-Recovery
Skill agen saya di repositori ini memiliki fitur *auto-recovery*. Setiap kali Anda menjalankan perintah `/graphify`, saya akan mendeteksi apakah library `graphifyy` sudah terpasang. Jika belum, saya akan menawarkan instalasi otomatis ke environment aktif Anda.

---
> [!TIP]
> Menggunakan `rtk graphify` sangat disarankan untuk menjaga efisiensi penggunaan token selama sesi riset intensif.
