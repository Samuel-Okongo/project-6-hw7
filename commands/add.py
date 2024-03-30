"""
This module defines the AddCommand class, which is responsible for performing
addition operations. It sums a sequence of numbers provided as arguments.
"""

class AddCommand:
    """
    A command class used for adding together a sequence of numbers. When executed,
    it returns the sum of all provided arguments.
    """
    def execute(self, *args):
        """
        Executes the addition operation on the provided arguments.

        Parameters:
            *args: A variable number of arguments (floats or integers) to be summed.

        Returns:
            The sum of all provided arguments as a float or integer. If no arguments
            are provided, returns 0.
        """
        return sum(args)
