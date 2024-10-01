from flask import Blueprint, jsonify, request

from db import database

auth_router = Blueprint("auth", __name__, url_prefix="/login")


@auth_router.route("", methods=["POST"])
def login():
    data = request.json
    print(data, "<<< this is data")
    username = data.get("username")  # admin
    password = data.get("password")
    print(username, password, "<<< this is username and password")
    userdb = database.get("user")
    # {
    #     "admin": {
    #         "password": "admin",
    #         "fullname": "Administrator",
    # }
    user = userdb.get(username)
    # if not found is None
    # {
    #         "password": "admin",
    #         "fullname": "Administrator",
    # }
    if user is None or user.get("password") != password:
        print("User not found")
        return jsonify({"message": "User not found"}), 401

    print("User found", user)
    return jsonify(user), 200
