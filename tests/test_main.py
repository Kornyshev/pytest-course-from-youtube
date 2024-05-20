from contextlib import nullcontext as does_not_raise

import pytest

from src.main import Calculator


@pytest.fixture
def calculator():
    return Calculator()


class TestCalculator:

    @pytest.mark.parametrize(
        ["x", "y", "res", "expectation"],
        [
            (1, 2, 0.5, does_not_raise()),
            (5, -1, -5, does_not_raise()),
            (10, 2, 5, does_not_raise()),
            (10, "2", 5, pytest.raises(TypeError)),
            ("10", 2, 5, pytest.raises(TypeError)),
            (10, 0, 5, pytest.raises(ZeroDivisionError)),
        ]
    )
    def test_divide(self, calculator, x, y, res, expectation):
        with expectation:
            assert calculator.divide(x, y) == res

    @pytest.mark.parametrize(
        ["x", "y", "res", "expectation"],
        [
            (1, 2, 3, does_not_raise()),
            (5, -1, 4, does_not_raise()),
            (10, 2, 12, does_not_raise()),
            (10, "2", 12, pytest.raises(TypeError)),
            ("10", 2, 12, pytest.raises(TypeError)),
        ]
    )
    def test_add(self, calculator, x, y, res, expectation):
        with expectation:
            assert calculator.add(x, y) == res


def pytest_runtest_setup(item):
    print(f"Setting up: {item}")


def pytest_runtest_teardown(item):
    print(f"\nTearing down: {item}")


def test_divide_with_monkeypatch(monkeypatch, calculator):
    def mock_divide(x, y):
        return 42

    monkeypatch.setattr(calculator, "divide", mock_divide)
    assert calculator.divide(1, 1) == 42


@pytest.mark.parametrize("x, y, expected", [(i, 1, i + 1) for i in range(1, 30)])
def test_parallel_addition(calculator, x, y, expected):
    assert calculator.add(x, y) == expected


@pytest.mark.modify
def test_should_be_skipped():
    assert 1 == 1


def test_normal():
    assert 1 == 1


def test_custom_option(custom_option):
    assert custom_option == "default_value"
