# Unit Converter + AI

Materi lanjutan workshop Python untuk pemula: konversi **tekanan, panjang, gaya,
dan suhu**, dengan Streamlit serta asisten penjelasan melalui Groq.

## Jalankan

Python 3.12 disarankan; 3.11–3.13 didukung. Buka terminal di root repo.

Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python -m streamlit run app.py
```

Linux/Ubuntu atau macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
python -m streamlit run app.py
```

Jika aktivasi diblokir, pakai `.\.venv\Scripts\python.exe` menggantikan `python`.
Salin template `.env` sekali saja; jangan menimpa file yang sudah terisi.
Lengkapi key secara privat sebelum mencoba AI; konverter berjalan tanpa key.

```dotenv
GROQ_API_KEY=YOUR_GROQ_API_KEY
GROQ_MODEL=openai/gpt-oss-20b
```

Ganti `YOUR_GROQ_API_KEY` dengan satu key milikmu. Versi GitHub hanya membaca
`GROQ_API_KEY`.
Mulai ulang aplikasi setelah mengubah `.env`.

## Urutan belajar

1. [Setup dan terminal](docs/01-setup.md)
2. [Python dari nol](docs/02-python-dasar.md)
3. [Logika konversi](docs/03-logika-konversi.md)
4. [Streamlit](docs/04-streamlit.md)
5. [Konsep LLM](docs/05-konsep-llm.md)
6. [Groq dan tool calling](docs/06-chatbot-groq.md)
7. [Guardrail dan batasnya](docs/07-guardrail.md)
8. [Deploy Streamlit Community Cloud](docs/08-deploy-streamlit-cloud.md)
9. [Latihan dan petunjuk jawaban](docs/09-latihan-mandiri.md)
10. [Sumber resmi](docs/10-sumber.md)

## Belajar interaktif tanpa instalasi

Buka [belajar/index.html](belajar/index.html) dari folder hasil unduhan atau clone
repository menggunakan browser. Jika membuka tautan ini di GitHub, unduh file HTML
dahulu, lalu buka file yang diunduh. Seluruh fitur berjalan offline tanpa Python
atau API key.

Empat modul tekanan, gaya, panjang, dan suhu menyediakan visual yang dapat diubah,
23 contoh dengan langkah rumus, konverter, dan 52 soal kuis satu per satu. Progres
disimpan lokal pada browser. Lihat [panduan penggunaan](belajar/README.md) dan
[rencana serta kriteria penerimaan](docs/11-rencana-belajar-interaktif.md).

## Tambahan dari versi workshop

Package `converters/`, `ai/`, dan `ui/`, satuan tambahan, validasi, tabel perbandingan,
UI reusable, serta pengujian otomatis. AI meminta fungsi menghitung melalui tool
calling; hasil Python ditampilkan tersendiri. Penjelasan dan argumen pilihan AI tetap
perlu diperiksa. Tanpa hasil tool, angka pada teks AI belum terverifikasi.

Contoh: **1 Pa = 0.00001 bar**, **-40 C = -40 F**, **1 kgf = 9.80665 N**.
kg adalah massa; kgf gaya; `um` mikrometer; `R` Rankine. Pada aplikasi Streamlit,
gauge ↔ absolute dan konversi lintas dimensi tidak tersedia. HTML belajar memiliki
simulasi gauge–absolut, gaya berat, serta luas/volume untuk menjelaskan konsepnya.

## Pemeriksaan

Selain Python, siapkan Node.js 24 untuk menguji JavaScript HTML terhadap konverter
Python. Node hanya diperlukan untuk pengembangan, bukan untuk membuka HTML.

```text
python -m pip install -r requirements-dev.txt
python scripts/check.py
```

Menjalankan format, lint, dan pytest, termasuk simulasi UI. Tidak memanggil API
atau membutuhkan key. CI memakai Ubuntu dan Python 3.11–3.13; rehearsal API nyata
tetap terpisah. Lihat [CONTRIBUTING](CONTRIBUTING.md) untuk GitHub Flow.

Pemeriksaan interaksi HTML dengan Edge/Chromium terpasang:

```text
python scripts/check_learning_browser.py
```

Jika browser tidak ditemukan, gunakan `--browser PATH`. Pemeriksaan ini membuka
file lokal dalam browser headless pada lebar 360, 768, dan 1280 piksel, tanpa server.

Lisensi [MIT](LICENSE).
