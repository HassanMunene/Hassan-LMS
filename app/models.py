from flask import current_app
from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer

class User(db.Model, UserMixin):
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

    def __init__(self, username, email, password, IDno, role):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.IDno = IDno
        self.role = role

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def generate_signed_token(self):
        s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        token = s.dumps(self.email)
        return token

    def confirm(self, token):
        s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data == self.email:
            return True

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
