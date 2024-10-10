
from flask import Blueprint, jsonify

from models.user import User


home_route = Blueprint("home", __name__)

@home_route.route("/")
def hello_world():
    users: list[User] = User.query.all()
    response = {}
    for user in users:
        response[user.id] = {"fullname": f"{user.first_name} {user.last_name}"}
    return jsonify(response), 200