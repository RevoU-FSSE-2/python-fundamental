from utils.profile_utils import generate_fullname, generate_gmail
import pytest

arguments_test= "firstname, lastname"
test_data = [
    ("iwant", "kece"),
    ("admin", "administrator"),
    ("john", "travolta"),
]

@pytest.mark.parametrize(arguments_test,
                         test_data,
                         )
def test_fullnameutils(firstname,lastname):
    fullname = generate_fullname(firstname, lastname)
    assert fullname == f"{firstname} {lastname}"
    
def test_generate_gmail():
    firstname = "iwant"
    email = generate_gmail(firstname)
    assert email == "iwant@gmail.com"