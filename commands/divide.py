"""
This module defines the DivideCommand class, which is responsible for performing
division operations. It divides an initial value by a sequence of other values,
handling division by zero with an appropriate error.
"""

class DivideCommand:
    """
    A command class used for dividing an initial value by a sequence of other
    numbers. It ensures division by zero is handled gracefully by raising a
    ValueError.
    """
    def execute(self, *args):
        """
        Executes the division operation.

        Parameters:
            *args: A variable number of arguments (floats or integers) where the first argument
            is the initial value to be divided by all subsequent arguments. Division by zero
            is checked for each subsequent argument.

        Raises:
            ValueError: If any of the subsequent arguments is zero, since division by zero
            is mathematically undefined.

        Returns:
            The result of the division operation as a float. If only one argument is provided,
            that argument is returned as the result.
        """
        if len(args) < 2:
            raise ValueError("At least two arguments are required for division.")
        result = args[0]
        for number in args[1:]:
            if number == 0:
                raise ValueError("Cannot divide by zero!")
            result /= number
        return result
