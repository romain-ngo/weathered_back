from flask import Blueprint, request, make_response, jsonify
from .user_model import db, UserModel
from ..location.location_model import LocationModel
from .user_schema import UserSchema
from .. import bcrypt

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/users', methods=['GET'])
def get_users():
    user_schema = UserSchema(many=True)
    result = UserModel.query.all()
    print(result[0].locations)
    return make_response(jsonify(user_schema.dump(result)), 200)


@user_bp.route('/user', methods=['POST'])
def create_user():
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']

    if email and username and password:
        user_exists = UserModel.query.filter(
            UserModel.email == email).first()
        if user_exists:
            return make_response(f"this email already exist", 400)

        hashed_password = bcrypt.generate_password_hash(
            password).decode('utf-8')

        new_user = UserModel(email=email, username=username,
                             password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return make_response(f"{username} created", 201)
    else:
        return make_response("error in the request", 400)

# TODO Must return email, username and JWT
@user_bp.route('/login', methods=['GET'])
def user_login():
    email = request.json['email']
    password = request.json['password']
    user = UserModel.query.filter(UserModel.email == email).first()
    if not user:
        return make_response("this email does not exist", 400)
    else:
        password_is_matching = bcrypt.check_password_hash(
            user.password, password)
        if password_is_matching:
            return make_response("ok", 200)
        else:
            return make_response("wrong password", 400)


@user_bp.route('/user/<user_id>/location', methods=['POST'])
def add_location_to_user(user_id):
    user = UserModel.query.filter(UserModel.id == user_id).first()
    location_id = request.json['locationId']
    location = LocationModel.query.filter(
        LocationModel.id == location_id).first()
    user.locations.append(location)
    db.session.commit()
    return make_response(f"location {location_id} added to {user.email}", 201)
