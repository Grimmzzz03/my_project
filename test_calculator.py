# test for calculator  
import pytest

from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_zero():  
    assert square(0) == 0

def test_negative():    
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-4) == 16
    assert square(-5) == 25

def test_str():
    with pytest.raises(TypeError):
            square("cat")