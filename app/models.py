from . import db

class User(db.Model):
    """
    the user table model
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True, index=True)
    RegNumber= db.Column(db.String(64), unique=True)

