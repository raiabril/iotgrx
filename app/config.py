class Config:
    # Setup a Sectet Key
    SECRET_KEY='dadc98d2ce2925035ffc2bdc6ce3c190'
    SQLALCHEMY_POOL_RECYCLE = 3600
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/iotHome.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # Email Address
    MAIL_USERNAME = 'raiablp@gmail.com'
    # Email Password
    MAIL_PASSWORD = ''