"""
This module contains the unit tests for the SubtractCommand class.
"""

import unittest
from commands.subtract import SubtractCommand

class TestSubtractCommand(unittest.TestCase):
    """
    Test cases for the SubtractCommand class.
    """
    def test_subtract(self):
        """
        Test the subtraction of numbers using the SubtractCommand class.
        """
        subtract_command = SubtractCommand()
        self.assertEqual(subtract_command.execute(10, 5), 5)
        self.assertEqual(subtract_command.execute(10, 2, 3), 5)
        self.assertEqual(subtract_command.execute(10.5, 0.5), 10.0)

if __name__ == '__main__':
    unittest.main()
