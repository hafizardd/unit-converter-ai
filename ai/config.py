"""Disediakan fasilitator: membaca konfigurasi tanpa menampilkan secret."""

import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

DEFAULT_MODEL = "openai/gpt-oss-20b"


def get_settings():
    load_dotenv(Path(__file__).resolve().parents[1] / ".env")
    raw_keys = os.getenv("GROQ_API_KEYS", "").strip()
    if raw_keys:
        keys = [key.strip() for key in raw_keys.split(",") if key.strip()]
    else:
        keys = [os.getenv("GROQ_API_KEY", "").strip()]
    if not keys or not all(keys) or any("YOUR_" in key for key in keys):
        raise ValueError("Isi API key di file .env terlebih dahulu.")
    try:
        index = int(os.getenv("GROQ_KEY_INDEX", "0"))
    except ValueError:
        raise ValueError("GROQ_KEY_INDEX harus berupa angka bulat mulai 0.") from None
    if not 0 <= index < len(keys):
        raise ValueError("GROQ_KEY_INDEX berada di luar jumlah key yang tersedia.")
    model = os.getenv("GROQ_MODEL", "").strip() or DEFAULT_MODEL
    return keys[index], model


def create_client():
    key, model = get_settings()
    # Tidak mencoba semua key ketika terkena 429: kuota bisa tetap satu organisasi.
    return Groq(api_key=key, timeout=20.0, max_retries=0), model
