"""
register main as a blueprint
"""
from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates')
from . import views

