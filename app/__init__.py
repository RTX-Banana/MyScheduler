import os

from flask import Flask
from config import Config
from flask_login import LoginManager 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#app = Flask(__name__)
#app.config.from_object(Config)

#db = SQLAlchemy(app)
migrate=Migrate (app,db)
login=LoginManager(app)
login.login_view='login'

#from app import routes, models

#db = SQLAlchemy()
#login=LoginManager()

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
        from . import routes
        db.create_all()
        return app
