# Belajar konversi satuan secara interaktif

Buka [index.html](index.html) dengan browser setelah mengunduh file atau clone
repository. Pada Windows, klik dua kali file tersebut. File berdiri sendiri: CSS,
JavaScript, ilustrasi, contoh, dan kuis ada di dalamnya. Tidak perlu menjalankan
Streamlit, memasang Python, menyiapkan key, atau mengakses internet.

## Cara belajar

1. Mulai dari **Mulai** untuk memahami satuan dan metode perantara.
2. Pilih **Tekanan**, **Gaya**, **Panjang**, atau **Suhu**. Urutan tidak dikunci.
3. Baca **Pahami**, lalu ubah slider atau nilai pada visual. Rumus dan langkahnya
   mengikuti input. Gunakan tombol bagian untuk berpindah cepat.
4. Pada contoh, buka langkah dengan **Langkah berikutnya** atau **Tampilkan semua**.
5. Coba **Hitung sendiri** untuk pasangan satuan dan nilai pilihanmu. **Sertakan
   satuan lanjutan** membuka satuan tambahan yang tersedia pada konverter Python.
6. Kerjakan kuis satu per satu. Gunakan **Petunjuk**, **Pembahasan**, atau **Ulangi**
   jika perlu. Pembahasan hitungan selalu memuat enam bagian penyelesaian.
7. Tandai materi yang sudah dipelajari dan buka **Kuis gabungan** untuk rekap.
   **Rumus** menyediakan pegangan cepat.

## Isi

| Topik | Visual dan latihan | Contoh terbahas | Soal |
|---|---|---:|---:|
| Tekanan | Gaya–luas dan gauge–absolut | 5, termasuk asal psi | 10 |
| Gaya | Gerak dari diam, massa dan gaya berat | 7, termasuk asal kgf/lbf | 10 |
| Panjang | Penggaris cm/in, luas/volume, kaki–inci | 6 | 10 |
| Suhu | Termometer C/F/K, titik vs perubahan | 5 | 10 |
| Gabungan | Soal lintas empat topik, catatan jawaban terpisah | — | 12 |

Setiap hitungan menampilkan diketahui/ditanya, rumus, substitusi, hitungan antara,
hasil dengan satuan, dan cek masuk akal. Faktor tidak dibulatkan sebelum hasil akhir;
tanda `≈` menunjukkan angka tampilan yang dibulatkan.

## Input angka dan penilaian

- Tulis desimal dengan koma atau titik: `1,5` atau `1.5`.
- Jangan memakai pemisah ribuan. Untuk seribu tulis `1000` atau `1e3`; `1.000`
  dianggap ambigu dan diminta diperbaiki. `0,001` dan `0.001` tetap diterima.
- Hasil ditampilkan dengan format Indonesia, misalnya `1.013,25`.
- Satuan jawaban kuis ditentukan soal dan tampil di samping kolom jawaban. Masukkan
  angka saja. Ikuti permintaan jumlah desimal; angka lebih teliti juga diterima
  bila pembulatannya sesuai. Soal eksak memakai toleransi floating point kecil.
- Jawaban pertama tanpa bantuan dipisahkan dari jawaban benar setelah petunjuk,
  pembahasan, atau percobaan ulang. Memeriksa ulang tidak menambah jumlah soal benar.
- Jawaban kosong dan format tidak valid tidak dihitung sebagai jawaban salah.

## Progres dan batas model

Progres disimpan dalam `localStorage` browser. Tidak ada akun atau sinkronisasi
antarperangkat. Penyimpanan file lokal bergantung pada browser dan lokasi file.
Jika penyimpanan ditolak, fitur tetap bekerja dengan progres selama halaman terbuka.
**Reset semua progres** meminta konfirmasi sebelum menghapus catatan belajar.

Gambar bersifat skematis. Penggaris di layar bukan penggaris ukuran fisik sebenarnya.
Gerak memakai massa tetap, gaya resultan satu dimensi, tanpa gesekan, dan mulai dari
diam. Gravitasi Bumi memakai nilai standar; gravitasi lokal dapat berbeda. Gravitasi
Bulan adalah pendekatan. Titik beku/didih air memakai acuan sekitar 1 atm. Perubahan
suhu berbeda dari titik suhu dan tidak memakai offset.

Input simulasi memiliki batas konteks tersendiri, misalnya luas/massa harus positif.
Gaya bertanda dan gauge negatif tidak otomatis salah secara fisika. Konversi satuan
dan hasil memakai floating point; nilai yang melampaui rentang numerik ditolak.

## Verifikasi pengembang

Jalankan dari root repository, dengan dependency pengembangan Python dan Node.js 24:

```text
python scripts/check.py
python scripts/check_learning_browser.py
git diff --check
```

Pemeriksaan pertama menguji format, lint, serta pytest. Mesin JavaScript dibandingkan
dengan semua pasangan satuan Python, termasuk nilai nol, negatif, satuan lanjutan,
dan kasus batas suhu. Kunci kuis diverifikasi dengan nilai acuan terpisah.

Pemeriksaan browser memakai Edge/Chromium yang sudah terpasang; dapat memilih lokasi
dengan `--browser PATH`. File uji sementara dan profil browser terpisah dipakai
tanpa server. Pengujian mencakup tujuh halaman, 23 contoh, 52 soal, input invalid,
slider, pertukaran satuan, mode perubahan suhu, serta lebar 360/768/1280 piksel.
Ini pemeriksaan otomatis terarah, bukan audit aksesibilitas formal semua browser.

Faktor satuan mengikuti [`converters/`](../converters/); rujukan utama tersedia pada
[sumber resmi](../docs/10-sumber.md). Rancangan dan kriteria penerimaan ada pada
[rencana implementasi](../docs/11-rencana-belajar-interaktif.md).
