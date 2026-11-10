# PandAI Master Test Plan & Test Cases (Aligned with Official US-1 to US-12)

## 1. Strategi 4 Level Pengujian (AoL SE LO3)
1. **Unit Testing:** Menguji fungsi prediksi regresi ML, rumus skor prioritas, dan validasi input menggunakan `pytest` dan `Jest`.
2. **Integration Testing:** Menguji komunikasi endpoint antara NestJS, PostgreSQL, dan FastAPI (termasuk syarat latensi < 100 ms).
3. **System Testing:** Menguji alur end-to-end di aplikasi Expo mulai dari onboarding, input tugas, penjadwalan otomatis, hingga review sesi.
4. **Acceptance Testing (UAT):** Pengujian langsung oleh minimal 5 mahasiswa di luar tim menggunakan kuesioner Likert (1-5) dan kualitatif.

---

## 2. Master Test Cases (Berdasarkan Acceptance Criteria US-1 s/d US-12)

| Test ID | Level | US ID | Backlog No | Skenario Pengujian | Hasil yang Diharapkan (Acceptance Criteria) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-01 | System | US-1 | 1, 2 | Register akun baru, login valid, & tes password salah | Akun baru masuk ke onboarding; login valid masuk ke halaman Hari Ini & sesi tersimpan; password salah ditolak dengan pesan error. |
| TC-02 | Integration | US-2 | 5, 6 | Input tugas dengan kalimat bebas ("laporan DB 10 halaman deadline Jumat") | Judul, matkul, tipe, deadline, dan ukuran terisi otomatis; bagian yang gagal terbaca dibiarkan kosong untuk diisi manual. |
| TC-03 | System | US-3 | 23, 24, 25 | Sinkronisasi Google Calendar & upload screenshot jadwal kuliah | Perubahan event Google Calendar muncul otomatis; screenshot menampilkan daftar kelas + input pemahaman awal (1-5); gambar rusak memunculkan opsi manual. |
| TC-04 | System | US-4 | 3, 4 | Simpan preferensi jam tidur, jam produktif, batas harian, & agenda rutin | Preferensi tersimpan di profil dan tidak ada sesi belajar yang dijadwalkan menabrak jam tidur atau agenda rutin. |
| TC-05 | Unit & Perf | US-5 | 7, 8, 9, 10 | Prediksi durasi tugas baru & uji latensi inferensi FastAPI (< 100 ms) | Menampilkan estimasi rentang jam beserta faktor utamanya dengan waktu respons endpoint ML < 100 ms. |
| TC-06 | Integration | US-5 | 26 | Personalisasi estimasi durasi setelah >= 5 tugas selesai tercatat | Setelah 5 tugas memiliki durasi aktual, estimasi tugas ke-6 otomatis menyesuaikan kebiasaan kecepatan kerja pengguna. |
| TC-07 | Integration | US-6 | 11, 12 | Urutan prioritas tugas di halaman Hari Ini beserta alasannya | Tugas terurut berdasarkan deadline, estimasi durasi, bobot, dan pemahaman matkul, dilengkapi teks alasan singkat. |
| TC-08 | System | US-7 | 13, 14 | Penjadwalan otomatis ke waktu kosong & kondisi durasi melebihi slot | Tugas masuk ke waktu kosong sesuai prioritas; jika total durasi melebihi waktu kosong sebelum deadline, muncul peringatan & saran pecah tugas. |
| TC-09 | System | US-8 | 15, 16 | Saran sesi belajar mandiri untuk matkul pemahaman terendah | Waktu kosong sisa diisi saran matkul dengan pemahaman awal terendah; tombol Terima menyimpan jadwal dan tombol Ganti memberi saran lain. |
| TC-10 | System | US-9 | 20, 21, 22 | Tandai kelas batal & geser sesi belajar di timeline (drag-and-drop) | Kelas batal memunculkan saran kegiatan pengganti; pergeseran sesi di timeline tersimpan sebagai preferensi pengguna. |
| TC-11 | System | US-10 | 17, 18 | Notifikasi pengingat 10 menit sebelum sesi dengan aksi Tunda / Lewati | Notifikasi tampil 10 menit sebelum sesi; tekan Tunda menggeser sesi 15 menit, tekan Lewati menandai sesi dilewati. |
| TC-12 | Integration | US-11 | 18, 19, 27, 28 | Konfirmasi hasil sesi belajar (rating 1-5) & tes lewat 24 jam tanpa konfirmasi | Input Sebagian/Belum memindahkan sisa durasi ke slot kosong berikutnya; sesi tanpa konfirmasi > 24 jam otomatis dianggap belum selesai. |
| TC-13 | System | US-12 | 29, 30, 31 | Evaluasi ringkasan mingguan & deteksi penurunan pemahaman matkul | Menampilkan tugas selesai vs rencana, jam belajar, akurasi estimasi, dan memberi tanda khusus pada matkul yang pemahamannya turun. |