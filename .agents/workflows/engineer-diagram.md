---
description: Panduan komprehensif mengaudit, merekayasa, dan mensinkronisasi arsitektur sistem (file .drawio) untuk logbook & praskripsi (Diadaptasi dari [Project_Name]).
---

# Workflow: Engineer Diagram Architecture (.drawio)

Workflow ini berisi alur kerja (pipeline) untuk merancang, memodifikasi, dan menyempurnakan file diagram arsitektur format XML (`.drawio`) secara sistematis. Alur ini diadaptasi dari praktik terbaik pada repositori **[Project_Name]**, memastikan diagram yang dihasilkan berstandar industri, tersinkronisasi dengan naskah akademis, bebas dari celah logika, dan siap dipertahankan dalam sidang praskripsi/tugas akhir.

---

## 🛠️ Prasyarat (Workspace & Skills)
Sebelum menjalankan workflow ini, pastikan hal-hal berikut sudah terdefinisi atau diinformasikan kepada AI:
1.  **File Sumber**: Lokasi file sumber `.drawio` yang ingin direkayasa.
2.  **File Referensi**: File *pipeline architecture* tambahan untuk menyelaraskan penamaan label komponen (agar penamaan sinkron antar diagram).
3.  **Konteks Algoritma Utama**: (Disarankan) Informasikan algoritma/formula spesifik yang digunakan sistem (misal: *Gaussian KDE*, atau threshold tertentu) agar alur diagram selaras dengan logika kode matematis.
4.  **Persona**: Aktifkan persona **B_Arsitek** untuk mengevaluasi arsitektur sistem terdistribusi, dan **D_Koordinator** untuk mengawal sinkronisasi data dengan naskah Bab/Laporan (persona tersedia di `.agents/plugins/research_bureau/personas/`).

---

## ⚙️ 5 Fase Rekayasa Diagram (Step-by-Step)

Untuk merekayasa diagram secara profesional, arahkan asisten AI untuk mengeksekusi 5 fase berikut secara sistematis:

### Fase 1: Audit & Penegasan Batasan Riset (Research Scoping)
*   **Tujuan:** Mempertegas batasan *novelty* (kebaruan) riset secara visual.
*   **Tindakan AI:**
    *   Membaca struktur XML `.drawio` untuk memahami letak pembagian wilayah komputasi (contoh: *Edge Device* vs *Cloud Server*).
    *   Membantu mendesain *Research Focus Scope Box* (area garis putus-putus) agar porsi algoritma yang menjadi fokus riset utama tersorot secara imbang.

### Fase 2: Pembenahan Alur Logis Server (Server Restructuring)
*   **Tujuan:** Menciptakan kaskade aliran pemrosesan data yang sistematis dan masuk akal secara teknis.
*   **Tindakan AI:**
    *   Menganalisis seluruh node komponen.
    *   Memodifikasi koordinat visual (`mxGeometry`) entitas secara logis. Memisahkan node yang bersifat pasif (seperti *Database*) dari node fungsional/aktif (seperti *Training Unit* atau *OTA Manager*) sehingga alur transmisi (misal: $\text{Broker} \rightarrow \text{Training Unit} \rightleftharpoons \text{Database} \rightarrow \text{Manager}$) terlihat mengalir secara natural.

### Fase 3: Pengisolasian Celah Logika Sidang (Loopholes Patching)
*   **Tujuan:** Mengantisipasi serangan penguji dalam "sidang bertahan" dengan mendeteksi titik putus/celah logika pada sistem.
*   **Tindakan AI:**
    *   Melakukan simulasi logika end-to-end pada koneksi diagram.
    *   Mendeteksi masalah potensial seperti: *feedback* aktuator yang terputus, alur pembaruan model (Model Update) yang tidak tersambung ke unit inference, eksekutor *trigger* yang ditempatkan pada entitas yang salah, atau ketiadaan sinkronisasi waktu (*timestamp*) pada *buffer* asinkron.

### Fase 4: Duplikasi & Injeksi XML Surgikal (Surgical Patching)
*   **Tujuan:** Menerapkan solusi dan menambal celah logika tanpa mengorbankan integritas format file.
*   **Tindakan AI:**
    *   **WAJIB** membuat salinan/backup dari berkas diagram lama menjadi versi baru (misal: `.drawio` v1 di-copy menjadi v2) sebelum memodifikasi.
    *   Melakukan operasi *Surgical XML Injection* (`replace_file_content` secara presisi) untuk menyuntikkan kode XML konektor baru (garis/panah `edge`) ke dalam hierarki `<root>` diagram.

### Fase 5: Harmonisasi & Penguncian Target Akhir (Verification & Locking)
*   **Tujuan:** Memastikan integritas garis penghubung tetap solid dan tidak berantakan saat dirapikan manual.
*   **Tindakan AI:**
    *   Memastikan setiap panah baru telah terprogram secara valid dengan atribut pengunci (`source` dan `target`) yang merujuk pada `ID` komponen secara eksak (contoh: `target="hw-act"`).
    *   Tahap ini krusial agar saat pengguna melakukan penyesuaian visual (*layouting*) menggunakan aplikasi UI Draw.io, panah-panah logika tetap menempel kuat pada komponennya.

---

## 🚀 Cara Menjalankan Workflow
Anda dapat menjalankan workflow ini dengan mengetikkan perintah berikut di chat:
> *"Tolong jalankan `/engineer-diagram` pada diagram fisik saya di `file.drawio`. Gunakan persona B_Arsitek untuk menambal celah logikanya sesuai 5 Fase Rekayasa."*
