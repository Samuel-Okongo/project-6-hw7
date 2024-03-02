"""
This module contains the unit tests for the DivideCommand class.
"""

import unittest
from commands.divide import DivideCommand

class TestDivideCommand(unittest.TestCase):
    """
    Test cases for the DivideCommand class.
    """
    def test_divide(self):
        """
        Test the division of numbers using the DivideCommand class.
        """
        divide_command = DivideCommand()
        self.assertEqual(divide_command.execute(10, 2), 5)
        self.assertEqual(divide_command.execute(10.5, 2), 5.25)

    def test_zero_division(self):
        """
        Test the DivideCommand class for handling division by zero.
        """
        divide_command = DivideCommand()
        with self.assertRaises(ValueError):
            divide_command.execute(10, 0)

if __name__ == '__main__':
    unittest.main()
