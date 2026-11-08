---
name: Bug Report (QA)
about: Laporkan temuan bug, error integrasi, atau pelanggaran batas latensi (< 100 ms)
title: "[BUG] <Komponen: FE/BE/ML> - <Ringkasan Masalah>"
labels: ["bug", "qa-review"]
assignees: ""
---

### Informasi Umum
- Test Case ID Terkait: (Contoh: TC-02 / TC-06)
- User Story Terkait: (Contoh: US-04 / US-07)
- Komponen Sistem: (Pilih: Mobile App Expo / Backend NestJS / ML Service FastAPI)
- Tingkat Keparahan (Fault Severity):
  - [ ] 1 - Cosmetic (Salah warna/typo/layout geser, fungsi utama aman)
  - [ ] 2 - Moderate (Fitur terganggu sebagian, masih ada jalan alternatif)
  - [ ] 3 - Major (Fitur utama gagal, jadwal bentrok, atau latensi ML > 100 ms)
  - [ ] 4 - Critical (Aplikasi crash, force close, atau data hilang)

### Langkah Reproduksi (Steps to Reproduce)
1. Nyalakan layanan atau buka halaman aplikasi...
2. Masukkan data input atau kirim request JSON...
3. Tekan tombol aksi...
4. Amati pesan error yang muncul.

### Hasil yang Diharapkan (Expected Behavior)
Jelaskan perilaku sistem yang seharusnya terjadi sesuai Acceptance Criteria.

### Hasil Aktual (Actual Behavior)
Jelaskan apa yang sebenarnya terjadi beserta catatan waktu latensi (ms).

### Bukti Screenshot atau Log Error
Tempelkan tangkapan layar UI atau log terminal di bagian ini.