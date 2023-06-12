from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    idno = StringField('Enter your Id', validators=[DataRequired()])
    password = PasswordField('Enter your password', validators=[DataRequired()])
    submit =SubmitField('submit')

class RegisterForm(FlaskForm):
    username = StringField('Enter your username', validators=[DataRequired()])
    email = StringField('Enter your email', validators=[DataRequired(), Email()])
    password = PasswordField('Enter you password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

