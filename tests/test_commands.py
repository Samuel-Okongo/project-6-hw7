# test_commands.py

import pytest
from test_commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    add_command = AddCommand(1, 2)
    assert add_command.execute() == 3

def test_subtract_command():
    subtract_command = SubtractCommand(5, 3)
    assert subtract_command.execute() == 2

def test_multiply_command():
    multiply_command = MultiplyCommand(4, 3)
    assert multiply_command.execute() == 12

def test_divide_command():
    divide_command = DivideCommand(10, 2)
    assert divide_command.execute() == 5

def test_divide_command_zero_division():
    with pytest.raises(ValueError):
        divide_command = DivideCommand(10, 0)
        divide_command.execute()
