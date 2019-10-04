from flask import Blueprint, request, make_response
from .user_model import db, UserModel


user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/users', methods=['GET'])
def get_users():
    return UserModel.object.all()


@user_bp.route('/user', methods=['POST'])
def create_user():
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']

    if email and username and password:
        new_user = UserModel(email=email, username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return make_response(f"{new_user} created.")
    else:
        return make_response(f"Error in the request")
