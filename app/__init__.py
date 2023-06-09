from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail


db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .registerBook import regBook as regBook_blueprint
    app.register_blueprint(regBook_blueprint)

    return app
