# 4. Dari terminal menjadi website

Streamlit membuat tampilan dari Python. Rumus tetap bisa digunakan tanpa UI.
Contoh file latihan dari root repo:

```python
import streamlit as st
from converters.pressure import convert_pressure, UNITS

st.title("Konverter tekanan")
value = st.number_input("Nilai", value=1.0)
from_unit = st.selectbox("Dari", UNITS)
to_unit = st.selectbox("Ke", UNITS, index=3)
result = convert_pressure(value, from_unit, to_unit)
st.success(f"{value:.10g} {from_unit} = {result:.10g} {to_unit}")
```

Jalankan `python -m streamlit run nama_file.py`. Nilai widget menjadi parameter
fungsi. Saat pilihan berubah, script dijalankan ulang; tidak wajib tombol konversi.

`st.tabs` mengatur tampilan. Isi tab umumnya tetap dieksekusi saat rerun walaupun
tidak dipilih. Letakkan panggilan API di dalam `if prompt:` setelah submit chat,
agar mengganti selectbox tidak memanggil model.

Widget serupa memakai `key` unik, misalnya `pressure_from` dan `length_from`.
Label boleh sama. Tangani input yang ditolak dengan `try/except ValueError` dan
`st.error`; jangan menyembunyikan semua error pemrograman.

Variabel biasa dibuat ulang saat rerun. `st.session_state` menyimpan riwayat chat
selama sesi browser, bukan database atau ingatan permanen. Pertanyaan baru
ditambahkan sekali, setelah fungsi AI menerima riwayat lama.

Repo memakai `ui/converter_tab.py` untuk empat kategori setelah versi workshop
mengajarkan tiap tab secara terpisah. Tabel perbandingan memakai fungsi yang sama.

**Latihan:** tambahkan caption satuan gaya tanpa mengubah rumus di `converters/`.
