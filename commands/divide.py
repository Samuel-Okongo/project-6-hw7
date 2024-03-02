class DivideCommand:
    def execute(self, *args):
        result = args[0]
        for number in args[1:]:
            if number == 0:
                raise ValueError("Cannot divide by zero!")
            result /= number
        return result
