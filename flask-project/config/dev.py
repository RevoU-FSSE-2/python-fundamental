from .base import *  # noqa
import os
SQLALCHEMY_DATABASE_URI = os.getenv("POSTGRES_CONNECTION_STRING")
