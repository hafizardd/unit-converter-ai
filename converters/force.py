from converters.base import convert_linear

FACTORS = {
    "N": 1,
    "kN": 1_000,
    "kgf": 9.80665,
    "lbf": 4.4482216152605,
    "dyne": 1e-5,
    "kip": 4_448.2216152605,
}
UNITS = list(FACTORS)


def convert_force(value, from_unit, to_unit):
    return convert_linear(value, from_unit, to_unit, FACTORS)
