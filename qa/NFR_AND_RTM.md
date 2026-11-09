# Non-Functional Requirements (NFR) & Requirements Traceability Matrix (RTM)

Dokumen ini disusun oleh Quality Assurance (QA) untuk menjamin kualitas non-fungsional serta ketertelusuran (traceability) antara User Stories (US-1 s/d US-12), Product Backlog (1-31), dan skenario pengujian pada proyek PandAI.

---

## 1. Spesifikasi Non-Functional Requirements (NFR)

| NFR ID | Kategori | Pernyataan Kebutuhan (Requirement Statement) | Metrik & Target Verifikasi QA |
| :--- | :--- | :--- | :--- |
| NFR-01 | Performance | Endpoint Machine Learning harus mengeksekusi model regresi estimasi durasi belajar secara real-time. | Rata-rata dan lonjakan maksimum inference latency FastAPI < 100 ms (diuji via Pytest & Postman). |
| NFR-02 | Performance | Algoritma penjadwalan otomatis, saran waktu kosong, dan penyesuaian kelas batal harus merespons secara cepat. | Waktu pemrosesan jadwal dan kemunculan kartu saran pengganti <= 5 detik. |
| NFR-03 | Security & Session | Sistem wajib mengamankan kredensial akun, menyimpan sesi login secara persisten, dan memvalidasi batas input API. | Password di-hash, sesi tersimpan aman (user tidak perlu login ulang), dan input di luar skala 1-5 ditolak (HTTP 400/422). |
| NFR-04 | Usability | Antarmuka aplikasi harus praktis (low-effort) dan membantu mahasiswa mengatur prioritas belajar harian. | Rata-rata skor kepuasan >= 4.0 / 5.0 (skala Likert) dari minimal 5 pengguna nyata di luar tim (UAT). |
| NFR-05 | ML Compliance | Model utama wajib menggunakan Classical ML (Scikit-learn) dengan manual preprocessing dan proses training eksplisit. | 0 library AutoML di requirements.txt; LLM hanya digunakan sebagai parser input (US-2 & US-3), bukan model utama yang dinilai. |
| NFR-06 | Reliability | Fitur ekstraksi kalimat bebas (LLM) dan import screenshot jadwal harus memiliki mekanisme fallback jika gagal terbaca. | Jika teks/gambar gagal diparsing, sistem tidak crash dan otomatis menyediakan kolom koreksi/input manual. |

---

## 2. Requirements Traceability Matrix (RTM)

Catatan QA: Kolom Story & Backlog memetakan nomor User Story resmi (US-1 s/d US-12) dengan nomor urut item pada tabel Product Backlog yang kini berjumlah 31 item bersih[cite: 16, 17, 18, 19, 20].

| Req ID | Deskripsi Kebutuhan Fungsional & Non-Fungsional | Story & Backlog | Prioritas | Komponen & Test ID |
| :--- | :--- | :--- | :--- | :--- |
| FR-01 | Registrasi akun, login, validasi password salah, & penyimpanan sesi login persisten | US-1 (Backlog 1, 2)[cite: 19] | Must[cite: 16, 19] | Expo, NestJS, DB (TC-01) |
| FR-02 | Input tugas satu kalimat bebas via parsing LLM & form koreksi manual jika ada kolom tak terbaca | US-2 (Backlog 5, 6)[cite: 19] | Must[cite: 16, 19] | Expo, NestJS (TC-02) |
| FR-03 | Sinkronisasi event Google Calendar & import screenshot jadwal (LLM Vision) + pemahaman awal (1-5) | US-3 (Backlog 23, 24, 25)[cite: 19, 20] | Should[cite: 16, 20] | Expo, NestJS (TC-03) |
| FR-04 | Pengaturan waktu aktif onboarding (jam tidur, jam produktif, batas harian, & agenda rutin) | US-4 (Backlog 3, 4)[cite: 19] | Must[cite: 16, 19] | Expo, NestJS, DB (TC-04) |
| FR-05 | Prediksi rentang durasi tugas & personalisasi ML setelah >= 5 tugas selesai tercatat | US-5 (Backlog 7-10, 26)[cite: 19, 20] | Must / Should[cite: 16, 19, 20] | FastAPI, NestJS, Expo (TC-05, TC-06) |
| FR-06 | Perhitungan skor prioritas tugas di halaman Hari Ini beserta alasan singkatnya | US-6 (Backlog 11, 12)[cite: 19] | Must[cite: 16, 19] | NestJS, Expo (TC-07) |
| FR-07 | Penjadwalan otomatis ke waktu kosong & peringatan jika total durasi melebihi slot sebelum deadline | US-7 (Backlog 13, 14)[cite: 19] | Must[cite: 16, 19] | NestJS, Expo (TC-08) |
| FR-08 | Rekomendasi sesi belajar di sisa waktu kosong untuk matkul dengan tingkat pemahaman terendah | US-8 (Backlog 15, 16)[cite: 19] | Must[cite: 16, 19] | NestJS, Expo (TC-09) |
| FR-09 | Penyesuaian cepat saat kelas ditandai batal (kartu saran pengganti) & drag-and-drop timeline | US-9 (Backlog 20, 21, 22) | Must[cite: 17, 20] | Expo, NestJS (TC-10) |
| FR-10 | Notifikasi pengingat 10 menit sebelum sesi belajar dimulai dengan aksi Tunda (15 menit) atau Lewati | US-10 (Backlog 17, 18)[cite: 19, 20] | Must[cite: 18, 19, 20] | Expo, NestJS (TC-11) |
| FR-11 | Konfirmasi hasil sesi (durasi aktual, rating 1-5, pindah sisa durasi, & aturan lewat 24 jam) | US-11 (Backlog 18, 19, 27, 28)[cite: 20] | Must / Should[cite: 18, 20] | Expo, NestJS, FastAPI (TC-12) |
| FR-12 | Ringkasan mingguan (tugas selesai vs rencana, akurasi estimasi, & tanda matkul pemahaman turun) | US-12 (Backlog 29, 30, 31)[cite: 20] | Should[cite: 18, 20] | NestJS, Expo (TC-13) |
| NFR-01 | Verifikasi batas latensi inferensi Machine Learning < 100 ms pada endpoint FastAPI | US-5 (Backlog 8)[cite: 19] | Must[cite: 16, 19] | FastAPI (TC-05) |
| NFR-04 | Evaluasi Usability & Usefulness oleh minimal 5 mahasiswa nyata di luar tim pengembang | Semua US | Must | End-to-End App (UAT) |