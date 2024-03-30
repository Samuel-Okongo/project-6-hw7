import logging

# Configure logging to write to a file with the level set to INFO
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class Calculator:
    @staticmethod
    def add(x, y):
        result = x + y
        logging.info(f'Added {x} to {y} resulting in {result}')
        return result

    @staticmethod
    def subtract(x, y):
        result = x - y
        logging.info(f'Subtracted {y} from {x} resulting in {result}')
        return result

    @staticmethod
    def multiply(x, y):
        result = x * y
        logging.info(f'Multiplied {x} with {y} resulting in {result}')
        return result

    @staticmethod
    def divide(x, y):
        try:
            result = x / y
            logging.info(f'Divided {x} by {y} resulting in {result}')
            return result
        except ZeroDivisionError:
            logging.error(f'Attempted to divide by zero')
            return None

# Example usage of the calculator
calculator = Calculator()

# Performing calculations
calculator.add(10, 5)
calculator.subtract(10, 5)
calculator.multiply(10, 5)
calculator.divide(10, 5)
calculator.divide(10, 0)  # This will log an error

# The operations above will generate and log the results in 'calculator.log'
