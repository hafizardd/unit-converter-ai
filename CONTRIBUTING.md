# Kontribusi

`main` cabang stabil. Buat branch pendek dari `main`, misalnya `feat/add-energy`,
`fix/temperature-boundary`, atau `docs/setup-linux`. Jangan memasukkan API key,
`.env`, `.venv`, zip peserta, atau cache.

Gunakan Conventional Commits berbahasa Inggris, subjek huruf kecil, maksimum 72
karakter. Contoh: `feat(converters): add nautical mile conversion`.
Satu commit untuk satu perubahan yang dapat dijelaskan.

```text
python -m pip install -r requirements-dev.txt
python -m ruff format .
python scripts/check.py
git diff --check
git diff --cached
```

Tambahkan test ketika perilaku hitungan atau error berubah. Pada PR, jelaskan
masalah, perubahan, dan pemeriksaan yang benar-benar dijalankan. Tunggu CI dan
review yang diwajibkan sebelum merge. Jangan mengubah aturan repo dari PR biasa.

Dokumentasi berbahasa Indonesia untuk pemula. Beri contoh input dan hasil yang
bisa dicoba. Hindari dependensi tambahan untuk fitur singkat dengan Python standar.
