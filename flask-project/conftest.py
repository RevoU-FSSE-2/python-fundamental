import pytest
from unittest.mock import patch
from config.settings import create_app, db
from models.user import User


@pytest.fixture(scope="module")
def app():
    app = create_app("config.testing")
    with app.app_context():
        yield app


@pytest.fixture(scope="module")
def client(app):
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="module", autouse=True)
def test_db(app):
    # Create the database and the tables
    db.create_all()

    yield db  # this is where the test happens

    # Teardown: drop the database and tables after the tests
    db.session.remove()
    db.drop_all()


@pytest.fixture
def generate_fake_user(test_db):
    iwant = User(first_name="iwant", last_name="kece", password="password")
    admin = User(first_name="admin", last_name="administrator", password="password")
    john = User(first_name="john", last_name="travolta", password="password")
    test_db.session.add(iwant)
    test_db.session.add(admin)
    test_db.session.add(john)
    test_db.session.commit()


@pytest.fixture
def appjson() -> dict:
    return {"Content-Type": "application/json"}

@pytest.fixture
def todo_get_all_stub():
    with patch("services.todo_service") as mocked_get:
        yield mocked_get