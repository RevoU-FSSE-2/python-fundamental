import pytest
from dotenv import load_dotenv
import os
load_dotenv()


@pytest.fixture
def app():
    from main import app
    # this where we are setup the app for testing

    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.getenv("TEST_POSTGRES_CONNECTION_STRING_TEST"),
    })
    # TODO: migrate database tables
    # TODO: create a test user / test data
    
    yield app # this is where the testing happens
    
    # TODO: clean up the database after testing
    

@pytest.fixture
def client(app):
    return app.test_client() 


@pytest.fixture
def appjson() -> dict:
    return {"Content-Type": "application/json"}
