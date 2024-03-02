"""
This module contains the unit tests for the MultiplyCommand class.
"""

import unittest
from commands.multiply import MultiplyCommand

class TestMultiplyCommand(unittest.TestCase):
    """
    Test cases for the MultiplyCommand class.
    """
    def test_multiply(self):
        """
        Test the multiplication of numbers using the MultiplyCommand class.
        """
        multiply_command = MultiplyCommand()
        self.assertEqual(multiply_command.execute(2, 3), 6)
        self.assertEqual(multiply_command.execute(1, 2, 3, 4), 24)
        self.assertEqual(multiply_command.execute(0.5, 2), 1.0)

if __name__ == '__main__':
    unittest.main()
