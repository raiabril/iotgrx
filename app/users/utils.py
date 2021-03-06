import os
import secrets
from PIL import Image
from flask import url_for, current_app, render_template
from flask_mail import Message
from app import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex+f_ext.lower()
    picture_path = os.path.join(current_app.root_path,'static/profile_pics',picture_fn)
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset request',
                  sender=('iotGRX','raiabril.grx6@gmail.com'), 
                  recipients=[user.email])
    msg.html = render_template('email/reset-password.html', 
                                reset_password_url=url_for('users.reset_token',token=token,_external=True))
    msg.body = render_template('email/reset-password.txt', 
                                reset_password_url=url_for('users.reset_token',token=token,_external=True))
    mail.send(msg)


def send_welcome_email(user):
    msg = Message('Welcome to iotGRX',
                  sender=('iotGRX','raiablp@gmail.com'), 
                  recipients=[user.email])
    msg.html = render_template('email/welcome.html')
    msg.body = render_template('email/welcome.txt')
    mail.send(msg)


def send_notification_email(user, resource):
    msg = Message('Notification',
                  sender=('iotGRX','raiabril.grx6@gmail.com'), 
                  recipients=[user.email])
    msg.html = render_template('email/notification.html')
    msg.body = render_template('email/notification.txt')
    mail.send(msg)