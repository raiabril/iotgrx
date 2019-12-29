from datetime import datetime
from flask import current_app
from app import db, login_manager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app import db, bcrypt
import base64
from datetime import datetime, timedelta
import os
from marshmallow import Schema, fields
import uuid


def uuid_gen():
    return str(uuid.uuid4())

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(30), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'],expires_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password,password)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'username': self.username
            }
        if include_email:
            data['email'] = self.email
        return data

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            setattr(self, 'password', bcrypt.generate_password_hash(data['password']).decode('utf-8'))

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)

    def __repr__(self):
        return f"Device('{self.id}','{self.name}')"


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False, index=True)
    
    def __repr__(self):
        return f"Device('{self.id}','{self.name}')"


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    value = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable=False, index=True)
    sensor = db.relationship('Sensor', lazy=True)

    def __repr__(self):
        return f"Device('{self.id}','{self.name}')"

    def to_dict(self):
        data = {
            'id': self.id,
            'date_created':self.date_created.strftime("%Y-%m-%d %H:%M:%S"),
            'value': self.value
            }
        return data