import unittest
from commands.divide import DivideCommand

class TestDivideCommand(unittest.TestCase):
    def test_divide(self):
        divide_command = DivideCommand()
        self.assertEqual(divide_command.execute(10, 2), 5)
        self.assertRaises(ValueError, divide_command.execute, 10, 0)
        self.assertEqual(divide_command.execute(10.5, 2), 5.25)

    def test_zero_division(self):
        divide_command = DivideCommand()
        with self.assertRaises(ValueError):
            divide_command.execute(10, 0)

if __name__ == '__main__':
    unittest.main()
