from flask import Flask, render_template, redirect, url_for, session, flash
from .forms import LoginForm, RegisterForm
from . import main
from app import db, login_manager
from app.models import User
from flask_login import login_user

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
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user and user.verify_password(password):
            login_user(user)
            if user.role == 'admin':
                flash("logged in as admin")
            elif user.role == 'librarian':
                flash("logged in as librarian")
            else:
                flash("logged in as student")
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        IDno = form.idno.data
        role = form.role.data

        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username, email, password, IDno, role)
            db.session.add(user)
            db.session.commit()
            flash('user registered successfully')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)





