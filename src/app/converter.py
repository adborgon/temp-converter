"""Pure temperature conversion functions between Celsius and Fahrenheit."""
from __future__ import annotations

import math
from typing import Union

Number = Union[int, float]


def _validate_temperature(value: object) -> None:
    """Raise if ``value`` is not a finite real number."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(
            f"temperature must be a real number, got {type(value).__name__}"
        )
    if math.isnan(value) or math.isinf(value):
        raise ValueError("temperature must be a finite number")


def celsius_to_fahrenheit(celsius: Number) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    Args:
        celsius: Temperature in degrees Celsius.

    Returns:
        The equivalent temperature in degrees Fahrenheit.

    Raises:
        TypeError: If ``celsius`` is not a real number.
        ValueError: If ``celsius`` is NaN or infinite.
    """
    _validate_temperature(celsius)
    return celsius * 9.0 / 5.0 + 32.0


def fahrenheit_to_celsius(fahrenheit: Number) -> float:
    """Convert a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit: Temperature in degrees Fahrenheit.

    Returns:
        The equivalent temperature in degrees Celsius.

    Raises:
        TypeError: If ``fahrenheit`` is not a real number.
        ValueError: If ``fahrenheit`` is NaN or infinite.
    """
    _validate_temperature(fahrenheit)
    return (fahrenheit - 32.0) * 5.0 / 9.0
