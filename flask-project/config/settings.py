import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("POSTGRES_CONNECTION_STRING")
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models.user import * # noqa
