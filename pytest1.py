import pytest


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Dzielenie przez zero!")
    return a / b


def test_addition():
    result = add(2.5, 3.5)
    assert result == 6.0


# sprawdzamy czy metoda rzuci ZeroDivisionError dla b=1
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_division_1():
    assert divide(5, 1) == 5


def test_division_2():
    assert divide(6, 2) == 3


def test_division_3():
    assert divide(6, '2') == 3  # TypeError
