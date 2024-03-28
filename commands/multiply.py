"""
This module defines the MultiplyCommand class which is responsible for performing
multiplication operations. It multiplies a sequence of numbers together.
"""

class MultiplyCommand:
    """
    A command class used for multiplying a sequence of numbers together. It accepts
    zero or more arguments and returns the product of all arguments.
    """
    def execute(self, *args):
        """
        Executes the multiplication operation.

        Parameters:
            *args: A variable number of arguments (floats or integers) to be multiplied
            together. If no arguments are given, the result will be 1, following the
            mathematical convention that the product of no numbers is the multiplicative
            identity.

        Returns:
            The product of all provided arguments as a float or integer. If no arguments
            are provided, returns 1.
        """
        result = 1
        for number in args:
            result *= number
        return result
