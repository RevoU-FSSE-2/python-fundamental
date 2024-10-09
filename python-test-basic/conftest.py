import pytest

@pytest.fixture
def person_fixture():
    persons = [
    {
        "firstname": "John",
        "lastname": "Doe",
        "age": 53,
        "expected": "John Doe",
        "expected_year": 1971,
    },
    {
        "firstname": "Jane",
        "lastname": "Doe",
        "age": 50,
        "expected": "Jane Doe",
        "expected_year": 1974,
    },
    {
        "firstname": "John",
        "lastname": "Wick",
        "age": 40,
        "expected": "John Wick",
        "expected_year": 1984,
    },
    {
        "firstname": "hasan",
        "lastname": "sudrajat",
        "age": 30,
        "expected": "hasan sudrajat",
        "expected_year": 1994,
    },
]
    return persons