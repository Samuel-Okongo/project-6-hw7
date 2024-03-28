"""
This module defines the SubtractCommand class which is responsible for performing
subtraction operations. It takes an initial value and subtracts all subsequent
values from it.
"""

class SubtractCommand:
    """
    A command class used for subtracting any number of values from an initial value.
    """
    def execute(self, *args):
        """
        Executes the subtraction operation.

        Parameters:
            *args: A variable number of arguments (floats or integers) where the first argument
            is the value from which all subsequent arguments are subtracted.

        Returns:
            The result of the subtraction operation as a float or integer.
        """
        return args[0] - sum(args[1:])
