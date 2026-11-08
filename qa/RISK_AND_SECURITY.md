# Risk Analysis (RMMM) & Security Mitigation Plan

## 1. Tabel Analisis Risiko Proyek (Skala Dampak: 1 = Catastrophic s/d 4 = Negligible)

| Risk ID | Deskripsi Risiko | Kategori | Probabilitas | Dampak | Strategi Mitigasi (Pencegahan) | Rencana Kontingensi (Management) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| RSK-01 | Latensi inferensi ML melebihi batas wajib 100 ms. | Performa | 35% | 1 (Catastrophic) | Pakai model Tree-based Scikit-learn & muat model.pkl ke RAM saat startup server. | Kurangi jumlah estimator pohon & lakukan warm-up request sebelum demo. |
| RSK-02 | Penggunaan fitur Deep Learning (LLM/OCR) yang dilarang AoL ML. | Akademik | 25% | 1 (Catastrophic) | Geser fitur LLM/OCR ke Won't Have & gunakan form input terstruktur. | Hapus dependensi non-klasik dari requirements.txt. |
| RSK-03 | Ketidaksesuaian format JSON antara Expo, NestJS, dan FastAPI. | Integrasi | 50% | 2 (Critical) | Kunci dokumen API_CONTRACT.md sebelum penulisan kode integrasi dimulai. | Pasang mapper/adapter di NestJS agar Frontend tidak perlu ubah state. |
| RSK-04 | Perbedaan versi library antar-laptop tim yang memicu crash. | Lingkungan | 45% | 2 (Critical) | Gunakan docker-compose.yml dan kunci versi paket di requirements.txt. | Jalankan seluruh pengujian QA dan demo di dalam kontainer Docker. |
| RSK-05 | Algoritma scheduler menempatkan tugas menabrak jam tidur. | Logika | 40% | 2 (Critical) | Tetapkan batas waktu tidur (23.00-06.00) pada algoritma scheduler NestJS. | Aktifkan fitur geser jadwal manual (drag-and-drop) sesuai US-09. |

## 2. Mitigasi Celah Keamanan (Secure SDLC)

| Tahap SDLC | Potensi Celah Keamanan | Implementasi Mitigasi di PandAI |
| :--- | :--- | :--- |
| Design & Auth | Akses jadwal milik pengguna lain tanpa izin. | Autentikasi token JWT di NestJS & filter user_id pada setiap query database. |
| Input Validation | Payload angka ekstrem yang membuat model ML atau server crash. | Validasi rentang input ketat menggunakan Pydantic (skala 1-5) di FastAPI. |
| Config & Secret | Kebocoran password database atau kunci API di repositori GitHub. | Simpan kredensial di file .env lokal dan masukkan .env ke dalam .gitignore. |