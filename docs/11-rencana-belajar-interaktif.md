# 11. Rencana modul belajar konversi interaktif

Status: **rencana disetujui; implementasi tersedia** pada
[`belajar/index.html`](../belajar/index.html). Pemilik proyek menyetujui implementasi
setelah dokumen rencana di-merge melalui PR #5. Dokumen ini mempertahankan rancangan
dan kriteria penerimaan sebagai acuan; panduan penggunaan ada di
[`belajar/README.md`](../belajar/README.md).

## 1. Tujuan dan hasil akhir

Membuat media belajar berbahasa Indonesia tentang **tekanan, gaya, panjang, dan
suhu** untuk pembaca berlatar computer science yang ingin mengingat fisika dasar.
Pembaca perlu memahami alasan memilih rumus, melihat pengaruh perubahan input,
dan mampu menyelesaikan soal sendiri.

Hasil implementasi yang diusulkan:

- `belajar/index.html`: satu file berisi HTML, CSS, JavaScript, dan ilustrasi SVG.
- Bisa dibuka langsung dari file, tanpa server, instalasi, API key, atau internet.
- Tampilan nyaman di laptop dan ponsel; semua fitur inti bekerja dengan keyboard.
- Empat modul, pengantar konversi, kuis gabungan, dan ringkasan rumus.
- Penjelasan ringkas di layar utama; penurunan rumus dan kaitan Python bisa dibuka.
- Setiap hasil hitungan disertai rumus, substitusi angka, langkah, dan satuan.

HTML dipilih agar hasil mudah disimpan, dibagikan, dan ditinjau melalui GitHub.
Penerbitan ke GitHub Pages atau pemindahan ke Claude Artifact menjadi pekerjaan
terpisah bila diminta; file lokal sudah menjadi hasil yang lengkap.

## 2. Batas materi dan acuan

Materi mengikuti pembahasan sebelumnya dan faktor dalam
[`converters/`](../converters/). Materi inti memakai satuan yang sudah dipelajari;
satuan tambahan versi GitHub tersedia dalam bagian **Lanjutan** agar pemula tidak
langsung menerima terlalu banyak pilihan.

| Modul | Satuan inti | Satuan lanjutan dari repository | Perantara hitungan |
|---|---|---|---|
| Tekanan | Pa, kPa, MPa, bar, atm, psi | mbar, Torr | Pa |
| Gaya | N, kN, kgf, lbf | dyne, kip | N |
| Panjang | mm, cm, m, km, in, ft, mi | nm, µm, yd, nmi | m |
| Suhu | °C, °F, K | °R (Rankine) | °C |

Label µm ditampilkan sebagai simbol; kunci `um` tetap digunakan ketika menjelaskan
kode repository. Celsius adalah perantara yang dipilih kode; **satuan dasar SI
untuk suhu termodinamik adalah kelvin**.

Pembahasan yang ikut masuk karena sudah dipelajari:

- Tekanan gauge dan absolut, dengan tekanan atmosfer sebagai input tersendiri.
- Gaya resultan, massa, percepatan, serta gaya berat dengan gravitasi yang dinyatakan.
- Luas, volume, dan tinggi gabungan kaki-inci sebagai pelengkap panjang.
- Perbedaan titik suhu dan perubahan suhu, serta batas nol mutlak.
- Hubungan tekanan, gaya, dan panjang melalui `P = F/A` dan definisi psi.

Simulasi pelengkap adalah fitur belajar baru dalam HTML. Konverter Python saat ini
tetap menjadi acuan konversi satuan; gauge–absolut dan konversi lintas dimensi belum
tersedia di aplikasi Streamlit. Implementasi HTML tidak mengubah API Python.

## 3. Cara menyampaikan materi

Setiap layar mengajarkan satu ide utama dengan urutan yang konsisten:

1. **Pahami:** definisi pendek dan contoh sehari-hari.
2. **Coba visualnya:** ubah slider atau input untuk melihat hubungan sebab-akibat.
3. **Kenali satuan:** arti simbol dan faktor ke satuan perantara.
4. **Ikuti contoh:** buka penyelesaian satu langkah demi satu langkah.
5. **Hitung sendiri:** masukkan nilai dan pilih satuan pada konverter.
6. **Uji pemahaman:** jawab kuis satu per satu dan baca pembahasannya.

