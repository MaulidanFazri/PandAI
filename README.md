# PandAI

Our Member :
1. 2902726403 - Aldridge Hansel Robin
2. 2902726422 - Bernardus Allan Fisthiantara
3. 2902726492 - Friska Deviana
4. 2902726555 - I Gede Wahyu Dipta Pariandika
5. 2902726675 - Maulidan Fazri

---

## Tentang Project

PandAI adalah aplikasi mobile berbasis **Expo (React Native)** yang membantu mahasiswa mengatur tugas dan jadwal belajar. Aplikasi ini didukung **Back-End NestJS** (API, database, perhitungan prioritas, dan penjadwalan) serta **Machine Learning FastAPI** (prediksi durasi tugas). Project ini dikerjakan secara kelompok, jadi semua anggota wajib mengikuti alur branch dan alur Jira di bawah supaya kodenya gak saling bentrok.

Board Jira: [pandai6.atlassian.net](https://pandai6.atlassian.net/jira/software/projects/KAN/boards) (project key **KAN**)

## Tim dan Peran

| Anggota | Peran | Branch | Label Jira |
|---|---|---|---|
| I Gede Wahyu Dipta Pariandika | Product Owner / Project Manager | | |
| Friska Deviana | Front-End | `feature/front-end` | `fe` |
| Aldridge Hansel Robin | Back-End | `feature/back-end` | `be` |
| Bernardus Allan Fisthiantara | Machine Learning | `feature/ML-Data` | `ml` |
| Maulidan Fazri | Quality Assurance | `integration/pandai` | |

Epic dan Story dipegang PO. Subtask di-assign ke anggota sesuai bagiannya.

## Cakupan MVP (target 29 November 2026)

| ID | Jira | User Story | Epic | Rilis |
|---|---|---|---|---|
| US-1 | KAN-55 | Login dan registrasi akun | A | MVP |
| US-2 | KAN-9 | Input tugas lewat kalimat bebas | A | MVP |
| US-3 | KAN-10 | Import jadwal kuliah | A | Rilis 2 |
| US-4 | KAN-11 | Pengaturan waktu aktif | A | MVP |
| US-5 | KAN-12 | Estimasi durasi tugas | B | MVP (AC 1), Rilis 2 (AC 2) |
| US-6 | KAN-13 | Prioritas tugas harian | B | MVP |
| US-7 | KAN-15 | Penjadwalan tugas otomatis | C | MVP |
| US-8 | KAN-14 | Saran sesi belajar di waktu kosong | B | MVP |
| US-9 | KAN-16 | Penyesuaian jadwal saat agenda berubah | C | MVP |
| US-10 | KAN-18 | Pengingat sesi belajar | E | MVP |
| US-11 | KAN-17 | Konfirmasi hasil sesi belajar | D | MVP (AC 1), Rilis 2 (AC 2 dan 3) |
| US-12 | KAN-19 | Ringkasan belajar mingguan | D | Rilis 2 |

Epic: A. Input dan Import Jadwal/Tugas, B. Prediksi dan Prioritas, C. Penjadwalan Otomatis dan Adaptif, D. Tracking dan Evaluasi Progres, E. Pengingat.

Subtask berlabel `mvp` dikerjakan duluan. Subtask Rilis 2 tetap di Backlog sampai MVP selesai.

## Struktur Branch

| Branch | Fungsi | Boleh push langsung? |
|---|---|---|
| `main` | Versi final yang stabil dan siap dikumpulkan/didemokan | Tidak |
| `integration/pandai` | Tempat menggabungkan semua fitur dan dites QA | Tidak, lewat Pull Request |
| `feature/front-end` | Tampilan dan logika aplikasi (Expo / React Native) | Ya, khusus tim front-end |
| `feature/back-end` | API NestJS, database, dan server | Ya, khusus tim back-end |
| `feature/ML-Data` | Dataset, model, dan endpoint FastAPI | Ya, khusus tim ML |

## Cara Kerja Branch

```
feature/front-end ─┐
feature/back-end  ─┼──► integration/pandai ──► main
feature/ML-Data   ─┘
   (kerja harian)        (gabung & tes QA)    (versi final)
```

1. **Kerja di branch `feature/*` masing-masing.** Semua perubahan harian dilakukan di sini, bukan di `main`.
2. **Kalau subtask sudah jalan**, buat **Pull Request (PR)** dari `feature/*` ke `integration/pandai`.
3. **Di `integration/pandai`**, semua fitur digabung dan dites QA supaya front-end, back-end, dan ML nyambung.
4. **Kalau sudah lolos tes dan disetujui PO**, buat PR dari `integration/pandai` ke `main`.
5. **`main` hanya berisi versi yang sudah dites.** Jangan pernah ngoding langsung di `main`.

## Alur Status Jira

Board pakai Kanban. Status di Jira harus selalu sama dengan kondisi kode di Git.

| Status Jira | Kapan dipindah | Yang memindahkan |
|---|---|---|
| Backlog | Belum siap dikerjakan atau bukan cakupan MVP | PO |
| Ready | Subtask jelas dan siap diambil | PO |
| Dev In Progress | Mulai ngoding subtask di branch `feature/*` | Developer |
| Dev Done | PR ke `integration/pandai` sudah dibuat dan di-merge | Developer |
| Testing In Progress | QA mulai ngetes di `integration/pandai` | QA |
| Testing Done | Lolos tes. Kalau gagal, balikin ke Dev In Progress dan kasih komentar | QA |
| Review (UAT) | PO cek hasil sesuai acceptance criteria di Story | PO |
| Done | Sudah masuk `main` | PO |

Aturan board:
- Satu orang maksimal pegang **2 subtask** di Dev In Progress sekaligus.
- Ambil subtask dari kolom Ready, urutkan dari prioritas tertinggi.
- Kalau ke-block, kasih komentar di subtask dan tag orang yang terkait.

## Alur Kerja Harian

### 1. Pertama kali (clone)

```bash
git clone https://github.com/diptaz/PandAI.git
cd PandAI
```

### 2. Pindah ke branch kerja lo

```bash
git fetch
git switch feature/front-end     # ganti sesuai bagian lo
```

### 3. Ambil subtask di Jira

Pilih subtask lo di kolom **Ready**, pindahkan ke **Dev In Progress**, lalu catat key-nya (misal `KAN-37`).

### 4. Sebelum mulai ngoding, ambil update terbaru

```bash
git pull
```

### 5. Simpan pekerjaan (wajib cantumkan key Jira)

```bash
git add .
git commit -m "feat(KAN-37): tambah layar login dan register"
git push
```

### 6. Update branch lo dengan versi terbaru integration (biar gak conflict)

```bash
git fetch origin
git merge origin/integration/pandai
```

### 7. Buat Pull Request

Buka GitHub, pilih branch lo, klik **Compare & pull request**, set tujuan ke `integration/pandai`.

- Judul PR diawali key Jira, contoh: `KAN-37 Layar login dan register`
- Di deskripsi, tulis apa yang dikerjakan dan cara ngetesnya.
- Minta minimal satu anggota lain buat review, lalu pindahkan subtask ke **Dev Done** setelah di-merge.

## Aturan Commit Message

Format: `type(KAN-xx): deskripsi singkat`

| Type | Artinya | Contoh |
|---|---|---|
| `feat:` | Fitur baru | `feat(KAN-26): tambah endpoint prediksi durasi` |
| `fix:` | Perbaikan bug | `fix(KAN-32): jadwal tidak muncul saat slot kosong` |
| `docs:` | Dokumentasi | `docs: update README` |
| `data:` | Perubahan dataset/model | `data(KAN-25): tambah dataset durasi tugas` |
| `refactor:` | Rapikan kode tanpa ubah fungsi | `refactor(KAN-30): pisah komponen kartu tugas` |
| `test:` | Tambah atau ubah pengujian | `test(KAN-29): uji perhitungan skor prioritas` |

Key Jira boleh dikosongkan hanya untuk perubahan yang tidak terkait subtask, misalnya update README.

## Aturan Tim

- Jangan push langsung ke `main` dan `integration/pandai`.
- Setiap commit dan PR harus terhubung ke subtask Jira lewat key `KAN-xx`.
- Jangan ngoding fitur yang belum ada subtask-nya di Jira. Kalau perlu, minta PO bikin dulu.
- Satu orang mengerjakan satu bagian di branch-nya, supaya conflict minim.
- Selalu `git pull` sebelum mulai kerja.
- Commit kecil dan sering, jangan numpuk berhari-hari.
- Jangan commit `node_modules/`, file `.env`, atau API key.
- Kalau ada conflict, jangan panik: selesaikan di VS Code, lalu `git add .` dan `git commit`.

## Struktur Folder

```
PandAI/
├── src/                 # kode aplikasi Expo
├── assets/              # gambar dan ikon
├── scripts/             # script bantu
├── datasheet/           # dataset (data.csv)
├── machine-learning/    # notebook dan model ML (ml.ipynb)
├── app.json
├── package.json
└── README.md
```

## Menjalankan Aplikasi

```bash
npm install
npx expo start
```

Scan QR pakai **Expo Go**, atau tekan `a` buat emulator Android, `w` buat web.

Kalau error aneh:

```bash
npx expo start -c
```
