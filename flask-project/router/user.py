from flask import Blueprint, jsonify, request

from db import database

user_route = Blueprint("user", __name__, url_prefix="/user")


def get_user(keyname):
    userdb = database.get("user")
    user = userdb.get(keyname)
    if user is None:
        return jsonify({"message": "User not found"}), 404
    return jsonify(user), 200


@user_route.route("", methods=["POST", "GET"])
@user_route.route("/<string:keyname>", methods=["GET"])
def user(keyname=None):
    """
    Greet a user
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: true
        description: The name of the user to greet
    responses:
      200:
        description: A greeting to the user
        schema:
          properties:
            greeting:
              type: string
              example: "Hello, John!"
    """

    if request.method == "POST":
        data = request.json
        username = data.get("username")
        password = data.get("password")
        fullname = data.get("fullname")
        userdb = database.get("user")
        if userdb.get(username) is not None:
            return jsonify({"message": "User already exists"}), 400
        userdb[username] = {
            "password": password,
            "fullname": fullname,
        }
        return jsonify(userdb[username]), 201
    elif request.method == "GET":
        userdb = database.get("user")
        if keyname is None:
            return jsonify(userdb), 200
        return get_user(keyname)
