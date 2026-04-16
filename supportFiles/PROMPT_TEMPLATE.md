# Session Start Prompt Template

Gunakan template ini saat memulai atau mereset sesi AI agar asisten kembali ke konteks proyek.

```markdown
Hai, jalankan `/context-summary`. 

**Audit Wajib Sebelum Mulai:**
1. Cek `ACTION_PLAN.md`: Apakah Phase 0 sudah [x]? 
2. Cek `gemini.md` & `SKILL.md`: Apakah masih ada placeholder [TBD]?

Jangan lakukan tugas akademik sebelum status audit di atas 'CLEAN'.
```

### 🆕 Sesi Pertama (Bootstrap)
Gunakan ini saat baru pertama kali melakukan clone repositori:
```markdown
Halo! Saya baru saja melakukan clone repositori template ini. Tolong jalankan protokol onboarding/bootstrap sesuai instruksi di `gemini.md` dan `custom_project_skill/SKILL.md`. Bantu saya mengisi profil riset saya.
```