Penjelasan utama sekitar 2–4 kalimat per ide. Definisikan simbol sebelum dipakai.
Gunakan kata "kali", "bagi", "geser titik nol", dan "satuan perantara" lebih dulu;
istilah teknis seperti offset diperkenalkan setelah contohnya.

Analogi CS digunakan seperlunya: konversi lewat satuan perantara mirip normalisasi
data ke satu format bersama. Analogi tidak menggantikan penjelasan fisikanya.

## 4. Navigasi dan tampilan

Navigasi utama: **Mulai · Tekanan · Gaya · Panjang · Suhu · Kuis gabungan · Rumus**.
Urutan awal mempertahankan urutan pembelajaran sebelumnya. Semua modul dapat dibuka
langsung tanpa harus lulus modul lain.

Pada laptop, panel penjelasan dan visual berdampingan jika ruang cukup. Pada
ponsel, urutannya penjelasan, kontrol, visual, lalu langkah hitung. Navigasi tetap
terbaca tanpa memaksa satu baris yang terlalu lebar.

Keputusan tampilan yang diusulkan:

- Latar terang, teks gelap, dan satu warna aksen berbeda untuk setiap topik.
- Rumus memakai ukuran yang nyaman dibaca dan baris terpisah untuk setiap langkah.
- Angka, satuan, dan teks menjelaskan hasil; warna bukan satu-satunya penanda.
- Animasi pendek hanya untuk membantu memahami perubahan; hormati pengaturan
  pengurangan gerak dan sediakan tombol jeda untuk animasi yang berjalan terus.
- Tombol konsisten: **Langkah berikutnya**, **Tampilkan semua**, **Coba sendiri**,
  **Petunjuk**, **Periksa jawaban**, dan **Ulangi**.

## 5. Pengantar: satu besaran, beberapa cara menulis

Tujuan: memahami bahwa mengganti satuan tidak mengubah besaran yang diukur.

- Visual satu batang yang sama dengan skala m, cm, dan in yang dapat diganti.
- Contoh `1 m = 100 cm`: batang tetap sama panjang, jumlah unit berubah.
- Peta interaktif `satuan asal → satuan perantara → satuan tujuan`.
- Makna faktor: "1 satuan ini sama dengan berapa satuan perantara?"
- Rumus konversi linear: `hasil = nilai × faktor asal ÷ faktor tujuan`.
- Prediksi sebelum menghitung: untuk nilai positif, satuan tujuan lebih besar
  berarti angka lebih kecil. Suhu bertitik nol berbeda dibahas dengan aturan sendiri.

## 6. Modul tekanan

**Konsep inti:** tekanan adalah gaya normal per luas bidang, `P = F/A`.
Jelaskan `P` dalam Pa, `F` dalam N, `A` dalam m², dan `1 Pa = 1 N/m²`.

**Visual A — gaya dan luas:** balok menekan bidang. Pengguna mengubah gaya dan
luas kontak; panah, luas bidang, dan angka tekanan ikut berubah. Dua preset memakai
gaya sama dengan luas berbeda agar pengaruh luas mudah dibandingkan. Luas harus
lebih besar dari nol.

**Visual B — gauge dan absolut:** batang tersusun menunjukkan bagian tekanan
atmosfer dan bagian tekanan gauge untuk contoh gauge positif. Input gauge negatif
yang masih menghasilkan tekanan absolut nonnegatif ditampilkan sebagai selisih
terhadap garis atmosfer, bukan sebagai batang dengan panjang negatif.

**Isi penjelasan:**

- Perbedaan Pa, kPa, MPa, bar, atm, dan psi serta konteks pemakaiannya.
- `1 atm = 101.325 Pa` adalah atmosfer standar; atmosfer lokal dapat berbeda.
- Mengapa `1 atm` dan `1 bar` dekat tetapi tidak sama.
- Asal psi dari `lbf/in²`, termasuk menguadratkan konversi inci ke meter.
- `P absolut = P gauge + P atmosfer`; samakan satuan sebelum menjumlahkan.
- mmHg dikenalkan sebagai konteks tambahan. Jangan menyamakan definisinya dengan
  Torr secara eksak; bila memakai pendekatan, tampilkan tanda `≈`.

**Contoh bertahap:** `500 N / 0,25 m²`, `250 kPa → bar`, `2 atm → psi`, serta
`32 psi gauge → bar absolut` dengan atmosfer `1 atm`. Contoh terakhir juga menegaskan
angka atmosfer yang pernah tertukar: `1 atm = 1,01325 bar`.

