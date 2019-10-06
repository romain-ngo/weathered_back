from .user_model import UserModel
from ..location.location_schema import LocationSchema
from .. import mallow


class UserSchema(mallow.ModelSchema):

    location = mallow.Nested(LocationSchema, many=True)

    class Meta:
        model = UserModel
