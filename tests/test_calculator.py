import pytest
from calculator.calculator import Calculator

def test_add():
    """Test that the add function returns the correct sum of two numbers."""
    assert Calculator.add(1, 2) == 3

def test_subtract():
    """Test that the subtract function returns the correct result of the subtraction of two numbers."""
    assert Calculator.subtract(5, 3) == 2

def test_multiply():
    """Test that the multiply function returns the product of two numbers."""
    assert Calculator.multiply(2, 3) == 6

def test_divide():
    """Test that the divide function returns the quotient of two numbers."""
    assert Calculator.divide(6, 2) == 3

def test_divide_by_zero():
    """Test that dividing by zero raises a ValueError."""
    with pytest.raises(ValueError):
        Calculator.divide(1, 0)
