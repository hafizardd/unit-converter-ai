import pytest

from converters import convert_unit


@pytest.mark.parametrize(
    "category,value,source,target,expected",
    [
        ("pressure", 1, "Pa", "bar", 0.00001),
        ("pressure", 1, "bar", "Pa", 100000),
        ("pressure", 1, "atm", "Pa", 101325),
        ("pressure", 760, "Torr", "atm", 1),
        ("length", 1, "in", "cm", 2.54),
        ("length", 3, "ft", "cm", 91.44),
        ("length", 1, "nmi", "m", 1852),
        ("force", 1, "kgf", "N", 9.80665),
        ("force", 1, "kip", "lbf", 1000),
        ("temperature", -40, "C", "F", -40),
        ("temperature", 32, "F", "C", 0),
        ("temperature", 0, "C", "K", 273.15),
        ("temperature", 0, "K", "C", -273.15),
        ("temperature", 0, "R", "K", 0),
        ("temperature", 491.67, "R", "F", 32),
        ("temperature", 100, "C", "Re", 80),
        ("temperature", 20, "Re", "F", 77),
        ("temperature", -218.52, "Re", "K", 0),
    ],
)
def test_reference_values(category, value, source, target, expected):
    result = convert_unit(category, value, source, target)
    assert result["result"] == pytest.approx(expected)


@pytest.mark.parametrize("value", [float("nan"), float("inf"), True, "1", 10**400])
def test_reject_invalid_numbers(value):
    with pytest.raises(ValueError):
        convert_unit("pressure", value, "Pa", "bar")


@pytest.mark.parametrize(
    "value,unit", [(-274, "C"), (-1, "K"), (-500, "F"), (-1, "R"), (-218.53, "Re")]
)
def test_reject_below_absolute_zero(value, unit):
    with pytest.raises(ValueError, match="nol mutlak"):
        convert_unit("temperature", value, unit, "K")


def test_reject_unknown_category_unit_and_overflow():
    for args in (
        ("mass", 1, "kg", "N"),
        ("force", 1, "kg", "N"),
        ("temperature", 1, "unknown", "C"),
        ("pressure", 1e308, "MPa", "Pa"),
    ):
        with pytest.raises(ValueError):
            convert_unit(*args)
