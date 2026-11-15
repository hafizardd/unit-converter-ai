"""Satu perintah pemeriksaan lokal, sama urutannya dengan CI."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for command in (
    [sys.executable, "-m", "ruff", "format", "--check", "."],
    [sys.executable, "-m", "ruff", "check", "."],
    [sys.executable, "-m", "pytest", "-q"],
):
    print(" ".join(command), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)
