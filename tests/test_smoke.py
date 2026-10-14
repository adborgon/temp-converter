"""Smoke tests executed inside DockerSandboxManager."""
from __future__ import annotations

from app import __version__, main


def test_version_is_defined() -> None:
    assert isinstance(__version__, str)
    assert len(__version__) > 0


def test_main_returns_zero(capsys) -> None:
    exit_code = main()
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Application running." in captured.out