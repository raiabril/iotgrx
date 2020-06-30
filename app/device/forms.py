from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from flask_login import current_user
from app.models import User

class WaterForm(FlaskForm):
    duration = FloatField('Time to water (s)', validators=[DataRequired(), NumberRange(min=0, max=100, message="Max is 100s!")])
    submit = SubmitField('Water!')