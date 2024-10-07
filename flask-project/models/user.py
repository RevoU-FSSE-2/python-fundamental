from config.settings import db
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    password = db.Column(db.String(128))
