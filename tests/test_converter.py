"""Unit tests for the temperature converter."""
from __future__ import annotations

import pytest

from app.converter import celsius_to_fahrenheit, fahrenheit_to_celsius


class TestCelsiusToFahrenheit:
    def test_freezing_point(self) -> None:
        assert celsius_to_fahrenheit(0) == 32.0

    def test_boiling_point(self) -> None:
        assert celsius_to_fahrenheit(100) == 212.0

    def test_body_temperature(self) -> None:
        assert celsius_to_fahrenheit(37) == 98.6

    def test_negative_temperature(self) -> None:
        # -40 is the unique point where both scales agree.
        assert celsius_to_fahrenheit(-40) == -40.0

    def test_accepts_float_input(self) -> None:
        assert celsius_to_fahrenheit(25.5) == 77.9

    @pytest.mark.parametrize("bad", ["10", None, [1], {1}, True, False])
    def test_rejects_non_numeric(self, bad) -> None:
        with pytest.raises(TypeError):
            celsius_to_fahrenheit(bad)  # type: ignore[arg-type]

    @pytest.mark.parametrize("bad", [float("nan"), float("inf"), float("-inf")])
    def test_rejects_non_finite(self, bad) -> None:
        with pytest.raises(ValueError):
            celsius_to_fahrenheit(bad)


class TestFahrenheitToCelsius:
    def test_freezing_point(self) -> None:
        assert fahrenheit_to_celsius(32) == 0.0

    def test_boiling_point(self) -> None:
        assert fahrenheit_to_celsius(212) == 100.0

    def test_body_temperature(self) -> None:
        assert fahrenheit_to_celsius(98.6) == pytest.approx(37.0)

    def test_negative_temperature(self) -> None:
        assert fahrenheit_to_celsius(-40) == -40.0

    @pytest.mark.parametrize("bad", ["32", None, [32], True, False])
    def test_rejects_non_numeric(self, bad) -> None:
        with pytest.raises(TypeError):
            fahrenheit_to_celsius(bad)  # type: ignore[arg-type]

    @pytest.mark.parametrize("bad", [float("nan"), float("inf"), float("-inf")])
    def test_rejects_non_finite(self, bad) -> None:
        with pytest.raises(ValueError):
            fahrenheit_to_celsius(bad)


class TestRoundTrip:
    @pytest.mark.parametrize("celsius", [-100, -40, 0, 21.7, 37, 100, 350])
    def test_celsius_round_trip(self, celsius: float) -> None:
        assert fahrenheit_to_celsius(celsius_to_fahrenheit(celsius)) == pytest.approx(
            celsius
        )

    @pytest.mark.parametrize("fahrenheit", [-220, -40, 32, 77.9, 98.6, 212, 500])
    def test_fahrenheit_round_trip(self, fahrenheit: float) -> None:
        assert celsius_to_fahrenheit(fahrenheit_to_celsius(fahrenheit)) == pytest.approx(
            fahrenheit
        )


class TestMainCli:
    def test_no_args_returns_zero_and_banner(self, capsys) -> None:
        from app import main

        assert main([]) == 0
        assert "Application running." in capsys.readouterr().out

    def test_celsius_to_fahrenheit_cli(self, capsys) -> None:
        from app import main

        assert main(["100", "c"]) == 0
        assert "212" in capsys.readouterr().out

    def test_fahrenheit_to_celsius_cli(self, capsys) -> None:
        from app import main

        assert main(["32", "f"]) == 0
        assert "0" in capsys.readouterr().out

    def test_explicit_target(self, capsys) -> None:
        from app import main

        assert main(["21", "f", "c"]) == 0
        assert "-6.111" in capsys.readouterr().out
