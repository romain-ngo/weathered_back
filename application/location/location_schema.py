from .location_model import LocationModel
from .. import mallow


class LocationSchema(mallow.ModelSchema):
    class Meta:
        model = LocationModel
