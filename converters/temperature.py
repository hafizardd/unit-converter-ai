from converters.base import validate_number

UNITS = ["C", "F", "K", "R"]


def convert_temperature(value, from_unit, to_unit):
    value = validate_number(value)
    if from_unit not in UNITS or to_unit not in UNITS:
        raise ValueError("Satuan suhu tidak tersedia.")
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        celsius = value * 5 / 9 - 273.15
    if celsius < -273.15 - 1e-9:
        raise ValueError("Suhu tidak boleh di bawah nol mutlak (0 K).")
    celsius = max(celsius, -273.15)
    if to_unit == "C":
        result = celsius
    elif to_unit == "F":
        result = celsius * 9 / 5 + 32
    elif to_unit == "K":
        result = celsius + 273.15
    else:
        result = (celsius + 273.15) * 9 / 5
    return validate_number(result)
