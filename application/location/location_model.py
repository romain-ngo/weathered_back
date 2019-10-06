from .. import db


class LocationModel(db.Model):
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(20), index=False,
                        unique=False, nullable=False)
    city = db.Column(db.String(20), index=False, unique=True, nullable=False)
    latitude = db.Column(db.Integer, index=False, unique=False, nullable=False)
    longitude = db.Column(db.Integer, index=False,
                          unique=False, nullable=False)

    def __repr__(self):
        return f"City {self.city}"
