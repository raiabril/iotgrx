from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from app.models import Event

class RealValueForm(FlaskForm):
    id = IntegerField('Id', render_kw={'readonly': True})
    real_value = FloatField('Manual')
    submit = SubmitField('Save')