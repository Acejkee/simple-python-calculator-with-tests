import pytest

from main_program.calculator import calculator


def test_plus():
    assert calculator('2+2') == 4


def test_no_sign():
    with pytest.raises(ValueError) as error:
        calculator("qwerty")
    assert 'Выражение должно содержать хотя бы один знак (+-/*)' == error.value.args[0]


def test_two_sign():
    with pytest.raises(ValueError) as error:
        calculator("3+3+3")
    assert 'Выражение должно содержать 2 целых числа и 1 знак' == error.value.args[0]


if __name__ == '__main__':
    pytest.main()
