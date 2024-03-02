from commands.command_handler import CommandHandler

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        # Register commands here
        self.command_handler.register_command("add", "AddCommand()")
        self.command_handler.register_command("subtract", "SubtractCommand()")
        self.command_handler.register_command("multiply", "MultiplyCommand()")
        self.command_handler.register_command("divide", "DivideCommand()")

    def start(self):
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
            except Exception as e:
                print(f"Error: {e}")
