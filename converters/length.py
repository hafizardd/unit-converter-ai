from converters.base import convert_linear

FACTORS = {
    "nm": 1e-9,
    "um": 1e-6,
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1_000,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1_609.344,
    "nmi": 1_852,
}
UNITS = list(FACTORS)


def convert_length(value, from_unit, to_unit):
    return convert_linear(value, from_unit, to_unit, FACTORS)
