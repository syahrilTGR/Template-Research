---
description: Sinkronisasi Knowledge Graph lokal ke Global Brain Center (incremental, tidak overwrite)
---

# Workflow: Sync Global Brain (Incremental)

Workflow ini menggabungkan data riset terbaru dari `graphify-out/graph.json` ke dalam `Brain-Global-Center`,
lalu me-refresh Obsidian Vault dan `GRAPH_REPORT.md` secara otomatis.

**Environment Wajib**: `train_mx150` (Conda/Miniconda di `F:/miniconda3/envs/train_mx150`)  
**Script Utama**: `scripts/update_global_brain.py`

---

## Step 0: Audit Perubahan (Git Status)

Sebelum sinkronisasi, periksa file mana saja yang berubah untuk memastikan context penelitian tetap akurat.

// turbo
```powershell
rtk git status
```

---

## Step 1: Sinkronisasi Komprehensif (Code & Docs)

Pastikan database `graph.json` lokal mencakup perubahan kode DAN dokumen (seperti `.md` di folder `intelligence/`) sebelum dikirim ke pusat.

// turbo
```powershell
rtk powershell -c "conda run -n train_mx150 python .agents\skills\graphify\scripts\sync_brain_comprehensive.py"
```

> **Catatan**: Skrip ini secara otomatis akan menjalankan `graphify update` (untuk kode) dan `scripts/update_global_brain.py` (untuk sinkronisasi global), sehingga Anda tidak perlu menjalankan Step 2 secara terpisah.

---

## Step 2: Verifikasi & Audit Hasil

### Output yang Diharapkan ✅

```
Syncing from local graph: f:\ML_Project\Template\graphify-out\graph.json
Graph loaded: [N] nodes, [E] edges.
Global Research Brain Finalized!
Updated Report saved to C:\Users\Syahril\Documents\Brain-Global-Center\GRAPH_REPORT.md
```

> **Peringatan**: Jika outputnya `Graph loaded: X nodes, 0 edges`, periksa apakah skrip membaca file lokal dengan benar.

---

## Step 3: Verifikasi Hasil Laporan

```powershell
# Lihat 30 baris pertama laporan untuk memeriksa God Nodes dan statistik terbaru
rtk powershell -c "Get-Content 'C:/Users/Syahril/Documents/Brain-Global-Center/GRAPH_REPORT.md' -TotalCount 30"
```

---

## Step 4 (Opsional): Buka Obsidian untuk Visualisasi

Buka folder `C:/Users/Syahril/Documents/Brain-Global-Center/Obsidian-Vault` sebagai Vault di Obsidian
untuk melihat visualisasi graph riset terbaru.

---

## Catatan Teknis Penting

| Poin | Detail |
|---|---|
| **Environment** | Selalu gunakan `conda run -n train_mx150` |
| **Sumber Data** | `graphify-out/graph.json` (lokal) → dipush ke `global-graph.json` (Global Brain) |
| **Skema edges** | File lokal pakai `"edges"`, file global kadang pakai `"links"` |
| **Frekuensi** | Jalankan setiap kali ada perubahan signifikan di kode atau draf thesis |

---
