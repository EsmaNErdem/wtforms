"""Forms Pet model forms"""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional,Length, NumberRange, URL

class AddPetForm(FlaskForm):
    """Form for adding pet"""

    name = StringField("Pet Name",
                       validators=[InputRequired()],
                       )
    species = SelectField("Species",
                          choices=[('cat', 'Cat'), ('dog', 'Dog'), ("porcupine", "Porcupine")],)
    photo_url = StringField("Photo URL",
                       validators=[InputRequired(), URL()],)
    age = IntegerField("Pet age", 
                        validators=[Optional(), NumberRange(min=0, max=30)],)
    notes = TextAreaField("Additional Notes", 
                        validators=[Optional(),Length(min=10)],)



class EditPetForm(FlaskForm):
    """Forms for editting a pet"""
    photo_url = StringField("Photo URL",
                       validators=[InputRequired(), URL()],)
    notes = TextAreaField("Additional Notes", 
                        validators=[Optional(),Length(min=10)],)
    available = BooleanField("Still available?")
    