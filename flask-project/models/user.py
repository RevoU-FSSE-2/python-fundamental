from sqlalchemy_serializer import SerializerMixin

from config.settings import db


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128), nullable=True)
    password = db.Column(db.String(128), nullable=True)

class Animal(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    zone = db.Column(db.String(128))
    last_seen_location = db.Column(db.String(128), nullable=True)
