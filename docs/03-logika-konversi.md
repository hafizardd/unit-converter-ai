# 3. Konversi melalui satuan dasar

Setiap faktor berarti **satu satuan ini sama dengan berapa satuan dasar**.
Tekanan memakai Pa. `"bar": 100000` berarti 1 bar = 100000 Pa.
Untuk 2 bar → kPa: `2 * 100000 = 200000 Pa`, lalu `200000 / 1000 = 200 kPa`.

Rumus umum: `value * factor_from / factor_to`. Panjang memakai hub m dan gaya N.
Jangan membalik faktor. Dictionary cukup satu untuk banyak pasangan satuan.

| Kasus | Hasil acuan |
|---|---|
| 1 Pa → bar | 0.00001 bar |
| 1 atm → Pa | 101325 Pa |
| 1 in → cm | 2.54 cm |
| 1 nmi → m | 1852 m |
| 1 kgf → N | 9.80665 N |
| 0 C → K | 273.15 K |
| -40 C → F | -40 F |
| 0 R → K | 0 K |

Suhu punya titik nol berbeda. Lewati Celsius: F → C memakai `(value - 32) * 5 / 9`,
K → C memakai `value - 273.15`, R → C memakai `value * 5 / 9 - 273.15`.
Dari Celsius ke tujuan gunakan rumus kebalikannya.

Suhu di bawah 0 K ditolak. Toleransi `1e-9` mengatasi selisih pembulatan float
yang sangat kecil. Sebagian pecahan tidak tersimpan tepat sebagai float, maka test
memakai toleransi. Tampilan `.12g` menjaga hasil kecil terlihat; `.4f` membuat
0.00001 menjadi 0.0000.

Validasi berada di `converters/base.py`, rumus di empat modul, kategori di
`converters/__init__.py`. UI dan tool AI memanggil `convert_unit` yang sama.
Tidak ada rumus lain khusus chatbot.

Nilai negatif kategori linear diperbolehkan sebagai aritmetika bertanda. Aplikasi
tidak menafsirkan gauge/absolute. kg adalah massa, kgf adalah gaya. Konversi suhu
di sini untuk nilai suhu, bukan selisih suhu.

**Latihan:** hitung 3 ft → cm. Jawaban: 91.44 cm.
