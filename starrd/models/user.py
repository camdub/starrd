from starrd.models import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    auth_token = db.Column(db.String(), unique=True)
    repos = db.relationship("UserRepo", backref='user', lazy='dynamic')

users = UserService()
