import os

from flask import Flask
from flask_login import LoginManager 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login=LoginManager()

def create_app(test_config=None):
    #Creating and configuring the app
    app = Flask(__name__, instance_relative_config=False)
    
    if test_config is None:
        #Load config instance
        app.config.from_object('config.Config')
    else:
        app.config.from_mapping(test_config)
    
    db.init_app(app)
    login.init_app(app)
    login.login_view = 'login'
    
    with app.app_context():
        from.import routes
        db.create_all()
        return app
