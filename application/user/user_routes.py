from flask import Blueprint, request, make_response, jsonify
from .user_model import db, UserModel
from .user_schema import UserSchema
from ..location.location_model import LocationModel
from .. import bcrypt

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/users', methods=['GET'])
def get_users():
    user_schema = UserSchema(many=True)
    result = UserModel.query.all()
    return make_response(jsonify(user_schema.dump(result)), 200)


@user_bp.route('/user', methods=['POST'])
def create_user():
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']

    if not email:
        return make_response("email field missing", 400)
    if not username:
        return make_response("username field missing", 400)
    if not password:
        return make_response("password field missing", 400)

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


@user_bp.route('/user', methods=['PUT'])
def edit_user():
    id = request.json['id']
    email = request.json['email']
    username = request.json['username']
    current_password = request.json['currentPassword']
    new_password = request.json['newPassword']
    if not id:
        return make_response("missing id field", 400)

    user = UserModel.query.filter(UserModel.id == id).first()
    if len(email) > 0:
        user.email = email
    if len(username) > 0:
        user.username = username
    if len(new_password) > 0:
        if bcrypt.check_password_hash(user.password, current_password):
            user.password = bcrypt.generate_password_hash(
                new_password).decode('utf-8')
        else:
            return make_response("wrong password", 401)
    db.session.commit()
    return make_response("ok", 200)

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
            return make_response("wrong password", 401)


@user_bp.route('/user/<user_id>/location', methods=['POST'])
def add_location_to_user(user_id):
    user = UserModel.query.filter(UserModel.id == user_id).first()
    location_id = request.json['locationId']
    if not location_id:
        return make_response("locationId field missing", 400)
    location = LocationModel.query.filter(
        LocationModel.id == location_id).first()
    user.locations.append(location)
    db.session.commit()
    return make_response(f"location {location_id} added to {user.email}", 201)
