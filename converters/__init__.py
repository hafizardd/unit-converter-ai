"""Daftar kategori dipakai bersama oleh UI dan tool AI."""

from converters import force, length, pressure, temperature

CATEGORIES = {
    "pressure": {"label": "Tekanan", "units": pressure.UNITS, "convert": pressure.convert_pressure},
    "length": {"label": "Panjang", "units": length.UNITS, "convert": length.convert_length},
    "force": {"label": "Gaya", "units": force.UNITS, "convert": force.convert_force},
    "temperature": {
        "label": "Suhu",
        "units": temperature.UNITS,
        "convert": temperature.convert_temperature,
    },
}


def convert_unit(category, value, from_unit, to_unit):
    if category not in CATEGORIES:
        raise ValueError("Kategori harus pressure, length, force, atau temperature.")
    result = CATEGORIES[category]["convert"](value, from_unit, to_unit)
    return {
        "category": category,
        "value": value,
        "from_unit": from_unit,
        "to_unit": to_unit,
        "result": result,
    }
