from typing import Sized
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms import validators
from wtforms.validators import DataRequired

class TodoFormProject(FlaskForm):
    name = StringField('name' , validators=[DataRequired()])
    start_date = TextAreaField('start_date',validators=[DataRequired()])
    end_date = TextAreaField('end_date',validators=[DataRequired()])