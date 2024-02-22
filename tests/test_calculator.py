"""
This module contains tests for arithmetic operations implemented in the Calculator class.
Tests cover addition, subtraction, multiplication, division, and division by zero.
"""

import pytest
from calculator.calculator import Calculator

@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, 3),
    (4, 5, 9),
])
def test_add(num1, num2, expected):
    """Test addition functionality."""
    assert Calculator.add(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 2),
    (10, 4, 6),
])
def test_subtract(num1, num2, expected):
    """Test subtraction functionality."""
    assert Calculator.subtract(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (2, 3, 6),
    (7, 8, 56),
])
def test_multiply(num1, num2, expected):
    """Test multiplication functionality."""
    assert Calculator.multiply(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (6, 2, 3),
    (9, 3, 3),
])
def test_divide(num1, num2, expected):
    """Test division functionality."""
    assert Calculator.divide(num1, num2) == expected

def test_divide_by_zero():
    """Test division by zero raises a ValueError."""
    with pytest.raises(ValueError):
        Calculator.divide(1, 0)
        