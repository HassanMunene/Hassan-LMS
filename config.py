import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    This is the base configuration class
    """
    SECRET_KEY = 'hard to guess secret key'
    SQLALCHEMY_TRACK_MODIFICATIONS =False
    FLASKY_ADMIN = 'devtools14347@outlook.com'
    FLASKY_LIBRARIAN = 'devtools214347@outlook.com'
    MAIL_SERVER = 'smtp.office365.com'
    MAIL_DEFAULT_SENDER = 'devtools14347@outlook.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_DEBUG = False
    MAIL_USERNAME = 'devtools14347@outlook.com'
    MAIL_PASSWORD = 'Munene14347'

    @staticmethod
    def init_app(app):
        pass

class Development(Config):
    """
    specific only for the development
    environment
    """
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
        'development': Development
        }
