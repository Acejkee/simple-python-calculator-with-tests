import pytest

from main_program.calculator import calculator


def test_plus():
    assert calculator('2+2') == 4


if __name__ == '__main__':
    pytest.main()
