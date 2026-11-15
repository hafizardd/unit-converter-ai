# 1. Setup: dari folder ke aplikasi

Proyek adalah folder berisi file terkait. Repo mencatat riwayatnya menggunakan Git.
Untuk menjalankan contoh, kamu boleh memilih **Code → Download ZIP** di GitHub,
lalu mengekstraknya; belum perlu menguasai Git.

Pasang Python 3.12 dan VS Code. Windows: centang **Add Python to PATH**. Buka
folder yang langsung berisi `requirements.txt` lewat **File → Open Folder**,
lalu **Terminal → New Terminal**. Terminal menjalankan perintah; editor menulis file.
Jangan menulis `pip install` di file `.py` atau di jendela bertanda `>>>`.

Ikuti perintah Windows/Linux dalam [README](../README.md#jalankan). `venv` adalah
tempat terpisah bagi library proyek. `python -m pip` menggunakan Python yang sedang
dipilih. `requirements.txt` adalah daftar alat dan versi yang perlu dipasang.

Ubuntu: jika `ensurepip` tidak tersedia, pasang `python3-venv` yang sesuai versi
Python melalui apt. Jangan memakai `sudo pip install`. Windows: jika aktivasi
diblokir, gunakan `.venv\Scripts\python.exe` langsung, sesuai README.

Salin `.env.example` menjadi `.env` sekali dan isi key secara privat. File titik
bisa tersembunyi; file manager Linux umumnya memakai Ctrl+H untuk menampilkannya.
Pastikan nama bukan `.env.txt`. Jangan menimpa `.env` yang sudah terisi.

`python -m streamlit run app.py` menyalakan server. Buka alamat dari terminal.
Terminal harus tetap menyala; Ctrl+C menghentikannya. Saat membuka proyek lagi,
aktifkan venv dan jalankan aplikasi; tidak perlu memasang ulang semua library.

| Error | Pemeriksaan pertama |
|---|---|
| File tidak ditemukan | Terminal sudah di folder yang benar? |
| ModuleNotFoundError | Python berasal dari `.venv`? |
| SyntaxError | Kutip, titik dua, kurung, dan nomor baris |
| IndentationError | Isi fungsi memakai empat spasi konsisten |
| Port terpakai | Hentikan server lama atau tambah `--server.port 8502` |

**Coba:** jalankan tanpa key. Konverter tetap berfungsi; pertanyaan chat terkait
satuan akan menghasilkan pesan konfigurasi.
