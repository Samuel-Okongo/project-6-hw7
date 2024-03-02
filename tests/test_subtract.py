import unittest
from commands.subtract import SubtractCommand

class TestSubtractCommand(unittest.TestCase):
    def test_subtract(self):
        subtract_command = SubtractCommand()
        self.assertEqual(subtract_command.execute(10, 5), 5)
        self.assertEqual(subtract_command.execute(10, 2, 3), 5)
        self.assertEqual(subtract_command.execute(10.5, 0.5), 10.0)

if __name__ == '__main__':
    unittest.main()
