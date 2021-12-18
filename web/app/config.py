""" 
    This is the main config class.
    - Flask configuration.
    - SQL alchemy configuration.
    - Mail server.
"""


class Config:
    # Setup a Sectet Key
    SECRET_KEY = 'dadc98d2ce2925035ffc2bdc6ce3c190'

    # SQLALCHEMY data
    SQLALCHEMY_POOL_RECYCLE = 3600
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/iotHome.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email Address
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'raiablp@gmail.com'
    MAIL_PASSWORD = ''
