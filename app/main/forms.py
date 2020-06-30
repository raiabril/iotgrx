from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from app.models import Event

class RealValueForm(FlaskForm):
    id = IntegerField('Id', render_kw={'readonly': True})
    value = FloatField('Raw',render_kw={'readonly': True})
    calibrated = FloatField('Calibrated', render_kw={'readonly': True})
    real_value = FloatField('Manual', validators=[DataRequired()])
    submit1 = SubmitField('Save')


class WateringForm(FlaskForm):
    id = IntegerField('Sensor id', render_kw={'readonly': True})
    name = StringField('Name')
    a0 = FloatField('a0', validators=[DataRequired()])
    a1 = FloatField('a1', validators=[DataRequired()])
    units = StringField('Units', validators=[DataRequired()])
    sensor_type = StringField('Sensor Type', validators=[DataRequired()])
    fit_type = SelectField('Fit type', choices=[('linear','y = a0 + a1*x'),('log','y = a0*e^a1')], validators=[DataRequired()])
    trigger = BooleanField('Watering trigger')
    level = FloatField('Water trigger level')
    submit2 = SubmitField('Save')