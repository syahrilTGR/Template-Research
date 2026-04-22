---
description: Navigasi dan query basis pengetahuan global menggunakan Knowledge Graph (GraphRAG).
---

# 🗺️ Workflow: Graphify Navigation

Gunakan workflow ini (`/graphify`) untuk menanyakan pertanyaan tingkat tinggi tentang hubungan antar komponen riset Anda yang sudah dipetakan.

### 🛠️ Langkah-Langkah (AI to User)

1. **Graph Check**: AI memastikan library `graphifyy` dan folder `graphify-out/` sudah ada. 
2. **Knowledge Retrieval**: AI menggunakan data dari Knowledge Graph (via `rtk graphify`) untuk melihat "God Nodes" (konsep sentral) dan hubungan antar bab.
3. **Synthesis**: AI memberikan jawaban yang menyatukan berbagai file (coding, paper, draft) secara terintegrasi.

### 🚀 Cara Menjalankan
Cukup ketik:
> "/graphify. Update graf saya dan tunjukkan hubungan antar komponen."

---
> [!IMPORTANT]
> Workflow ini sangat powerful untuk mendeteksi inkonsistensi antar bab yang berjauhan.
