from flask import jsonify

from config.settings import create_app
from models.user import User

app = create_app()


@app.route("/")
def hello_world():
    users: list[User] = User.query.all()
    response = {}
    for user in users:
        response[user.id] = {"fullname": f"{user.first_name} {user.last_name}"}
    return jsonify(response), 200
