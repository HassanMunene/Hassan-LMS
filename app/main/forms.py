from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    username = StringField('Enter you name', validators=[DataRequired()])
    regno = StringField('Enter Reg No:', validators=[DataRequired()])
    email = StringField('Enter your email', validators=[DataRequired()])
    submit =SubmitField('submit')
