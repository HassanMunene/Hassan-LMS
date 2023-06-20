from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired


class RegisterBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author =StringField('Author', validators=[DataRequired()])
    isbn = StringField('ISBN', validators=[DataRequired()])
    publisher = StringField('Publisher', validators=[DataRequired()])
    publication_date = DateField('Publication Date')
    genre = StringField('Genre')
    condition = SelectField('Condition', choices=[('new','New'), ('used', 'Used'), ('damaged', 'Damaged')])
    submit = SubmitField('Register')
