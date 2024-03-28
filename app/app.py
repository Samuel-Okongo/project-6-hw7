"""Module docstring: This module contains the App class that demonstrates
a simple command handling mechanism for mathematical operations. It
utilizes a CommandHandler to register and execute commands corresponding
to basic mathematical operations such as addition, subtraction,
multiplication, and division. Users interact with the calculator by
entering commands and arguments through the command line."""

from commands.add import AddCommand
from commands.command_handler import CommandHandler
from commands.divide import DivideCommand
from commands.multiply import MultiplyCommand
from commands.subtract import SubtractCommand

class App:
    """
    App class to demonstrate a simple command handling mechanism for
    a calculator. Supports basic mathematical operations.
    """
    def __init__(self):
        """
        Initializes the App with a command handler and registers the
        mathematical operations as commands.
        """
        self.command_handler = CommandHandler()
        # Ensure these command strings are properly handled elsewhere,
        # or consider directly passing instantiated objects or functions.
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())
    def start(self):
        """
        Starts the application loop which prompts the user for commands
        and executes them. Type 'exit' to exit.
        """
        print("Type 'exit' to exit.")
        while True:
            command_input = input(">>> ").strip().lower().split()
            if not command_input:
                continue
            command_name = command_input[0]
            if command_name == "exit":
                print("Exiting the calculator...")
                break
            try:
                args = list(map(float, command_input[1:]))
                result = self.command_handler.execute_command(command_name, *args)
                print(result)
            except ValueError as e:
                print(f"Error: {e}")
