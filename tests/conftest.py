
import pytest
from faker import Faker

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of records to generate")

def pytest_generate_tests(metafunc):
    # Check for the 'dynamic_data'
    if "dynamic_data" in metafunc.fixturenames:
        faker = Faker()
        num_records = metafunc.config.option.num_records
        
        data = []
        for _ in range(num_records):
            a = faker.random_number(digits=2)
            b = faker.random_number(digits=2)
            operation = faker.random_element(elements=('add', 'subtract', 'multiply', 'divide'))
            if operation == 'add':
                expected = a + b
            elif operation == 'subtract':
                expected = a - b
            elif operation == 'multiply':
                expected = a * b
            elif operation == 'divide':
                expected = a / b if b != 0 else 'ValueError'  
            data.append((a, b, expected))
        
        metafunc.parametrize("a, b, expected", data)
