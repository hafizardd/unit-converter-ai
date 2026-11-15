"""Validasi angka dan konversi linear melalui satuan dasar."""

import math


def validate_number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Nilai harus berupa angka.")
    try:
        value = float(value)
    except OverflowError:
        raise ValueError("Angka terlalu besar.") from None
    if not math.isfinite(value):
        raise ValueError("Nilai harus terbatas; NaN dan infinity tidak didukung.")
    return value


def convert_linear(value, from_unit, to_unit, factors):
    value = validate_number(value)
    if from_unit not in factors or to_unit not in factors:
        raise ValueError("Satuan tidak tersedia untuk kategori ini.")
    result = value * factors[from_unit] / factors[to_unit]
    return validate_number(result)
