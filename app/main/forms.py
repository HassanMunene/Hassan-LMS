from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    name = StringField('What\'s your name?', validators=[DataRequired()])
    email = StringField('Enter your email', validators=[DataRequired(), Email()])
    submit =SubmitField('submit')
