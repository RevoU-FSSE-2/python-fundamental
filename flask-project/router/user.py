from flask import Blueprint, jsonify, request
from config import settings

user_route = Blueprint("user", __name__, url_prefix="/user")


def get_user(keyname):
    user:settings.User = settings.User.query.filter_by(first_name=keyname).first()
    if user is None:
        return jsonify({"message": "User not found"}), 404
    return jsonify(user.to_dict(rules=('-password',))), 200


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
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        password = data.get("password")
        user = settings.User(first_name=first_name, last_name=last_name, password=password)
        settings.db.session.add(user)
        settings.db.session.commit()
        return jsonify({"id": user.id}), 201
    elif request.method == "GET":
        users: list[settings.User] = settings.User.query.all()
        response = []
        for user in users:
            response.append(user.to_dict(rules=('-password',)))
        if keyname is None:
            return jsonify(response), 200
        return get_user(keyname)
