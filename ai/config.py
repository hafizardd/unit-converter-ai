"""Disediakan fasilitator: membaca konfigurasi tanpa menampilkan secret."""

import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

DEFAULT_MODEL = "openai/gpt-oss-20b"


def get_settings():
    load_dotenv(Path(__file__).resolve().parents[1] / ".env")
    key = os.getenv("GROQ_API_KEY", "").strip()
    if not key or "YOUR_" in key:
        raise ValueError("Isi API key di file .env terlebih dahulu.")
    model = os.getenv("GROQ_MODEL", "").strip() or DEFAULT_MODEL
    return key, model


def create_client():
    key, model = get_settings()
    return Groq(api_key=key, timeout=20.0, max_retries=0), model
