import unittest
from commands.multiply import MultiplyCommand

class TestMultiplyCommand(unittest.TestCase):
    def test_multiply(self):
        multiply_command = MultiplyCommand()
        self.assertEqual(multiply_command.execute(2, 3), 6)
        self.assertEqual(multiply_command.execute(1, 2, 3, 4), 24)
        self.assertEqual(multiply_command.execute(0.5, 2), 1.0)

if __name__ == '__main__':
    unittest.main()