## 7. Modul gaya

**Konsep inti:** dorongan atau tarikan; dalam contoh massa tetap, gaya resultan
memenuhi `F = m × a`. Bedakan gaya resultan dari salah satu gaya pada benda.

**Visual A — gaya dan percepatan:** balok dengan panah gaya. Pengguna mengubah massa
dan gaya resultan lalu melihat percepatan. Model dinyatakan satu dimensi dengan
massa tetap dan tanpa gaya gesek tambahan. Gerak, jika dianimasikan, dimulai dari
keadaan diam dan memiliki tombol jalankan serta reset.

**Visual B — massa dan berat:** bandingkan benda bermassa sama pada gravitasi Bumi
standar dan Bulan (pendekatan). Massa tetap, panah gaya berat berubah. Nilai `g`
terlihat dan dapat diedit; tidak menyamakan semua lokasi di Bumi dengan gravitasi
standar.

**Isi penjelasan:**

- Arti N, kN, kgf, dan lbf; asal `1 N = 1 kg·m/s²`.
- `kg` menyatakan massa; `kgf` menyatakan gaya.
- Definisi kgf memakai gravitasi standar `9,80665 m/s²`, sehingga faktor kgf tetap.
- Menghitung berat dengan `W = m × g` membutuhkan nilai gravitasi; ini berbeda
  dari mengganti satuan gaya.

**Contoh bertahap:** `m = 2 kg, a = 3 m/s²`, `5 kgf → N`, `500 lbf → kN`, dan
gaya berat massa `70 kg` pada dua nilai gravitasi.

## 8. Modul panjang

**Konsep inti:** jarak antara dua titik; awalan metrik dan hubungan inci-kaki-mil.

**Visual A — penggaris ganda:** satu panjang ditunjukkan dalam cm dan in secara
bersamaan. Rentang visual menyesuaikan nilai dan menampilkan skala. Untuk jarak
sangat besar atau sangat kecil, tampilkan diagram berskala dengan label; ukuran
di layar tidak diklaim sebagai ukuran fisik sebenarnya.

**Visual B — panjang, luas, volume:** persegi dan kubus menunjukkan faktor yang
dipakai satu, dua, atau tiga kali. Gambar bersifat skematis; tidak menggambar satu
juta elemen ketika menjelaskan volume.

**Isi penjelasan:**

- Awalan milli, centi, dan kilo; faktor cm adalah `0,01 m`, bukan `100 m`.
- `1 in = 2,54 cm` tepat, `1 ft = 12 in`, dan `1 mi = 5.280 ft`.
- Luas memakai kuadrat faktor; volume memakai kubik faktor.
- Tinggi `5 ft 10 in` adalah dua komponen; bukan `5,10 ft`.

**Contoh bertahap:** `250 cm → m`, `5 ft → cm`, `100 mi → km`, tinggi
`5 ft 10 in → cm`, serta `2 m² → cm²` dan `1 m³ → cm³` sebagai pelengkap.

## 9. Modul suhu

**Konsep inti:** skala suhu dapat memiliki ukuran interval dan titik nol berbeda.
Hindari definisi universal "suhu adalah kecepatan partikel". Gerak termal menjadi
ilustrasi sederhana, terutama pada gas; kalor dijelaskan sebagai energi yang
berpindah akibat perbedaan suhu, bukan sesuatu yang disimpan sebagai "panas".

**Visual A — tiga termometer:** penanda suhu yang sama bergerak serempak pada
skala °C, °F, dan K. Tampilkan titik beku/didih air sebagai acuan sekitar tekanan
1 atm; jelaskan bahwa titik didih bergantung pada tekanan.

**Visual B — titik dan selisih:** pengguna mengganti mode **Suhu** dan **Perubahan
suhu**. Dua penanda memperlihatkan bahwa kenaikan 10 °C setara kenaikan 18 °F,
sedangkan titik suhu 10 °C setara 50 °F.

**Isi penjelasan:**

