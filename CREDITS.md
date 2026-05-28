## 🔍 File Properties (Inline Index Block)
- **File Path:** `CREDITS.md`
- **Purpose:** Documenting third-party open-source libraries, APIs, servers, and frameworks used in this research repository.
- **Functions & Roles:** Provides academic citation credits, lists developer links, respects software licenses, and supports research integrity auditing.
- **Upstream Dependencies:** None
- **Downstream Dependencies:** `supportFiles/FILE_INDEX.md`

---

# 🎓 Atribusi Lisensi & Kredit Open-Source (CREDITS)

Proyek template penelitian kolaboratif ini dibangun di atas fondasi teknologi dan kontribusi luar biasa dari komunitas pengembang open-source global. Dokumentasi ini disusun sebagai wujud kepatuhan terhadap lisensi perangkat lunak bebas, menjaga integritas ilmiah riset akademik Anda, serta mempermudah audit lisensi naskah skripsi/penelitian.

Kami menyampaikan apresiasi dan kredit sepenuhnya kepada proyek-proyek open-source berikut:

---

## 🗺️ 1. Model Context Protocol (MCP) Servers

Perkakas berbasis protokol MCP yang menjembatani asisten AI lokal dengan aplikasi eksternal:

| Nama Komponen | Sumber Hulu (Upstream Repository) | Lisensi | Fungsi dalam Repositori |
| :--- | :--- | :--- | :--- |
| **`notebooklm-mcp-cli`** | [GitHub - notebooklm-mcp-cli](https://github.com/) | MIT | Menyediakan executable `nlm.exe` untuk menghubungkan obrolan asisten dengan data Google NotebookLM Anda di cloud. |
| **`chrome-devtools-mcp`** | [GitHub - chrome-devtools-mcp](https://github.com/) | MIT | Mengizinkan asisten AI mengendalikan browser Chrome lokal untuk simulasi kueri web dan pengetesan antarmuka. |
| **`graphify`** | [GitHub - graphify](https://github.com/) | MIT | Menghasilkan Knowledge Graph interaktif untuk memetakan hubungan AST (Abstract Syntax Tree) dari kode riset Anda. |

---

## 📚 2. Basis Data Ilmiah Global (Scholarly Database APIs)

Antarmuka pemrograman aplikasi (API) akademik yang diakses secara legal oleh perkakas pencarian literatur di `.agents/skills/`:

| Nama Layanan | Penyedia / Institusi | Aksesibilitas | Peran Integrasi |
| :--- | :--- | :--- | :--- |
| **OpenAlex API** | [OurResearch / OpenAlex](https://openalex.org/) | Terbuka & Gratis (Open-Access) | Digunakan oleh skill `literature_search_openalex` untuk mencari dokumen ilmiah, sitasi, dan mengunduh PDF secara legal. |
| **arXiv API** | [Cornell University / arXiv](https://arxiv.org/) | Terbuka & Gratis (Open-Access) | Digunakan oleh skill `literature_search_arxiv` untuk menelusuri naskah ilmiah pra-cetak (*preprints*) di bidang koding/ML secara real-time. |

---

## 📄 3. Pustaka Manipulasi & Ekstraksi Dokumen (Software Libraries)

Perpustakaan kode yang terpasang di dalam sistem maupun di dalam virtual environment (`thesis_venv`) untuk menyusun dokumen formal:

| Nama Pustaka | Platform / Registri | Lisensi | Fungsi Teknis |
| :--- | :--- | :--- | :--- |
| **`docx` (Node.js)** | [NPM - docx](https://www.npmjs.com/package/docx) | MIT | Pustaka JavaScript utama untuk membangun berkas Word (`.docx`) akademik dari nol secara terprogram dengan gaya pemformatan tinggi. |
| **`python-docx`** | [PyPI - python-docx](https://pypi.org/project/python-docx/) | MIT | Pustaka Python untuk membongkar, membaca, dan menyisipkan konten ke dalam berkas XML Word. |
| **`python-pptx`** | [PyPI - python-pptx](https://pypi.org/project/python-pptx/) | MIT | Pustaka Python untuk menyusun dan memperbarui berkas presentasi PowerPoint (`.pptx`) secara otomatis. |
| **`openpyxl`** | [PyPI - openpyxl](https://pypi.org/project/openpyxl/) | MIT | Pustaka manipulasi berkas spreadsheet Excel (`.xlsx`) untuk mengelola metrik data tabel. |
| **`pdfplumber`** | [PyPI - pdfplumber](https://pypi.org/project/pdfplumber/) | MIT | Menggerakkan mesin **Smart Extractor V2.5** (`scripts/extract_pdfs.py`) untuk mengekstraksi baris teks dan tabel numerik dari PDF jurnal. |
| **`Playwright`** | [Microsoft / Playwright](https://playwright.dev/) | Apache-2.0 | Otomatisasi browser untuk mensimulasikan pengetesan dan kueri situs web eksternal. |

---

## 🎨 4. Platform Memori Eksternal & Visualisasi (Application Ecosystems)

Platform visualisasi data dan catatan terstruktur yang diintegrasikan sebagai repositori memori:

*   **Obsidian (LLM Wiki Vault):**
    *   *Sumber:* [Obsidian.md](https://obsidian.md/) (Aplikasi basis pengetahuan berbasis Markdown).
    *   *Lisensi:* Komersial Gratis (untuk penggunaan pribadi/akademik).
    *   *Fungsi:* Media visualisasi grafik hubungan antar konsep dan ringkasan paper yang disimpan asisten di folder `intelligence/`.
*   **Draw.io (Diagrams.net Scheme):**
    *   *Sumber:* [Draw.io / Jgraph](https://www.draw.io/) (Aplikasi open-source pembuat diagram alur).
    *   *Lisensi:* Apache-2.0.
    *   *Fungsi:* Skema XML diagram yang dihasilkan perkakas asisten dirancang agar kompatibel dan dapat disunting langsung di editor Draw.io.

---

> [!NOTE]
> Semua kontribusi kekayaan intelektual di atas dihargai sepenuhnya dan dilindungi oleh pemegang hak cipta masing-masing lisensi. Penggunaan dalam proyek ini murni ditujukan untuk tujuan riset akademik dan pembelajaran non-komersial.
