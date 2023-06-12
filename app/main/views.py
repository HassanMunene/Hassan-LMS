from flask import Flask, render_template, redirect, url_for, session, flash
from .forms import LoginForm, RegisterForm
from . import main
from app import db, login_manager
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
        if user:
            if user.role=="admin" or user.role=="librarian":
                flash("Login successful")
                return redirect(url_for('main.index'))
            else:
                flash("Invalid User")
        else:
            flash("Invalide credentials")
        return redirect(url_for('main.login'))
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)
