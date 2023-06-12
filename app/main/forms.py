from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    idno = StringField('Enter your Id', validators=[DataRequired()])
    password = PasswordField('Enter your password', validators=[DataRequired()])
    submit =SubmitField('submit')
