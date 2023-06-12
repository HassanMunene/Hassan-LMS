from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Enter your username', validators=[DataRequired()])
    password = PasswordField('Enter your password', validators=[DataRequired()])
    submit =SubmitField('submit')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    idno = StringField('Id no', validators=[DataRequired()])
    role = SelectField('Role', choices=[('admin','Admin'), ('librarian', 'Librarian'), ('student', 'Student')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

class ResetEmail2(FlaskForm):
    username = StringField('New username', validators=[DataRequired()])
    password = PasswordField('New password', validators=[DataRequired(), EqualTo('password2', message='passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Reset')

class ResetEmail(FlaskForm):
    email = StringField('Enter your email', validators=[DataRequired(), Email()])
    submit = SubmitField('Reset')
