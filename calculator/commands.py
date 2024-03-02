# commands.py

from command_interface import Command

class AddCommand(Command):
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def execute(self):
        return self.operand1 + self.operand2

class SubtractCommand(Command):
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def execute(self):
        return self.operand1 - self.operand2

class MultiplyCommand(Command):
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def execute(self):
        return self.operand1 * self.operand2

class DivideCommand(Command):
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def execute(self):
        if self.operand2 == 0:
            raise ValueError("Cannot divide by zero.")
        return self.operand1 / self.operand2
