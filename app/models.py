
from . import db

class User(db.Model):
    """
    the user table model
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True, index=True)
    role = db.Column(db.String(64))
    password = db.Column(db.String(64), unique=True)
    IDno = db.Column(db.String(64), unique=True)

