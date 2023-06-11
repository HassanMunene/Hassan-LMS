from flask import Flask, render_template, redirect, url_for, session
from .forms import LoginForm
from . import main
from app import db
from app.models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    if 'logged_in' in session:
        return render_template('index.html', logged_in=True)
    else:
        return render_template('index.html', logged_in=False)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

