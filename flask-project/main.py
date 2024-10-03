from flask import jsonify
from router.auth import auth_router
from router.user import user_route
from config import settings

app = settings.app

app.register_blueprint(auth_router)
app.register_blueprint(user_route)
@app.route("/")
def hello_world():
    users: list[settings.User] = settings.User.query.all()
    response = {}
    for user in users:
        response[user.id] = {"fullname": 
            f"{user.first_name} {user.last_name}"
            }
    return jsonify(response), 200