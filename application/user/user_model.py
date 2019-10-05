from .. import db


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=False, unique=True, nullable=False)
    username = db.Column(db.String(30), index=False,
                         unique=True, nullable=False)
    password = db.Column(db.String(512), index=False,
                         unique=True, nullable=False)

    def __repr__(self):
        return f"User {self.username}"
