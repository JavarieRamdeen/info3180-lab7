# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SubmitField, validators, SelectField, IntegerField, FileField
from wtforms.validators import DataRequired, InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg','png'], 'Images only!')])
    submit = SubmitField("Submit")