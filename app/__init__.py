import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from app.config import Config
from flask_moment import Moment
import logging
from flask_restful import Api, Resource

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
#logging.basicConfig(filename='error.log',level=logging.DEBUG)

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config())
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    moment = Moment(app)
    migrate.init_app(app, db)
    
    from app.main.routes import main
    app.register_blueprint(main)

    from app.users.routes import users
    app.register_blueprint(users)

    from app.device.routes import device
    app.register_blueprint(device)

    from app.errors.handlers import errors
    app.register_blueprint(errors)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    print("\n============================ MAPS ===============\n")
    print(app.url_map,'\n')


    with app.app_context():
        db.create_all()
    
    return app
    