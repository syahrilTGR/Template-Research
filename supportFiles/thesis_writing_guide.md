# Panduan Gaya Penulisan Skripsi
## Berdasarkan Analisis 2 Skripsi Kating ([Your_Department], [Your_University])

> **Dibuat:** 2026-03-16
> **Sumber:** `example/[Example_Thesis_1].docx` dan `example/[Example_Thesis_2].docx`
> **Tujuan:** Menjadi referensi standar penulisan untuk skripsi [Your_Name] (Incremental Learning [Project_Name])

---

## 1. Statistik Perbandingan Bab 2

| Aspek | [Example_Author_1] (IoT + YOLO) | [Example_Author_2] (YOLO Comparison) | Target [Your_Name] |
|---|---|---|---|
| Jumlah subbab Bab 2 | 9 subbab | 17 subbab | ~15–20 subbab |
| Total paragraf body | 66 | 157 | ~100–130 |
| Rata-rata kata/paragraf | ~43 kata | ~54 kata | ~60–80 kata |
| Total estimasi kata Bab 2 | ~2.800 | ~8.400 | ~7.000–10.000 |
| Kedalaman teknis | Moderat (deskriptif) | Tinggi (komponen per komponen) | Tinggi (formula + komponen) |

**Kesimpulan:** Bab 2 skripsi [Your_Department] **yang lebih kuat ([Example_Author_2]) memiliki ~8.000+ kata** dengan kedalaman teknis tinggi. Target [Your_Name] sebaiknya minimal **7.000 kata** untuk Bab 2 yang komprehensif.

---

## 2. Struktur Organisasi Bab 2

### Pola Umum (Kedua Kating):
```
BAB II TINJAUAN PUSTAKA
  2.1 Penelitian Terdahulu
      └── Tabel penelitian + 2-3 paragraf sintesis
  2.2 Kajian Teori
      2.2.1 [Konsep Umum — Konteks / Masalah]
      2.2.2 [Teknologi Inti 1]
      2.2.3 [Teknologi Inti 2]
      2.2.4 [dst...]
```

### Observasi Penting:
- **Penelitian Terdahulu** selalu ditulis dalam **tabel + narasi sintesis**, bukan bullet point.
- Narasi sintesis di akhir Penelitian Terdahulu **wajib ada**: 2-3 paragraf yang menjelaskan gap dan positioning penelitian ini.
- **Kajian Teori** dimulai dari konsep yang paling umum/dasar, lalu makin spesifik ke teknologi yang digunakan.

---

## 3. Gaya Penulisan Paragraf

### Karakteristik Kating [Example_Author_1]:
- Paragraf lebih pendek (~43 kata), langsung ke poin.
- Setiap konsep dijelaskan dalam 1-2 paragraf untuk konsep sederhana.
- Kutipan diletakkan di akhir kalimat: `...seperti penggunaan MQTT [41].`
- **Pola:** Definisi → Penjelasan cara kerja → Relevansi untuk sistem

### Karakteristik Kating [Example_Author_2]:
- Paragraf lebih panjang (~54 kata), struktur lebih elaborate.
- Arsitektur teknis (backbone, neck, head) dijelaskan **komponen per komponen** dengan sub-kalimat.
- Menggunakan bahasa transisi: *"Proses dimulai dari... dilanjutkan dengan... komponen kunci..."*
- **Pola:** Definisi → Latar historis/konteks → Komponen teknis → Cara kerja detail → Keunggulan → Relevansi

### Rekomendasi untuk [Your_Name]:
- Ikuti **pola [Example_Author_2]** (lebih dalam) karena topik IL/prototype lebih kompleks secara matematis.
- Target: **60–80 kata per paragraf** (setara [Example_Author_2] atau lebih).
- Gunakan rumus matematika inline (seperti handoff_v3.md sudah lakukan): $\mu_c$, $\tau$, dll.
- Transisi antar paragraf harus jelas: "Sementara itu, ...", "Lebih lanjut, ...", "Berdasarkan hal tersebut, ..."

---

## 4. Konvensi Kutipan

### Format yang Digunakan Kating:
- `[angka]` ditempatkan di **akhir kalimat**, sebelum titik: `...dengan akurasi 97% [10].`
- Multi-sitasi ditulis berurutan: `[10][11][12]` (tidak ada koma)
- Nama penulis **tidak selalu disebutkan** di teks — biasanya hanya nomor.
- Referensi ke tabel/gambar: `Tabel 2.1 menunjukkan bahwa...` atau `ditunjukkan pada Gambar 2.5`

### Rekomendasi untuk [Your_Name] (skripsi berbahasa Indonesia):
- Jika ada nama penulis yang perlu disebutkan: *"Han et al. [8] menunjukkan bahwa..."*
- Jika sitasi saja sudah cukup: *"...menggunakan Gaussian KDE [8]."*
- **Catatan:** Jika skripsi akhir dalam bahasa Indonesia, prose yang ada di `handoff_v3.md` perlu diterjemahkan ke BI yang formal.

---

## 5. Kedalaman Penjelasan Per Subbab

