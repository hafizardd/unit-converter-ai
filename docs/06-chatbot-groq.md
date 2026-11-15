# 6. Menghubungkan Groq

Groq adalah layanan yang menjalankan model untuk aplikasi kita. Model default
`openai/gpt-oss-20b` dipanggil melalui SDK **Groq**, menggunakan key Groq; kamu
tidak perlu memasang SDK OpenAI atau membuat key OpenAI.

Daftar model dan kuota bisa berubah. Default dipilih dari pengganti resmi Groq
untuk Llama 8B yang sudah dihentikan pada free/developer tier. Periksa halaman
[model](https://console.groq.com/docs/models) dan
[depresiasi](https://console.groq.com/docs/deprecations) sebelum acara.

`ai/config.py` membaca `.env` pada root repo. Isi `GROQ_API_KEY` dengan satu key
Groq milikmu. Key tidak dicetak. Mulai ulang setelah mengedit `.env`.

Alur panggilan biasa:

```python
from ai.config import create_client

client, model = create_client()
response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Jelaskan satuan Pascal."}],
    temperature=0.2,
    max_completion_tokens=1024,
)
print(response.choices[0].message.content)
```

Ini hanya latihan API; aplikasi memakai prompt, filter, dan penanganan error.
Anggaran token keluaran juga dapat digunakan model reasoning. Jika jawaban kosong
atau terpotong, coba pertanyaan lebih sederhana dan periksa respons/anggaran saat
rehearsal; jangan menaikkan batas besar-besaran untuk seluruh kelas sekaligus.

## Tool calling pada repo

Model menerima skema tool `convert_unit(category, value, from_unit, to_unit)`.
Jika model meminta tool, aplikasi memeriksa nama dan argumen JSON, menjalankan
fungsi Python, lalu mengirim hasilnya sebagai pesan role `tool`. Panggilan API
kedua meminta penjelasan tanpa tool tambahan.

Satu giliran maksimal dua panggilan API dan dua konversi. Tidak ada eksekusi kode
bebas. UI menampilkan hasil fungsi Python terpisah dari teks penjelasan.
Model dapat memilih satuan yang keliru atau tidak meminta tool; periksa argumen dan
jangan menganggap angka teks tanpa hasil tool sudah terverifikasi.

| Error | Tindakan |
|---|---|
| 401 | Periksa key secara privat |
| 429 | Tunggu giliran dan batas reset, jangan spam retry |
| Model tidak diizinkan | Periksa `GROQ_MODEL` dan akses organisasi |
| Koneksi/timeout | Periksa internet; tab konversi tetap bisa dipakai |

`timeout=20` dan `max_retries=0` membuat kegagalan cepat terlihat. Test memakai
respons tiruan; sebelum acara tetap lakukan satu tes dengan key asli secara privat.
