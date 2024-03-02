class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name, command_instance):
        self.commands[command_name] = eval(command_instance)

    def execute_command(self, command_name, *args):
        if command_name in self.commands:
            return self.commands[command_name].execute(*args)
        else:
            raise ValueError("Command not found!")
