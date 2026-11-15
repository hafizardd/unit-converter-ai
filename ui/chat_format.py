"""Ubah delimiter LaTeX keluaran AI menjadi format matematika Streamlit."""

import re

TOKENS = re.compile(
    r"```.*?```|`[^`\n]*`|\\\[(?P<block>.*?)\\\]|\\\((?P<inline>.*?)\\\)",
    re.DOTALL,
)


def normalize_math(text):
    def replace(match):
        if match.group("block") is not None:
            return "\n\n$$\n" + match.group("block").strip() + "\n$$\n\n"
        if match.group("inline") is not None:
            return "$" + match.group("inline").strip() + "$"
        return match.group(0)  # Contoh kode tetap tampil sebagai kode.

    return TOKENS.sub(replace, text)
