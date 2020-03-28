from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from app.models import Event

class RealValueForm(FlaskForm):
    id = IntegerField('Id', render_kw={'readonly': True})
    calibrated = FloatField('Calibrated', render_kw={'readonly': True})
    real_value = FloatField('Manual')
    submit1 = SubmitField('Save')


class WateringForm(FlaskForm):
    id = IntegerField('Sensor id', render_kw={'readonly': True})
    a0 = FloatField('a0')
    a1 = FloatField('a1')
    trigger = BooleanField('Activate')
    level = IntegerField('Level')
    submit2 = SubmitField('Save')