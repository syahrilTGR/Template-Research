---
description: Sinkronisasi draf cerdas antara repositori koding lokal dan Global Brain Center (OneDrive/Cloud)
---

# 🧠 Workflow: Sync Global Brain

Gunakan workflow ini (`/sync-global-brain`) untuk memastikan draf Markdown di repositori ini, file Word di OneDrive, dan catatan di Vault Obsidian saling sinkron secara semantik.

### 🛠️ Langkah-Langkah (AI to User)

1. **Inisialisasi**: Asisten akan menjalankan skrip `scripts/sync_global_brain.ps1`.
2. **Change Detection**: AI membandingkan timestamp dan konten di `supportFiles/handoff.md` dengan file source di OneDrive (jika dikonfigurasi).
3. **Conflict Resolution**: Jika ada perbedaan konten, AI akan bertanya: *"Versi mana yang ingin Anda jadikan acuan?"*
4. **Final Sync**: AI memperbarui semua titik (Handoff & Wiki) agar memiliki informasi terbaru yang sama.

### 🚀 Cara Menjalankan
Cukup ketik:
> "/sync-global-brain. Tolong pastikan draf koding saya sinkron dengan update terbaru di Word."

---
> [!NOTE]
> Pastikan Anda sudah mengatur path OneDrive Anda di dalam file `scripts/sync_global_brain.ps1`.
