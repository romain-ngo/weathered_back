from flask import Blueprint

userRoute = Blueprint('userRoute', __name__)


@userRoute.route('/users')
def get_users():
    return 'hello'
