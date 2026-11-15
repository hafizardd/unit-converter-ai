# 9. Latihan mandiri

Kerjakan berurutan. Buat branch untuk tiap latihan; jangan mengubah key di kode.

## Level 1 — Membaca kode

Prediksi hasil 2 bar → kPa, 5 km → m, dan 100 C → F, lalu coba di aplikasi.
Jawaban: 200 kPa, 5000 m, 212 F. Jelaskan mengapa suhu membutuhkan offset.

## Level 2 — Menambah satuan

Tambahkan `MN` ke gaya. Petunjuk: 1 MN = 1000000 N. Ubah dictionary faktor saja;
daftar UI dan prompt memakai data yang sama. Tambahkan test 2 MN → 2000 kN.

Tambahkan yard pada versi sederhana workshop, lalu cocokkan dengan repo.
Petunjuk: 1 yd = 0.9144 m. Jangan membuat fungsi baru per pasangan.

## Level 3 — Menukar pilihan

Tambahkan tombol tukar satuan di UI reusable. Gunakan callback untuk menukar
dua nilai `session_state` sebelum widget dibuat pada rerun berikutnya. Jangan
mengganti key widget setelah widget sudah dibuat pada run yang sama.
Uji bahwa hasil 2 m → cm menjadi 2 cm → m setelah tukar tanpa mengubah nilai input.

## Level 4 — Pengujian

Tambahkan test bolak-balik satu pasangan satuan memakai `pytest.approx`.
Nilai acuan harus dihitung dari definisi, bukan menyalin rumus implementasi ke test.
Tambahkan contoh unit tidak dikenal dan suhu di bawah nol mutlak.

## Level 5 — Chatbot

Amati respons tiruan di `tests/test_ai.py`. Catat urutan system → user → tool request
→ hasil tool → penjelasan. Tambahkan contoh model memilih satuan yang tidak ada;
pastikan tool mengembalikan error dan tidak ada hasil numerik yang dianggap valid.

Streaming adalah tantangan lanjutan: buat panggilan tool tetap non-stream, lalu
stream penjelasan setelah hasil tool tersedia. Jangan melakukan parsing tool JSON
dari potongan token jika belum memahami state dan error yang mungkin terjadi.

## Level 6 — Eksperimen guardrail

Cari pertanyaan valid yang salah ditolak, dan pertanyaan di luar topik yang lolos
karena menyebut satuan. Tulis keterbatasan sebelum menambah aturan. Bandingkan biaya
filter lokal dengan classifier LLM tambahan: classifier memerlukan request/token
tambahan dan tetap bisa salah.

Selesai bila kamu bisa menjelaskan perubahan dan buktinya, bukan hanya aplikasi
terlihat berjalan. Gunakan `python scripts/check.py` sebelum membuka PR.
