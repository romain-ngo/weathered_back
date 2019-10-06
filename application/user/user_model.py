from .. import db
from ..location.location_model import LocationModel


# Join table
userLocations = db.Table('userLocations',
                         db.Column('user_id', db.Integer, db.ForeignKey(
                             'user.id'), primary_key=True),
                         db.Column('location.id', db.Integer, db.ForeignKey(
                             'location.id'), primary_key=True))


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=False, unique=True, nullable=False)
    username = db.Column(db.String(30), index=False,
                         unique=True, nullable=False)
    password = db.Column(db.String(512), index=False,
                         unique=True, nullable=False)
    locations = db.relationship(LocationModel, secondary=userLocations,
                                lazy='subquery', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f"User {self.username}"
