"""Main application package."""
from __future__ import annotations

import sys
from typing import Sequence

from app.converter import celsius_to_fahrenheit, fahrenheit_to_celsius

__version__ = "0.1.0"

_USAGE = (
    f"temp-converter {__version__} — convierte temperaturas entre Celsius y Fahrenheit.\n"
    "Uso: python -m app <valor> <c|f> [c|f]\n"
    "  valor   temperatura numérica\n"
    "  c/f     unidad de origen (c = Celsius, f = Fahrenheit)\n"
    "  [c|f]   unidad de destino (por defecto: la otra escala)"
)


def _label(unit: str) -> str:
    return "°C" if unit == "c" else "°F"


def main(argv: Sequence[str] | None = None) -> int:
    """Application entry point.

    Args:
        argv: CLI arguments (without the program name). When ``None`` or
            empty, prints the banner and usage, and returns 0.
    """
    argv = list(argv or [])
    if not argv:
        print("Application running.")
        print(_USAGE)
        return 0

    try:
        value = float(argv[0])
    except ValueError:
        print(f"Error: '<valor>' no es un número válido: {argv[0]!r}", file=sys.stderr)
        return 2

    if len(argv) < 2 or argv[1] not in {"c", "f"}:
        print("Error: la unidad de origen debe ser 'c' o 'f'.", file=sys.stderr)
        return 2

    source = argv[1]
    if len(argv) > 3 or (len(argv) == 3 and argv[2] not in {"c", "f"}):
        print("Error: la unidad de destino debe ser 'c' o 'f'.", file=sys.stderr)
        return 2

    target = argv[2] if len(argv) == 3 else ("f" if source == "c" else "c")

    if source == "c":
        result = celsius_to_fahrenheit(value) if target == "f" else value
    else:
        result = fahrenheit_to_celsius(value) if target == "c" else value

    print(f"{value:g} {_label(source)} = {result:g} {_label(target)}")
    return 0
