from app import db


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True, nullable=False)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(512), unique=True, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.email)
