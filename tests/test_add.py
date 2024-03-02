import unittest
from commands.add import AddCommand

class TestAddCommand(unittest.TestCase):
    def test_add(self):
        add_command = AddCommand()
        self.assertEqual(add_command.execute(1, 2, 3), 6)
        self.assertEqual(add_command.execute(-1, -2), -3)
        self.assertEqual(add_command.execute(1.5, 2.5), 4.0)

if __name__ == '__main__':
    unittest.main()
