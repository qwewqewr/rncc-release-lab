import pytest

from rncc_calc import __version__
from rncc_calc.calculator import calculate


def test_add():
    assert calculate(2, "+", 3) == 5


def test_divide():
    assert calculate(9, "/", 3) == 3


def test_unknown_operator():
    with pytest.raises(ValueError):
        calculate(1, "?", 1)


def test_version_is_semver():
    major, minor, patch = __version__.split("-")[0].split(".")
    assert all(part.isdigit() for part in (major, minor, patch))
