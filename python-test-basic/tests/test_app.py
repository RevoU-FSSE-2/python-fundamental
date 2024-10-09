from utils import (
    calculate_discounted_price,
    calculate_dimensions,
    fullname,
    get_year_of_birth,
)




def test_discount():
    # assert -> bener ga yang result == (sama dengan) expected
    assert calculate_discounted_price(10_000, 50) == 5_000
    assert calculate_discounted_price(100_000, 10) == 90_000


def test_dimension():
    assert calculate_dimensions(30, 20, 10) == 6000


def test_fullname(person_fixture):

    for person in person_fixture:
        assert fullname(person["firstname"], person["lastname"]) == person["expected"]


def test_get_year_of_birth(person_fixture):
    for person in person_fixture:
        assert get_year_of_birth(person["age"]) == person["expected_year"]
