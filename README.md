# PandAI

Our Member :
1. 2902726403 - Aldridge Hansel Robin
2. 2902726422 - Bernardus Allan Fisthiantara
3. 2902726492 - Friska Deviana
4. 2902726555 - I Gede Wahyu Dipta Pariandika
5. 2902726675 - Maulidan Fazri

---

## Tentang Project

PandAI adalah aplikasi mobile berbasis **Expo (React Native)** yang didukung komponen **Machine Learning** dan **Back-End**. Project ini dikerjakan secara kelompok, jadi semua anggota wajib mengikuti alur branch di bawah supaya kodenya gak saling bentrok.

## Struktur Branch

| Branch | Fungsi | Boleh push langsung? |
|---|---|---|
| `main` | Versi final yang stabil dan siap dikumpulkan/didemokan | Tidak |
| `integration/pandai` | Tempat menggabungkan semua fitur dan ngetes bareng | Tidak, lewat Pull Request |
| `feature/front-end` | Tampilan dan logika aplikasi (Expo / React Native) | Ya, khusus tim front-end |
| `feature/back-end` | API, database, dan server | Ya, khusus tim back-end |
| `feature/ML-Data` | Dataset dan model Machine Learning | Ya, khusus tim ML |

## Cara Kerja Branch

```
feature/front-end ─┐
feature/back-end  ─┼──► integration/pandai ──► main
feature/ML-Data   ─┘
   (kerja harian)        (gabung & tes)      (versi final)
```

1. **Kerja di branch `feature/*` masing-masing.** Semua perubahan harian dilakukan di sini, bukan di `main`.
2. **Kalau fitur sudah jalan**, buat **Pull Request (PR)** dari `feature/*` ke `integration/pandai`.
3. **Di `integration/pandai`**, semua fitur digabung dan dites supaya front-end, back-end, dan ML nyambung.
4. **Kalau sudah stabil**, buat PR dari `integration/pandai` ke `main`.
5. **`main` hanya berisi versi yang sudah dites.** Jangan pernah ngoding langsung di `main`.

## Alur Kerja Harian

### 1. Pertama kali (clone)

```bash
git clone https://github.com/MaulidanFazri/PandAI.git
cd PandAI
```

### 2. Pindah ke branch kerja lo

```bash
git fetch
git switch feature/front-end     # ganti sesuai bagian lo
```

### 3. Sebelum mulai ngoding, ambil update terbaru

```bash
git pull
```

### 4. Simpan pekerjaan

```bash
git add .
git commit -m "feat: tambah halaman login"
git push
```

### 5. Update branch lo dengan versi terbaru integration (biar gak conflict)

```bash
git fetch origin
git merge origin/integration/pandai
```

### 6. Buat Pull Request

Buka GitHub, pilih branch lo, klik **Compare & pull request**, set tujuan ke `integration/pandai`, lalu minta anggota lain buat review.

## Aturan Commit Message

Pakai awalan supaya riwayatnya rapi:

| Awalan | Artinya | Contoh |
|---|---|---|
| `feat:` | Fitur baru | `feat: tambah endpoint prediksi` |
| `fix:` | Perbaikan bug | `fix: crash saat buka kamera` |
| `docs:` | Dokumentasi | `docs: update README` |
| `data:` | Perubahan dataset/model | `data: tambah data.csv` |
| `refactor:` | Rapikan kode tanpa ubah fungsi | `refactor: pisah komponen header` |

## Aturan Tim

- Jangan push langsung ke `main` dan `integration/pandai`.
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