- Turunkan rasio `180/100 = 9/5` dari rentang skala acuan.
- `F = C × 9/5 + 32` dan `C = (F − 32) × 5/9`.
- `K = C + 273,15`; simbol K tidak memakai tanda derajat.
- Konversi lintas pasangan lewat Celsius dengan urutan operasi yang terlihat.
- Perubahan suhu hanya memakai rasio; tidak menambah atau mengurangi offset.
- Batas nol mutlak berlaku pada titik suhu dalam model termodinamika pengantar.
  Perubahan suhu negatif tetap sah: artinya suhu turun.

**Contoh bertahap:** `25 °C → °F`, `98,6 °F → °C`, `300 K → °F`,
`0 K → °F`, dan kenaikan `10 °C → °F`. Rankine tersedia di bagian Lanjutan dan
diberi label lengkap agar tidak tertukar dengan Réaumur.

## 10. Standar langkah hitung untuk seluruh fitur

Satu format digunakan oleh contoh, konverter bebas, simulasi konsep, dan pembahasan
kuis. Setiap langkah dihitung dari input aktif, bukan teks contoh yang tidak berubah.

1. **Diketahui dan ditanya:** nilai, satuan asal, satuan tujuan, serta konteks.
2. **Rumus:** persamaan simbolik dan arti faktor/variabel yang dipakai.
3. **Substitusi:** masukkan angka lengkap dengan satuannya.
4. **Hitungan antara:** tunjukkan urutan operasi dan nilai perantara.
5. **Hasil akhir:** angka, satuan, serta penanda pembulatan jika diperlukan.
6. **Cek masuk akal:** kaitkan arah perubahan dengan konsep.

Contoh tampilan untuk `5 ft → cm`:

```text
Diketahui: 5 ft. Ditanya: panjang dalam cm.
Faktor asal: 1 ft = 0,3048 m. Faktor tujuan: 1 cm = 0,01 m.
Rumus: hasil = nilai × faktor asal ÷ faktor tujuan.
Langkah 1: 5 ft × (0,3048 m/ft) = 1,524 m.
Langkah 2: 1,524 m ÷ (0,01 m/cm) = 152,4 cm.
Cek: cm lebih kecil dari ft; untuk panjang positif yang sama, angkanya membesar.
```

Contoh tampilan untuk `300 K → °F`:

```text
Langkah 1: C = K − 273,15 = 300 − 273,15 = 26,85 °C.
Langkah 2: F = C × 9/5 + 32.
           F = 26,85 × 1,8 + 32 = 48,33 + 32 = 80,33 °F.
```

Pada contoh terarah, langkah dibuka satu per satu. Pada konverter bebas, semua
langkah tampil langsung agar hasil mudah diperiksa. Faktor tidak dibulatkan
sebelum perhitungan selesai; tanda `≈` dipakai jika angka tampilan dibulatkan.

## 11. Contoh soal dan kuis

Target isi awal: **minimal 4 contoh terbahas dan 10 soal kuis per modul**, ditambah
**12 soal gabungan**. Total minimal 16 contoh dan 52 soal. Variasi contoh pelengkap
di atas dapat menambah jumlah contoh tanpa mengurangi target inti.

Komposisi setiap kuis modul:

- 3 soal konsep/prediksi, misalnya pengaruh luas terhadap tekanan.
- 4 soal hitungan langsung dan konversi satuan.
- 2 soal jebakan umum, misalnya kg vs kgf atau offset perubahan suhu.
- 1 soal gabungan dengan beberapa langkah.

Perilaku kuis:

1. Satu soal ditampilkan pada satu waktu; tingkat kesulitan naik bertahap.
2. Soal konsep memakai pilihan jawaban; soal hitungan memakai angka dan satuan
   terpilih atau satuan target yang sudah jelas tercantum.
3. Tombol **Petunjuk** memberi arah rumus sebelum membuka hasil.
4. **Periksa jawaban** memberi umpan balik spesifik. Jika salah, pengguna dapat
   mencoba lagi atau membuka **Pembahasan**.
5. Pembahasan hitungan selalu memuat langkah lengkap; soal konsep menjelaskan
   alasan pilihan benar dan kekeliruan yang ditargetkan.
6. Jawaban pertama dicatat terpisah dari keberhasilan setelah bantuan. Mengulang
   tombol periksa tidak menambah skor; soal yang dibuka jawabannya diberi penanda.
7. Ringkasan menampilkan hasil per topik dan tautan untuk mengulang soal yang salah.

