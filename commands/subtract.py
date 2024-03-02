class SubtractCommand:
    def execute(self, *args):
        return args[0] - sum(args[1:])
