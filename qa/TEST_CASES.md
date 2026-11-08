# PandAI Master Test Cases (4 Levels of Testing)

| Test ID | Level Uji | US ID | Komponen | Skenario Pengujian | Data Input | Hasil yang Diharapkan | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-01 | Unit & Integration | US-04 | FastAPI | Prediksi durasi belajar input normal | difficulty: 4, confidence: 2, deadline: 3 hari | HTTP 200 OK, mengembalikan durasi > 0 jam dan skor prioritas 0-100. | Pending |
| TC-02 | Integration (Perf) | US-04 | FastAPI | Uji batas latensi inferensi ML < 100 ms | 10x request beruntun ke POST /predict-duration | Rata-rata waktu respons tercatat < 100 ms. | Pending |
| TC-03 | Unit (Boundary) | US-04 | FastAPI | Uji batas input invalid (Category-Partition) | confidence: 0, confidence: 6, deadline: -2 | Ditolak dengan HTTP 400/422 tanpa membuat server crash. | Pending |
| TC-04 | Integration | US-05 | NestJS & ML | Update rating pemahaman pasca-belajar | Kirim post_study_confidence_rating: 4 | Skor mastery mata kuliah di database berhasil diperbarui. | Pending |
| TC-05 | Integration | US-06 | FastAPI | Kalibrasi estimasi dari riwayat aktual user | Rasio historis user: 1.25 + input tugas baru | Durasi prediksi otomatis dikalibrasi 1.25x dari durasi dasar. | Pending |
| TC-06 | System | US-07 | NestJS & Expo | Penempatan otomatis tugas ke slot kosong | 3 tugas aktif + slot kosong jam 13.00-17.00 | Tugas masuk ke slot kosong sesuai prioritas tanpa tabrak jam tidur. | Pending |
| TC-07 | System | US-08 | Expo & NestJS | Trigger reschedule cepat saat kelas batal | Tekan tombol "Ya, batal" pada kelas jam 13.00 | Kartu saran pengganti muncul untuk slot tersebut dalam <= 5 detik. | Pending |
| TC-08 | System | US-09 | Expo & NestJS | Konfirmasi 1-tap dan pindah jadwal drag-n-drop | Tekan Terima atau geser blok jadwal di kalender | Jadwal tersimpan di database dan tampil sesuai posisi baru. | Pending |
| TC-09 | System | US-10 | NestJS | Pengisian jeda tanggung (< 30 menit) | Jeda kosong 20 menit di antara dua kelas | Sistem menyisipkan saran micro-task (review catatan/flashcard). | Pending |
| TC-10 | System | US-11 | Expo & NestJS | Pencatatan durasi aktual via Focus Timer | Jalankan timer belajar lalu tekan Selesai | Durasi aktual tersimpan otomatis sebagai data histori pengguna. | Pending |
| TC-11 | Security | Semua | NestJS | Akses endpoint jadwal tanpa token login | Panggil GET /api/schedules tanpa header JWT | Request ditolak dengan status HTTP 401 Unauthorized. | Pending |
| TC-12 | Acceptance (UAT) | Semua | End-to-End | Pengujian pemakaian nyata oleh 5 mahasiswa | 5 responden di luar tim menjalankan aplikasi | Rata-rata skor Usability & Usefulness >= 4.0 dari skala Likert 5.0. | Pending |