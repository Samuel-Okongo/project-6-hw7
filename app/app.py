import logging
from commands.add import AddCommand
from commands.command_handler import CommandHandler
from commands.divide import DivideCommand
from commands.multiply import MultiplyCommand
from commands.subtract import SubtractCommand

# Create a custom logger
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
    App class demonstrating a simple command handling mechanism for
    a calculator, with history tracking and logging. Uses logging for
    most user interactions and error handling.
    """
    def __init__(self):
        """
        Initializes the App with a command handler, registers the
        mathematical operations as commands, and initializes history tracking.
        """
        self.command_handler = CommandHandler()
        self.history = []
        
        # Register commands
        self.register_command("add", AddCommand())
        self.register_command("subtract", SubtractCommand())
        self.register_command("multiply", MultiplyCommand())
        self.register_command("divide", DivideCommand())
    
    def register_command(self, name, command):
        """
        Registers a command and logs the registration.
        """
        self.command_handler.register_command(name, command)
        logger.info(f"Registered command: {name}")
    
    def start(self):
        """
        Starts the application loop, handling commands and logging outputs.
        """
        logger.info("Calculator started. Type 'exit' to exit. Type 'history' to view command history.")
        while True:
            command_input = input(">>> ").strip().lower().split()
            if not command_input:
                continue
            
            command_name = command_input[0]
            if command_name == "exit":
                logger.info("Exiting the calculator...")
                break
            elif command_name == "history":
                self.print_history()
                continue
            
            try:
                args = list(map(float, command_input[1:]))
                result = self.command_handler.execute_command(command_name, *args)
                self.history.append((command_name, args, result))
                logger.info(f"Result: {result}")
            except ValueError as e:
                logger.error(f"Error executing command '{command_name}' with args {args}: {e}")
    
    def print_history(self):
        """
        Logs the history of commands executed.
        """
        if not self.history:
            logger.info("No history available.")
            return
        
        for i, (command, args, result) in enumerate(self.history, start=1):
            logger.info(f"{i}: {command} {args} = {result}")
