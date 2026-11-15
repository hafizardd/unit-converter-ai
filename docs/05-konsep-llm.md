# 5. Mengenal AI dan LLM

AI adalah istilah luas untuk sistem dengan kemampuan yang kita kaitkan dengan
kecerdasan. Machine learning belajar pola dari data; deep learning memakai jaringan
saraf berlapis. LLM adalah model bahasa besar dalam keluarga ini.

Model memproses teks sebagai token, potongan yang tidak selalu sama dengan satu
kata. Analogi: saat mendengar “Ibu pergi ke …”, kita bisa menebak kelanjutannya.
LLM menghasilkan token berikutnya berdasarkan pola yang dipelajari dan konteks.
Analogi ini pengantar, bukan uraian lengkap semua kemampuan model.

Teks yang masuk akal dapat tetap salah. Model bisa keliru menghitung, memilih
satuan, atau menyatakan informasi dengan yakin. Karena itu fungsi Python menjadi
sumber perhitungan, sedangkan model membantu menjelaskan.

Percakapan API memakai pesan dengan role:

```python
messages = [
    {"role": "system", "content": "Kamu tutor konversi satuan."},
    {"role": "user", "content": "Bagaimana mengubah 1 Pa menjadi bar?"},
]
```

`system` memberi arahan, `user` bertanya, `assistant` berisi jawaban model. Pada
API chat yang dipakai proyek ini, aplikasi mengirim ulang riwayat yang ingin
disertakan. Model tidak menyimpan ingatan sesi aplikasi kita secara otomatis.

Prompt adalah instruksi; konteks adalah informasi yang tersedia saat menjawab.
Versi workshop menyisipkan tabel faktor statis. Itu belum merupakan RAG lengkap:
tidak ada pengambilan dokumen berdasarkan pertanyaan. Versi repo menawarkan tool
konversi yang dapat diminta model dan dijalankan aplikasi.

API menghubungkan aplikasi lokal dengan layanan Groq. Key mengizinkan akses dan
terkait kuota organisasi. Jangan menaruhnya di kode atau mengunggahnya ke GitHub.
`temperature=0.2` adalah parameter variasi keluaran, tidak berkaitan dengan suhu
fisik di tab konverter. Nilai rendah tidak menjamin jawaban benar.

## Contoh tersimpan saat koneksi tidak tersedia

Ini **contoh ilustratif**, bukan bukti panggilan API berhasil:

Pengguna: “Bagaimana mengubah 1 Pa menjadi bar?”

Contoh jawaban: “1 bar = 100000 Pa. Dari Pa ke bar, bagi dengan 100000.
Jadi 1 Pa = 0.00001 bar.”

Tanyakan ke peserta: bagian mana yang berupa rumus, angka, dan penjelasan?
Bagian mana yang harus diperiksa bila model membuat kesalahan?
