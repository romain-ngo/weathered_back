from .user_model import UserModel
from .. import mallow


class UserSchema(mallow.ModelSchema):
    class Meta:
        model = UserModel
