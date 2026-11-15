from converters.base import convert_linear

FACTORS = {
    "Pa": 1,
    "kPa": 1_000,
    "MPa": 1_000_000,
    "bar": 100_000,
    "mbar": 100,
    "atm": 101_325,
    "psi": 6_894.757293168,
    "Torr": 101_325 / 760,
}
UNITS = list(FACTORS)


def convert_pressure(value, from_unit, to_unit):
    return convert_linear(value, from_unit, to_unit, FACTORS)