### Pedoman Jumlah Paragraf Per Subbab:
| Tipe Subbab | Kating | Rekomendasi [Your_Name] |
|---|---|---|
| Subbab konsep dasar (misal: Sampah, IoT) | 1–2 paragraf | 2–3 paragraf |
| Subbab teknologi utama (misal: YOLOv8, MobileNet) | 3–5 paragraf | 4–6 paragraf |
| Subbab metode kunci (misal: IL, HITL) | 4–6 paragraf | 5–7 paragraf |
| Penelitian Terdahulu | Tabel + 3–4 paragraf | Tabel + 3–4 paragraf |

### Skripsi [Example_Author_2] — Template Subbab YOLOv9 (sangat detail):
1. **Pengantar umum arsitektur** (~80 kata): Apa itu, apa inovasinya dibanding versi sebelumnya.
2. **Deskripsi Backbone** (~150 kata): Fungsi, komponen (RepNCSPELAN4, ADown, SPPELAN), cara kerja.
3. **Deskripsi Neck/Head** (~150 kata): Cara fusi fitur, loss function.
4. **Paragraph penutup** (~50 kata): Relevansi ke penelitian ini.

**[Your_Name] adaptasi:** Untuk Subbab 2.2.2 (IL), seharusnya ada:
1. Definisi IL dan jenis-jenisnya
2. Catastrophic Forgetting — mekanisme dan dampaknya
3. Prototype-based approach — matematika (formula µ)
4. Gaussian KDE untuk prototype enhancement
5. Frozen encoder strategy
6. Paragraph penutup — koneksi ke [Project_Name]

---

## 6. Hal yang TIDAK Ada di Skripsi Kating (tapi ada di rencana [Your_Name]):

- **Formula matematika** (Σ, µ, KDE) — ini **nilai plus** untuk skripsi [Your_Name], tidak lazim di kating.
- **Sitasi IEEE format** (kating pakai BI style yang lebih longgar).
- **Bahasa Inggris** — kating keduanya menulis dalam **Bahasa Indonesia**.

> [!IMPORTANT]
> **[Your_Name] perlu memutuskan:** Apakah skripsi akhir ditulis dalam Bahasa Indonesia atau Inggris?
> Jika Bahasa Indonesia → Prosa di `handoff_v3.md` perlu diterjemahkan.
> Jika Bahasa Inggris → Sudah sesuai, lanjutkan.

---

## 7. Checklist Kualitas Per Subbab

Sebelum finalisasi setiap subbab, pastikan:
- [ ] Setidaknya **4 paragraf** untuk subbab teknologi inti
- [ ] Setiap paragraf minimal **50 kata**
- [ ] Ada **koneksi eksplisit** ke [Project_Name]/penelitian ini di paragraf terakhir setiap subbab
- [ ] Semua kutipan berformat `[angka]` dan ada di reference list
- [ ] Tidak ada kalimat satu baris / fragmen tanpa penjelasan
- [ ] Setiap konsep teknis (formula, arsitektur) dijelaskan dalam bahasa prosa, bukan hanya persamaan

---

## 8. Contoh Kalimat Transisi yang Dipakai Kating

| Fungsi | Contoh dari Kating |
|---|---|
| Menyebutkan penelitian sebelumnya | "Penelitian sebelumnya yang menggunakan YOLOv5... menunjukkan akurasi 86% [18]." |
| Menjelaskan gap | "Meskipun demikian, sistem tersebut masih terbatas dalam..." |
| Memperkenalkan solusi penelitian ini | "Berdasarkan masalah yang telah diuraikan, penelitian ini mengusulkan..." |
| Menjelaskan komponen | "Proses dimulai dari... dilanjutkan dengan... komponen kunci meliputi..." |
| Relevansi ke penelitian | "Hal ini sangat relevan karena sistem [Project_Name] juga memerlukan..." |

---

## 9. Aturan Tanda Baca Teknis (Technical Punctuation Rules)

Untuk menjaga konsistensi format akademik dan menghindari penulisan bergaya "AI-isms" yang tidak alami, ikuti aturan penggunaan tanda baca berikut:

### **Penggunaan Titik Dua (Colon `:`)**
- **Dilarang keras** menggunakan tanda titik dua (`:`) atau titik koma (`;`) di tengah-tengah paragraf prosa yang mengalir untuk tujuan penjelasan, enumerasi inline, atau penghubung anak kalimat.
  - *Salah*: "Sistem ini memiliki tiga keunggulan utama: efisiensi daya, akurasi tinggi, dan pemulihan cepat."
  - *Benar*: "Sistem ini memiliki tiga keunggulan utama yang meliputi efisiensi daya, akurasi tinggi, dan pemulihan cepat." (Atau pecah menjadi kalimat terpisah).
- **Diperbolehkan** menggunakan titik dua (`:`) di akhir kalimat pengantar (*introductory sentence*) yang langsung mengarah pada **bulleted list**, **numbered list**, atau **persamaan matematika blok** (karena tidak berada di tengah-tengah paragraf prosa mengalir).
  - *Contoh Berorientasi List*: "Tahapan implementasi ini dibagi ke dalam enam fase utama pengembangan:"
  - *Contoh Berorientasi Rumus*: "Persamaan total kerugian $L_{total}$ didefinisikan sebagai:"


