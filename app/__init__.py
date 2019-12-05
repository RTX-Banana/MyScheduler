import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()

def create_app(test_config=Config):
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(test_config)
    db.init_app(app)
    login.init_app(app)
    login.init_app(app)
    login.login_view = 'login'

    with app.app_context():
        from . import routes
        db.create_all()
        return app