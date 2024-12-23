# test_operations.py

from app import square, add_numbers, subtract_numbers

def test_square():
    assert square(2) == 4
    assert square(-3) == 9

def test_add_numbers():
    assert add_numbers(3, 5) == 8
    assert add_numbers(-1, 1) == 0

def test_subtract_numbers():
    assert subtract_numbers(10, 5) == 5
    assert subtract_numbers(0, 4) == -4
