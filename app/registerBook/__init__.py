"""
register books blueprint
"""
from flask import Blueprint

regBook = Blueprint('regBook', __name__, template_folder='templates')
from . import views
