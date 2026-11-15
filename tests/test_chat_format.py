import pytest

from ui.chat_format import normalize_math


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            r"Hasil \(5 \times 1000 / 6894.757 = 0.725\) psi",
            r"Hasil $5 \times 1000 / 6894.757 = 0.725$ psi",
        ),
        (r"\[\frac{5000}{6894.757}\]", "\n\n$$\n" + r"\frac{5000}{6894.757}" + "\n$$\n\n"),
        (r"\( x = 1 \)", "$x = 1$"),
        ("Suhu (C) dan gaya (N)", "Suhu (C) dan gaya (N)"),
        (r"`\(x\)`", r"`\(x\)`"),
        (
            "```python\n" + r"formula = '\(x\)'" + "\n```",
            "```python\n" + r"formula = '\(x\)'" + "\n```",
        ),
        (r"Sudah benar: $x = 1$", r"Sudah benar: $x = 1$"),
        (r"Belum lengkap: \(x", r"Belum lengkap: \(x"),
    ],
)
def test_supported_delimiters_and_preserved_text(source, expected):
    result = normalize_math(source)
    assert result == expected
    assert normalize_math(result) == result
