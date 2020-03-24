from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from flask_login import current_user
from app.models import User

class WaterForm(FlaskForm):
    duration = IntegerField('Time to water (millis)', validators=[DataRequired(), NumberRange(min=0, max=10000, message="Max is 10000!")])
    submit = SubmitField('Water!')