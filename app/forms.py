from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search = StringField('Enter your search with tags seperated by commas!', validators=[DataRequired()])
    submit = SubmitField('Search')
