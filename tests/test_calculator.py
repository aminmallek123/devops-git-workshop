import pytest
from app.calculator import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 3) == 2

def test_mul():
    assert mul(4, 3) == 12

def test_div_basic():
    assert div(6, 3) == 2

def test_div_float():
    # Ce test échouera tant que la division est entière
    assert div(7, 2) == 3.5

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)