from flask import Blueprint, jsonify
from models.user import User
from utils.profile_utils import generate_fullname, generate_gmail

profile_route = Blueprint("profile", __name__, url_prefix="/profile")

@profile_route.route("", methods=["GET"])
def get_user_profile():
    users: list[User] = User.query.all()
    modified_response = []
    for user in users:
        modified_response.append({
            "full_name": generate_fullname(user.first_name, user.last_name),
            "email": generate_gmail(user.first_name)
        })
    return jsonify(modified_response), 200