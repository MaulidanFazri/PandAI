# Risk Analysis (RMMM) & Security Mitigation Plan

Dokumen ini disusun untuk memenuhi kriteria penilaian LO3 Software Engineering (Risk Analysis, Security, and Testing) pada proyek PandAI.

---

## 1. Tabel Analisis Risiko Proyek (RMMM Plan)

Skala Dampak (Impact Scale sesuai materi kuliah Software Risk):
- 1 = Catastrophic (Proyek gagal total atau melanggar aturan mutlak penilaian AoL)
- 2 = Critical (Penurunan performa signifikan atau fitur utama gagal berfungsi)
- 3 = Marginal (Jadwal mundur ringan atau dapat diatasi dengan workaround)
- 4 = Negligible (Dampak minor pada tampilan dan tidak mengganggu fungsi utama)

| Risk ID | Deskripsi Risiko | Probabilitas | Dampak (1-4) | Strategi RMMM (Mitigasi, Monitoring, Management) |
| :--- | :--- | :--- | :--- | :--- |
| RSK-01 | Latensi inferensi model regresi ML (US-5) melebihi batas wajib 100 ms. | 35% | 1 (Catastrophic) | Mitigation: Gunakan model Tree-based Scikit-learn ringan & muat file .pkl ke RAM satu kali saat startup FastAPI. Monitoring: Uji otomatis rata-rata & max latency (< 100 ms) via pytest di setiap Pull Request. Management: Kurangi jumlah estimator pohon & lakukan warm-up call sebelum demo. |
| RSK-02 | Ketidakpatuhan aturan AoL ML (memakai AutoML, preprocessing tidak manual, atau tidak ada proses training eksplisit). | 25% | 1 (Catastrophic) | Mitigation: Wajibkan preprocessing manual (Pandas/NumPy) & training eksplisit pada model regresi durasi (US-5), serta batasi pemakaian LLM hanya untuk ekstraksi teks/gambar di NestJS (US-2 & US-3). Monitoring: Audit notebook ML dan requirements.txt oleh QA. Management: Tulis ulang kode preprocessing secara manual tanpa pustaka AutoML. |
| RSK-03 | Ketidaksesuaian kontrak JSON antar-komponen (Expo, NestJS, FastAPI) & penomoran US di Backlog. | 50% | 2 (Critical) | Mitigation: Kunci dokumen API_CONTRACT.md dan selaraskan nomor referensi US pada tabel Backlog (item 1-33) sejak awal. Monitoring: Validasi skema otomatis menggunakan Pydantic (FastAPI) dan DTO (NestJS). Management: Gunakan mapper di sisi NestJS agar struktur state di Expo tidak rusak. |
| RSK-04 | Kegagalan pembacaan atau timeout saat parsing kalimat bebas (US-2) dan screenshot jadwal (US-3) via LLM. | 45% | 2 (Critical) | Mitigation: Terapkan batas timeout panggilan API LLM dan sediakan state kolom kosong/manual sesuai Acceptance Criteria US-2 & US-3. Monitoring: Uji skenario input kalimat ambigu dan gambar jadwal buram (TC-02 & TC-03). Management: Alihkan langsung pengguna ke form input tugas dan jadwal manual. |
| RSK-05 | Algoritma scheduler (US-7 & US-8) menempatkan sesi belajar menabrak jam tidur, agenda rutin (US-4), atau melebihi slot kosong. | 40% | 2 (Critical) | Mitigation: Pasang hard-constraint jam aktif/tidur (US-4) pada algoritma scheduler dan hitung selisih total durasi terhadap sisa waktu sebelum deadline. Monitoring: Pengujian boundary case jadwal padat (TC-04 & TC-08). Management: Tampilkan peringatan jadwal tidak muat & aktifkan geser jadwal manual (drag-and-drop US-9). |
| RSK-06 | Perbedaan versi library (Scikit-learn, Python 3.12, Node.js, Postgres 18) antar-laptop tim yang memicu crash. | 40% | 2 (Critical) | Mitigation: Gunakan konfigurasi kontainer docker-compose.yml dan kunci rentang versi pada requirements.txt serta package-lock.json. Monitoring: Pantau status build otomatis pada workflow GitHub Actions CI. Management: Jalankan pengujian integrasi QA dan demo menggunakan Docker. |
| RSK-07 | Akurasi estimasi awal meleset bagi pengguna baru (< 5 tugas selesai pada US-5) atau sesi lewat 24 jam tanpa konfirmasi (US-11). | 35% | 3 (Marginal) | Mitigation: Gunakan baseline global model untuk 1-4 tugas pertama sebelum mengaktifkan personalisasi di tugas ke-5, dan jalankan pengecekan otomatis batas 24 jam. Monitoring: Verifikasi logika transisi tugas ke-5 (TC-06) dan status lewat 24 jam (TC-12). Management: Beri opsi koreksi durasi aktual saat review sesi. |
| RSK-08 | Keterlambatan penyelesaian fitur sekunder (Scope Creep pada 33 item Backlog termasuk fitur grup US-13). | 50% | 3 (Marginal) | Mitigation: Fokuskan pengerjaan Sprint awal pada item berprioritas Must (US-1, US-2, US-4 s/d US-11) dan batasi WIP di Kanban. Monitoring: Evaluasi progres mingguan menjelang konsultasi Week 7 & Week 11. Management: Tunda fitur berprioritas Could (Backlog 32-33) jika waktu terbatas. |

