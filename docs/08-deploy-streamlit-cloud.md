# 8. Deploy ke Streamlit Community Cloud

Deployment adalah latihan setelah workshop, bukan syarat kelas. Jalankan aplikasi
secara lokal lebih dahulu. Jangan memakai key workshop yang sudah dicabut.

1. Fork repo ke akunmu dan pastikan tidak ada `.env` atau key dalam Git.
2. Masuk ke Streamlit Community Cloud dengan GitHub.
3. Buat app dari repo, branch yang diinginkan, dan entry point `app.py`.
4. Pilih Python yang didukung proyek, disarankan 3.12 bila tersedia.
5. Pada pengaturan Secrets, isi konfigurasi TOML berikut secara privat.

```toml
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
GROQ_MODEL = "openai/gpt-oss-20b"
```

Secret tingkat atas di Community Cloud tersedia sebagai environment variables;
`ai/config.py` membacanya lewat `os.getenv`, sehingga tidak memerlukan `.env` pada
server. Nilai environment diprioritaskan oleh `load_dotenv` dengan defaultnya.
Jangan menaruh secret dalam file TOML yang di-commit.

Jalankan deploy dan periksa log. Dependensi runtime berasal dari `requirements.txt`.
Jika konverter berjalan tetapi AI gagal, periksa secret, model, dan kuota akun.

App publik membagikan kuota key server kepada pengunjung. Batas sesi UI pada repo
tidak mengendalikan total kuota. Untuk layanan publik berkelanjutan, tambahkan
autentikasi dan batas terpusat atau matikan AI sampai pengelolaan akses tersedia.
Untuk latihan singkat, pantau penggunaan dan hentikan app bila kuota habis.

Lihat panduan resmi [secrets management](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).
