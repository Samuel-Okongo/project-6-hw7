"""
This module defines the CommandHandler class, which is responsible for managing
command instances. It supports registering commands under specific names and
executing these commands by name with given arguments. The CommandHandler ensures
that commands can be dynamically added and executed based on user input or
programmatic decisions.
"""

class CommandHandler:
    """
    Manages registration and execution of commands. Commands are stored in a dictionary
    and are accessed by their name for execution.
    """

    def __init__(self):
        """
        Initializes the CommandHandler with an empty dictionary to store command instances.
        """
        self.commands = {}

    def register_command(self, command_name, command_instance):
        """
        Registers a command instance under a specific name.

        Parameters:
            command_name (str): The name of the command under which the instance will be stored.
            command_instance (object): An instance of a command class.
        
        Raises:
            ValueError: If `command_instance` is not an instance of a command class.
        """
        # Assuming command_instance is now passed as an already initialized object
        if not hasattr(command_instance, 'execute'):
            raise ValueError("Provided command_instance does not have an execute method.")
        self.commands[command_name] = command_instance

    def execute_command(self, command_name, *args):
        """
        Executes a registered command by name with the provided arguments.

        Parameters:
            command_name (str): The name of the command to execute.
            *args: Variable arguments that will be passed to the command's execute method.

        Returns:
            The result of the command's execute method.

        Raises:
            ValueError: If the specified command name does not exist in the registry.
        """
        if command_name in self.commands:
            return self.commands[command_name].execute(*args)
        raise ValueError("Command not found!")
