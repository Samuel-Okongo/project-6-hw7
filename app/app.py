"""
This module contains the App class which demonstrates a simple command handling mechanism for
a calculator, with history tracking and logging. Uses logging for most user interactions
and error handling.
"""

import logging
import pandas as pd
from commands.add import AddCommand
from commands.command_handler import CommandHandler
from commands.divide import DivideCommand
from commands.multiply import MultiplyCommand
from commands.subtract import SubtractCommand

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Set the log level

# Create handlers for both the terminal and the file output
stream_handler = logging.StreamHandler()  # Terminal output
file_handler = logging.FileHandler('app.log', mode='a')  # Append mode

# Create a formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

class App:
    """
    App class for a calculator, with command handling, history tracking, and logging.
    """
    def __init__(self):
        """
        Initializes the App with a command handler and history tracking.
        """
        self.command_handler = CommandHandler()
        try:
            self.history = pd.read_csv('history.csv')
        except FileNotFoundError:
            self.history = pd.DataFrame(columns=['Command', 'Arguments', 'Result'])

        self.register_command("add", AddCommand())
        self.register_command("subtract", SubtractCommand())
        self.register_command("multiply", MultiplyCommand())
        self.register_command("divide", DivideCommand())

    def register_command(self, name, command):
        """
        Registers a command with the command handler.
        """
        logger.info("Registered command: %s", name)
        self.command_handler.register_command(name, command)

    def start(self):
        """
        Starts the calculator application, accepting user input.
        """
        logger.info("Calculator started.'exit' to exit.'history' to view command history.")
        while True:
            command_input = input(">>> ").strip().lower().split()
            if not command_input:
                continue

            command_name = command_input[0]
            if command_name == "exit":
                logger.info("Exiting the calculator...")
                break
            if command_name == "history":
                self.print_history()
                continue

            try:
                args = list(map(float, command_input[1:]))
                result = self.command_handler.execute_command(command_name, *args)
                self.add_to_history(command_name, args, result)
                logger.info("Result: %s", result)
            except ValueError as e:
                logger.error("Error with '%s' args %s: %s", command_name, args, e)

    def add_to_history(self, command_name, args, result):
        """
        Adds a completed command's details to the history.
        """
        new_entry = pd.DataFrame([[command_name, args, result]],
                                 columns=['Command', 'Arguments', 'Result'])
        self.history = pd.concat([self.history, new_entry], ignore_index=True)
        self.history.to_csv('history.csv', index=False)

    def print_history(self):
        """
        Prints the history of executed commands.
        """
        if self.history.empty:
            logger.info("No history available.")
            return

        for index, row in self.history.iterrows():
            logger.info("%d: %s %s = %s", index + 1, row['Command'],
                        row['Arguments'], row['Result'])
