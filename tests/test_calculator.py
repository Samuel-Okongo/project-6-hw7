'''My Calculator Test'''

from calculator import add, subtract

def test_addition():
    """
    Tests the add function from the calculator module.
    
    Ensures that the addition of two numbers returns the correct sum.
    """
    assert add(2, 2) == 4

def test_subtraction():
    """
    Tests the subtract function from the calculator module.
    
    Ensures that subtracting the second number from the first returns the correct difference.
    """
    assert subtract(2, 2) == 0
