from .base import *  # noqa
import os

SQLALCHEMY_DATABASE_URI = os.getenv("TEST_POSTGRES_CONNECTION_STRING_TEST")
TESTING = True
