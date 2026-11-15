"""Tool hanya dapat memanggil konverter; tidak mengeksekusi kode dari model."""

import json

from converters import CATEGORIES, convert_unit

TOOL = {
    "type": "function",
    "function": {
        "name": "convert_unit",
        "description": "Hitung konversi memakai fungsi Python yang tervalidasi.",
        "parameters": {
            "type": "object",
            "properties": {
                "category": {"type": "string", "enum": list(CATEGORIES)},
                "value": {"type": "number"},
                "from_unit": {"type": "string"},
                "to_unit": {"type": "string"},
            },
            "required": ["category", "value", "from_unit", "to_unit"],
            "additionalProperties": False,
        },
    },
}


def execute_tool(name, arguments):
    if name != "convert_unit":
        return {"error": "Tool tidak diizinkan."}
    try:
        data = json.loads(arguments)
        if not isinstance(data, dict) or set(data) != {"category", "value", "from_unit", "to_unit"}:
            raise ValueError("Argumen tool tidak lengkap atau memiliki field tambahan.")
        if not all(isinstance(data[key], str) for key in ("category", "from_unit", "to_unit")):
            raise ValueError("Kategori dan satuan harus teks.")
        return convert_unit(**data)
    except (ValueError, TypeError, KeyError, OverflowError):
        return {"error": "Konversi ditolak: cek kategori, angka, satuan, dan batas suhu."}