Toleransi jawaban ditentukan per soal berdasarkan presisi yang diminta. Untuk soal
dua desimal, jawaban yang membulat ke nilai dua desimal yang benar diterima, dengan
pengaman kecil untuk floating point. Soal yang meminta nilai eksak memakai toleransi
numerik ketat. Jawaban kosong atau format tidak valid tidak dihitung sebagai salah.

## 12. Angka, validasi, dan progres

- Tampilan memakai format Indonesia, misalnya `1.013,25`.
- Input tanpa pemisah ribuan menerima koma atau titik desimal: `1,5` dan `1.5`.
  Beri contoh tepat di input. Jangan menebak string ambigu atau campuran pemisah;
  minta pengguna memasukkan ulang tanpa pemisah ribuan.
- Tolak input kosong, nilai nonnumerik, NaN, tak hingga, dan hasil yang melampaui
  rentang numerik. Tampilkan pesan dekat input terkait.
- Massa dan luas pada simulasi harus positif; panjang/besar gaya pada simulasi
  memakai rentang nonnegatif. Jangan menyimpulkan bahwa gaya bertanda atau tekanan
  gauge negatif selalu tidak sah secara fisika.
- Konverter satuan mempertahankan aturan numerik Python yang relevan; pembatasan
  konteks diterapkan pada simulasi yang memerlukannya.
- Nol mutlak memakai toleransi sejalan dengan Python untuk titik suhu.
- Simpan progres per modul dan ringkasan kuis di `localStorage` dengan versi data.
  Jika penyimpanan diblokir, mode belajar tetap berjalan selama halaman terbuka.
- Sediakan **Reset progres** dengan konfirmasi; jelaskan penyimpanan lokal tidak
  menyinkronkan perangkat dan dapat berbeda antarbrowser ketika dibuka dari file.
- Semua perubahan nilai, status benar/salah, dan pesan error tersedia sebagai teks
  yang dapat dibaca teknologi bantu.

## 13. Rancangan teknis implementasi

Gunakan JavaScript biasa dan SVG sebaris tanpa library atau CDN. Pemisahan tanggung
jawab di dalam satu file:

| Bagian | Tanggung jawab |
|---|---|
| Data materi | Definisi, faktor, contoh, kuis, penjelasan kesalahan umum |
| Perhitungan | Konversi linear, suhu, perubahan suhu, dan simulasi konsep |
| Langkah hitung | Menghasilkan urutan rumus, substitusi, nilai antara, dan hasil |
| Presentasi | Navigasi, kontrol, SVG, tampilan rumus, umpan balik kuis |
| Progres | Status pelajaran, jawaban, penyimpanan lokal dan reset |

Fungsi perhitungan mengembalikan hasil dan data langkah yang memakai nilai antara
yang sama. Tampilan tidak menghitung ulang dengan faktor berbeda. Data contoh dan
kuis memakai fungsi yang sama untuk menghasilkan pembahasan, lalu diverifikasi
terhadap hasil acuan yang ditetapkan secara independen.

Bagian opsional **Kaitkan dengan Python** menyorot dictionary faktor, dua langkah
lewat perantara, dan penanganan suhu pada file repository. Jangan menyiratkan bahwa
percabangan `if/elif` adalah satu-satunya cara menerapkan konversi suhu.

## 14. Urutan pengerjaan setelah rencana disetujui

| Tahap | Pekerjaan | Bukti selesai |
|---|---|---|
| 1. Audit isi | Verifikasi definisi, faktor, rumus, contoh dan soal; catat rujukan satuan primer | Daftar isi dan hasil acuan, termasuk koreksi penyederhanaan materi lama |
| 2. Fondasi | Buat file HTML, navigasi, gaya responsif, model data dan fungsi hitung | File terbuka langsung; perhitungan dasar dan langkahnya sesuai acuan |
| 3. Tekanan | Bangun satu modul lengkap dari konsep sampai kuis | Slider, konverter, contoh dan kuis tekanan saling konsisten |
| 4. Tiga modul lain | Terapkan pola yang sama pada gaya, panjang, suhu | Empat modul lengkap dan kasus khusus bekerja |
| 5. Integrasi | Kuis gabungan, ringkasan rumus, progres, lanjutan, kaitan Python | Navigasi lintas modul dan penyimpanan/reset dapat dicoba |
| 6. Verifikasi | Uji angka, langkah, interaksi, aksesibilitas, offline dan regresi | Catatan hasil pemeriksaan dan batas pengujian yang nyata |
| 7. GitHub | README cara membuka HTML, commit, push, PR, CI dan merge sesuai instruksi | HTML dan dokumentasi tersedia pada branch utama |

