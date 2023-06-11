from . import db

class User(db.Model):
    """
    the user table model
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True, index=True)
    regno= db.Column(db.String(64), unique=True)