### Perhitungan Risk Exposure (RE)
Mengacu pada rumus materi kuliah (`RE = Probabilitas x Estimasi Dampak Pengerjaan Ulang`):
- Pada **RSK-03 (Mismatch Kontrak API & Backlog)**: Jika terjadi ketidakcocokan struktur data pada endpoint utama antara Expo, NestJS, dan FastAPI, dibutuhkan waktu pengerjaan ulang (*rework*) sekitar 12 jam kerja. Dengan probabilitas `0.50`, nilai *Risk Exposure* adalah `0.50 x 12 jam = 6 jam kerja ekstra` yang dimitigasi sejak awal melalui penguncian `API_CONTRACT.md`.

---

## 2. Identifikasi Celah Keamanan & Mitigasi (Secure SDLC)

| Tahap SDLC | Potensi Celah Keamanan (Vulnerability) | Strategi Mitigasi Keamanan di PandAI |
| :--- | :--- | :--- |
| Authentication & Session (US-1) | Pencurian kredensial atau penyalahgunaan sesi login pengguna di perangkat mobile. | Melakukan hashing password (bcrypt), menggunakan JWT untuk otorisasi endpoint, dan menyimpan token sesi di penyimpanan terenkripsi (Expo SecureStore). |
| Input & LLM Parsing (US-2 & US-3) | Prompt Injection pada input kalimat bebas atau unggahan file berbahaya pada fitur screenshot jadwal. | Membatasi panjang karakter input teks, mengisolasi instruksi sistem LLM agar hanya mengeluarkan JSON, serta memvalidasi format (PNG/JPG) dan ukuran maks gambar. |
| ML & API Validation (US-5 & US-11) | Malformed Payload / Denial of Service akibat pengiriman angka ekstrem ke endpoint prediksi ML. | Memasang validasi rentang ketat menggunakan Pydantic (skala 1-5 untuk kesulitan & pemahaman, serta deadline >= 0) sebelum data diproses model Scikit-learn. |
| Data Privacy & Access Control | Kebocoran data jadwal kuliah, waktu aktif (US-4), dan riwayat belajar antar-mahasiswa. | Memastikan setiap query database PostgreSQL memfilter data berdasarkan user_id dari token JWT pemilik sesi yang sah. |
| Deployment & Secrets Config | Eksposur kunci rahasia (DATABASE_URL, JWT_SECRET, API Key LLM) di repositori GitHub publik. | Menyimpan seluruh kredensial di variabel lingkungan (.env) dan memastikan file .env terdaftar di dalam .gitignore. |