Pekerjaan dapat dilakukan oleh satu lead; tidak memerlukan worker. Jika kemudian
dibutuhkan worker, brief dan persetujuan operator harus didapat sebelum memulainya.

## 15. Pemeriksaan penerimaan

Nilai acuan berikut adalah sampel pemeriksaan; bukan batas seluruh cakupan uji.

| Kasus | Hasil yang diharapkan |
|---|---|
| 500 N pada 0,25 m² | 2.000 Pa |
| 250 kPa → bar | 2,5 bar |
| 1 atm → bar | 1,01325 bar |
| 32 psi gauge + atmosfer 1 atm → bar absolut | ≈ 3,2195723338 bar |
| 2 kg × 3 m/s² | 6 N |
| 1 kgf → N | 9,80665 N |
| 500 lbf → kN | ≈ 2,2241108076 kN |
| 5 ft → cm | 152,4 cm |
| 100 mi → km | 160,9344 km |
| 5 ft 10 in → cm | 177,8 cm |
| 2 m² → cm² | 20.000 cm² |
| 1 m³ → cm³ | 1.000.000 cm³ |
| 25 °C → °F | 77 °F |
| 98,6 °F → °C | 37 °C |
| 300 K → °F | 80,33 °F |
| −40 °C → °F | −40 °F |
| 0 K → °F | −459,67 °F |
| Kenaikan 10 °C → perubahan °F | 18 °F |
| Penurunan 10 °C → perubahan °F | −18 °F |
| Titik suhu −300 °C | Ditolak sebagai di bawah nol mutlak |

Pemeriksaan implementasi juga mencakup:

- Seluruh pasangan satuan inti dan lanjutan dibandingkan dengan konverter Python;
  uji satuan sama, nilai nol, dan konversi bolak-balik dengan toleransi numerik.
- Setiap hasil dan langkah antara konsisten, termasuk ketika input/unit berubah.
- Seluruh kunci kuis dan contoh diperiksa; kesalahan jawaban, bantuan, pengulangan,
  skor, dan reset tidak membuat progres terhitung dua kali.
- Input tidak valid, pembagian nol, batas suhu, hasil terlalu besar, dan kegagalan
  penyimpanan tidak merusak halaman.
- File lokal bekerja tanpa request jaringan dan tanpa error JavaScript.
- Tampilan diuji setidaknya pada lebar 360, 768, dan 1280 piksel; kontrol dapat
  dipakai melalui keyboard, fokus terlihat, dan rumus panjang tidak memotong halaman.
- Pengurangan gerak dan teks alternatif diagram berfungsi; SVG informatif memiliki
  judul/deskripsi dan nilai hitungan tersedia sebagai teks.
- Jalankan pemeriksaan repository `python scripts/check.py` dan `git diff --check`.
  Jika pengujian browser atau lint JavaScript membutuhkan alat tambahan, periksa
  alat yang tersedia dahulu dan minta persetujuan sebelum menambah dependensi.

## 16. Tahap GitHub untuk dokumen rencana ini

1. Mulai dari `main` yang sinkron dengan `origin/main` dan periksa perubahan lokal.
2. Buat branch `docs/interactive-learning-plan`.
3. Tambahkan dokumen ini dan tautan dari README; tinjau diff dan hitungan contoh.
4. Jalankan pemeriksaan repository yang tersedia serta `git diff --check`.
5. Commit dengan Conventional Commit berbahasa Inggris, lalu push branch.
6. Buat PR yang menjelaskan bahwa perubahan hanya rencana, bukan HTML yang selesai.
7. Tunggu CI dan review yang diwajibkan, lalu merge tanpa melewati aturan repository.
8. Sinkronkan `main` lokal dan laporkan tautan PR, commit merge, serta pemeriksaan.

**Catatan pelaksanaan:** tahap dokumen rencana di atas telah selesai. Implementasi
yang disetujui menyediakan empat modul, 23 contoh terbahas, dan 52 soal. Pekerjaan
dibagi menjadi commit kecil berdasarkan fondasi, mesin hitung, modul, kuis, perbaikan,
pengujian, dan dokumentasi. Gunakan kriteria penerimaan di bagian 15 untuk memeriksa
perubahan berikutnya.
