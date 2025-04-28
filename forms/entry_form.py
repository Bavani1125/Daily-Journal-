from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired, Length
from datetime import datetime

class EntryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    date = DateField('Date', default=datetime.utcnow().date(), validators=[DataRequired()])
    submit = SubmitField('Save Entry')