"""Filter sederhana untuk latihan, bukan jaminan tahan semua prompt injection."""

import re

from converters import CATEGORIES

REFUSAL = "Aku membantu konversi tekanan, suhu, panjang, dan gaya. Coba tanyakan salah satunya."
BLOCKED = ["abaikan instruksi", "ignore previous", "system prompt", "lupakan aturan"]
TOPICS = {
    "pressure",
    "tekanan",
    "temperature",
    "suhu",
    "length",
    "panjang",
    "force",
    "gaya",
    "pascal",
    "celsius",
    "celcius",
    "fahrenheit",
    "kelvin",
    "meter",
    "newton",
    "pa",
    "kpa",
    "mpa",
    "bar",
    "atm",
    "psi",
    "mm",
    "cm",
    "m",
    "km",
    "in",
    "ft",
    "mi",
    "n",
    "kn",
    "kgf",
    "lbf",
    "c",
    "f",
    "k",
}

TOPICS |= {unit.casefold() for data in CATEGORIES.values() for unit in data["units"]}
TOPICS |= {"rankine", "mikrometer", "nanometer", "yard", "dina"}


def check_input(prompt, history=None):
    text = prompt.strip().casefold()
    if not text:
        return "Tulis pertanyaan terlebih dahulu."
    if len(text) > 500:
        return "Batasi pertanyaan sampai 500 karakter."
    if any(phrase in text for phrase in BLOCKED):
        return REFUSAL
    words = set(re.findall(r"[^\W\d_]+", text))
    if words & TOPICS:
        return None
    # Izinkan pertanyaan lanjutan yang pendek setelah topik valid.
    if history and text in {"kenapa?", "mengapa?", "jelaskan lagi", "jelaskan lagi dong"}:
        return None
    return REFUSAL
