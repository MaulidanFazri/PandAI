# Panduan Real User Testing (UAT) & Kuesioner Evaluasi (Min. 5 Users)

Dokumen ini disiapkan untuk memenuhi syarat wajib Real User Testing Requirement (AoL ML LO3 & AoL SE LO3): minimal 5 pengguna nyata di luar anggota Kelompok 6, dilengkapi profil anonim, skenario pemakaian, serta evaluasi kuantitatif (Likert) dan kualitatif.

## 1. Tabel Profil Responden Anonim (Diisi Saat Pengujian)

| Kode User | Jurusan / Semester | Jumlah Matkul Aktif | Kebiasaan Pencatatan Jadwal Sebelumnya | Tanggal Uji |
| :--- | :--- | :--- | :--- | :--- |
| User-01 | - | - | - | - |
| User-02 | - | - | - | - |
| User-03 | - | - | - | - |
| User-04 | - | - | - | - |
| User-05 | - | - | - | - |

## 2. Skenario Pemakaian (Usage Scenarios) yang Dijalankan Responden

Setiap responden diminta menjalankan 4 langkah skenario berikut secara berurutan di aplikasi PandAI:
1. Skenario 1 (Input Tugas & Confidence Level): Masukkan 3 tugas atau ujian kuliah nyata yang sedang dihadapi minggu ini beserta tanggal deadline, tingkat kesulitan (1-5), dan confidence level saat ini (1-5).
2. Skenario 2 (Prediksi ML & Auto-Scheduling): Tekan tombol pembuatan jadwal otomatis, lalu amati berapa jam estimasi durasi belajar yang direkomendasikan sistem serta di jam berapa saja tugas tersebut ditempatkan pada kalender.
3. Skenario 3 (Simulasi Kelas Batal / Reschedule): Simulasikan satu jadwal kuliah hari ini batal, lihat kartu saran pengganti yang muncul, lalu terima atau geser jadwal tersebut.
4. Skenario 4 (Focus Timer & Feedback Mastery): Jalankan focus timer singkat, tandai sesi selesai, dan berikan rating pemahaman baru (skala 1-5).

## 3. Pertanyaan Kuantitatif (Skala Likert 1 - 5)
Keterangan: 1 = Sangat Tidak Setuju, 2 = Tidak Setuju, 3 = Netral, 4 = Setuju, 5 = Sangat Setuju

1. Kemudahan Penggunaan (Usability - Ease of Use): Antarmuka aplikasi PandAI mudah dipahami dan saya dapat memasukkan tugas serta membuat jadwal belajar tanpa kebingungan. (Skor: 1 - 5)
2. Kecepatan Respons Sistem (Responsiveness): Aplikasi memberikan prediksi durasi belajar dan menyusun jadwal secara instan tanpa waktu tunggu yang mengganggu. (Skor: 1 - 5)
3. Kewajaran Prediksi Durasi ML (Prediction Accuracy): Estimasi durasi jam belajar yang direkomendasikan model Machine Learning terasa logis dan sesuai dengan tingkat kesulitan serta confidence level saya. (Skor: 1 - 5)
4. Kualitas Penempatan Jadwal (Schedule Usefulness): Penempatan jadwal belajar otomatis ke dalam slot waktu kosong sangat membantu saya menentukan prioritas tanpa harus menyusun manual dari nol. (Skor: 1 - 5)
5. Manfaat Fitur Adaptif (Feedback Loop & Reschedule): Fitur rating pemahaman pasca-belajar dan saran reschedule saat kelas batal membuat jadwal saya lebih fleksibel mengikuti dinamika kuliah. (Skor: 1 - 5)
6. Dampak Produktivitas (Overall Impact): Secara keseluruhan, saya merasa PandAI dapat mengurangi waktu yang terbuang untuk merencanakan jadwal dan membantu saya menyelesaikan tugas tepat waktu. (Skor: 1 - 5)

## 4. Pertanyaan Kualitatif (Open-Ended Feedback)

1. Bagian atau fitur mana dari PandAI yang paling membantu Anda dalam mengatur jadwal belajar? Mengapa?
2. Apakah ada kendala, kebingungan, atau hasil rekomendasi waktu belajar yang terasa kurang pas saat Anda mencoba skenario tadi?
3. Saran perbaikan apa yang paling Anda harapkan agar aplikasi ini semakin nyaman dipakai setiap hari?