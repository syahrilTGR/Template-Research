# SOP Pembuatan & Pengelolaan Diagram (Draw.io)

Dalam penulisan skripsi akademik, diagram alir (*flowchart*), arsitektur model, dan blok sistem harus terlihat profesional, seragam, dan mudah diedit di kemudian hari.

Oleh karena itu, proyek riset ini menggunakan standar **Draw.io (diagrams.net)**.

---

## 🛠️ Langkah-Langkah Pembuatan Diagram

Agar diagram Anda tersimpan dengan aman bersama draf skripsi (dan tidak hilang ketika komputer berganti), ikuti standar alur kerja berikut:

### 1. Meminta AI Mendesain Konsep Diagram
Jika Anda bingung struktur diagramnya, Anda bisa meminta asisten Antigravity.
- **Prompt:** *"Tolong buatkan struktur flowchart untuk metodologi pengumpulan data saya. Buatkan dalam bentuk list agar saya mudah memindahkannya ke Draw.io."*

### 2. Membuat File Diagram Baru
Alih-alih menggunakan aplikasi berbayar, gunakan platform web gratis standar industri:
1. Buka browser Anda dan kunjungi **[app.diagrams.net](https://app.diagrams.net/)**.
2. Jika ditanya tempat penyimpanan (*save location*), pilih **"Device"**.
3. Pilih **"Create New Diagram"**.
4. Beri nama file yang deskriptif, contoh: `arsitektur_model.drawio` atau `alur_pengumpulan_data.drawio`.
5. Mulai gambar sesuai konsep yang Anda buat.

### 3. Menyimpan File ke Repositori
Agar diagram tidak terpisah dari repositori riset Anda:
1. Di dalam web Draw.io, klik `File` -> `Save As...` -> `Device`.
2. Simpan file berakhiran `.drawio` ini ke dalam folder `supportFiles/` milik template riset Anda.
   *(Jika Anda memiliki banyak diagram, Anda boleh membuat folder baru: `supportFiles/diagrams/` dan menyimpannya di sana).*

### 4. Membuka Kembali & Mengedit Diagram Lama
Jika suatu hari dosen pembimbing meminta revisi pada *flowchart* Anda:

#### Opsi A: Melalui Web (app.diagrams.net)
1. Buka kembali **[app.diagrams.net](https://app.diagrams.net/)**.
2. Pilih opsi **"Open Existing Diagram"** (atau klik `File` -> `Open From` -> `Device`).
3. Navigasikan ke repositori lokal Anda (`supportFiles/diagrams/`).
4. Pilih file `.drawio` Anda.

#### Opsi B: Metode Salin XML (Extras)
Jika Anda ingin mengedit secara manual melalui kode atau dari sumber lain:
1. Buka file `.drawio` Anda di text editor dan salin konten XML-nya.
2. Di web app.diagrams.net, pergi ke menu **Extras** -> **Edit Diagram**.
3. Paste konten XML Anda di sana dan klik **OK**.

#### Opsi C: VS Code Extension (Direkomendasikan)
Untuk pengalaman mengedit langsung di dalam folder proyek, pastikan ekstensi berikut terinstall di VS Code Anda:
- **ID Ekstensi:** `eighthundreds.vscode-drawio`
- Dengan ekstensi ini, Anda cukup klik file `.drawio` di folder proyek dan editor grafis akan langsung terbuka di dalam VS Code.

---

## 💡 Tips & Standar Estetika Akademik

- **Konsistensi Font:** Sebisa mungkin gunakan font seperti *Times New Roman* atau *Arial* (ukuran 10-12) agar seragam dengan laporan Word (`.docx`).
- **Ekspor Gambar Resolusi Tinggi:** Setelah diagram selesai, JANGAN discreenshot! Gunakan fitur `File` -> `Export As` -> `PNG...`.
  - Pastikan opsi **Zoom** diatur ke **300%** atau **400%** agar gambar tidak pecah (*pixelated*) saat dimasukkan ke draf Word.
  - Centang opsi *Transparent Background* hanya jika memang dibutuhkan.
- **Arah Panah:** Pastikan panah yang menggambarkan proses memiliki arah (ujung mata panah) yang jelas dan konsisten.
