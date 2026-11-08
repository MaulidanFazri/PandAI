<!-- DRAFT -->

# Non-Functional Requirements (NFR) & Traceability Matrix (RTM)

## 1. Spesifikasi Non-Functional Requirements (NFR)

| NFR ID | Kategori | Pernyataan Kebutuhan | Target Verifikasi QA |
| :--- | :--- | :--- | :--- |
| NFR-01 | Performance | Sistem mengeksekusi model regresi ML secara real-time. | Rata-rata latensi endpoint FastAPI < 100 ms. |
| NFR-02 | Performance | Sistem menyusun saran reschedule cepat saat kelas batal. | Kartu saran jadwal tampil dalam <= 5 detik (US-08). |
| NFR-03 | Security | Sistem memvalidasi batas input API dan mengisolasi jadwal user. | Input di luar skala 1-5 ditolak (HTTP 400/422) & proteksi JWT. |
| NFR-04 | Usability | Aplikasi mudah digunakan tanpa membebani waktu perencanaan. | Skor rata-rata Likert >= 4.0/5.0 dari minimal 5 user nyata. |
| NFR-05 | Maintainability | Model hanya memakai Classical ML dengan versi library terkunci. | 0 library Deep Learning & Cyclomatic Complexity <= 10. |

## 2. Requirements Traceability Matrix (RTM)

| Req ID | Deskripsi Kebutuhan | User Story | Prioritas MoSCoW | Komponen | Test Case ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FR-01 | Input tugas, deadline, kesulitan, dan confidence awal | US-01, US-02 | Must Have (P0) | Expo + NestJS | TC-03, TC-06 |
| FR-02 | Prediksi durasi belajar (jam) & prioritas via Scikit-learn | US-04 | Must Have (P0) | FastAPI | TC-01, TC-02 |
| FR-03 | Penempatan otomatis tugas ke slot kosong tanpa tabrak jam tidur | US-07 | Must Have (P0) | NestJS | TC-06 |
| FR-04 | Rating pemahaman (1-5) pasca-belajar untuk update mastery | US-05 | Must Have (P0) | Expo + NestJS | TC-04 |
| FR-05 | Kalibrasi estimasi durasi dari rasio penyelesaian historis | US-06 | Should Have (P1) | FastAPI | TC-05 |
| FR-06 | Konfirmasi jadwal 1-tap / drag-n-drop & reschedule kelas batal | US-08, US-09 | Should Have (P1) | Expo + NestJS | TC-07, TC-08 |
| FR-07 | Pencatatan durasi aktual via Focus Timer & micro-task < 30m | US-10, US-11 | Should / Could | Expo + NestJS | TC-09, TC-10 |