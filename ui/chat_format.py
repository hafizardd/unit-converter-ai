"""Ubah delimiter LaTeX keluaran AI menjadi format matematika Streamlit."""

import re

TOKENS = re.compile(
    r"```.*?```|`[^`\n]*`|\n{0,2}(?:\\\[(?P<block>.*?)\\\]|"
    r"\$\$(?P<dollar_block>.*?)\$\$)\n{0,2}|\\\((?P<inline>.*?)\\\)",
    re.DOTALL,
)


def normalize_math(text):
    def replace(match):
        block = match.group("block")
        if block is None:
            block = match.group("dollar_block")
        if block is not None:
            return "\n\n$$\n" + block.strip() + "\n$$\n\n"
        if match.group("inline") is not None:
            return "$" + match.group("inline").strip() + "$"
        return match.group(0)  # Contoh kode tetap tampil sebagai kode.

    return TOKENS.sub(replace, text)
