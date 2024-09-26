
import pytest
from convert import convert

# Program 2

print("~~~~~~~~~~~~~~~Program 2~~~~~~~~~~~~~~~")

def test_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000

def test_error():
    with pytest.raises(TypeError):
        convert("1")

# Program 3

print("~~~~~~~~~~~~~~~Program 3~~~~~~~~~~~~~~~")

def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.691)

# Program 4

print("~~~~~~~~~~~~~~~Program 4~~~~~~~~~~~~~~~")

def test_float_conversion_two():
    assert convert(0.001) == pytest.approx(149597870.691, abs=0.1)


# Program 5

print("~~~~~~~~~~~~~~~Program 5~~~~~~~~~~~~~~~")

def test_float_conversion_three():
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-5)

# Program 6

print("~~~~~~~~~~~~~~~Program 6~~~~~~~~~~~~~~~")

def test_float_conversion_four():
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-3)


# Program 7

print("~~~~~~~~~~~~~~~Program 7~~~~~~~~~~~~~~~")

def test_float_conversion_five():
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-2)

# Program 8

print("~~~~~~~~~~~~~~~Program 8~~~~~~~~~~~~~~~")

def test_float_conversion_six():
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-12)

