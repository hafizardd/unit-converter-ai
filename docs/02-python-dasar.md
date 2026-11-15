# 2. Python dari nol

Buat `hello.py` di folder latihan. Tulis `print("Halo!")`, simpan dengan Ctrl+S,
lalu jalankan `python hello.py`. Menyimpan berbeda dengan menjalankan.

Variabel memberi nama pada nilai. Coba ubah `value` menjadi 10:

```python
value = 1
factor = 100000
result = value / factor
print(result)
```

`=` mengisi variabel; `+`, `-`, `*`, `/` operator. Desimal memakai titik: `2.5`.
Teks memakai kutip, misalnya `"Pa"`. Python membedakan huruf besar dan kecil.

Fungsi menyimpan langkah berulang. Parameter adalah input; `return` mengirim hasil
kepada pemanggil. Empat spasi menandai isi fungsi:

```python
def pa_to_bar(value):
    return value / 100000


result = pa_to_bar(1)
print(result)
```

`print` menampilkan nilai; `return` mengembalikan nilai. Fungsi yang hanya mencetak
tidak otomatis menghasilkan angka yang bisa dipakai UI.

Dictionary berisi pasangan kunci dan nilai:

```python
factors = {"Pa": 1, "kPa": 1000, "bar": 100000}
print(factors["bar"])
units = list(factors)
print(units)
```

`factors["bar"]` mencari angka 100000. `list(factors)` mengambil daftar kunci untuk
pilihan UI. Salah ejaan dapat menyebabkan `KeyError`.

Percabangan memilih langkah. `==` membandingkan, bukan mengisi variabel:

```python
def to_celsius(value, unit):
    if unit == "F":
        return (value - 32) * 5 / 9
    elif unit == "K":
        return value - 273.15
    else:
        return value
```

`if` diperiksa lebih dahulu, lalu `elif`, lalu `else`. Pada kode aplikasi, satuan
tak dikenal ditolak sebelum memilih rumus; contoh pendek di atas untuk belajar sintaks.

Modul adalah file Python. Dari root repo, buat file latihan berisi:

```python
from converters.pressure import convert_pressure

print(convert_pressure(1, "Pa", "bar"))
```

`import` mengambil fungsi dari file lain. Jangan menamai latihan `streamlit.py`
atau `groq.py` karena bertabrakan dengan library.
`if __name__ == "__main__":` menandai contoh terminal yang tidak ikut berjalan
ketika file di-import.

**Latihan:** fungsi `double(value)` mengembalikan dua kali input. `double(3)`
harus menghasilkan 6 tanpa menaruh `print` di dalam fungsi.
