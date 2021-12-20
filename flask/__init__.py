#!/usr/bin/python3
import os

from flask import Flask
from flask_login import LoginManager
from .models import UserBase


def create_app():
    app = Flask(__name__)
    app.secret_key = 'hdsfjkhdsjfk'

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for upload routes in our app
    from .upload import upload as upload_blueprint
    app.register_blueprint(upload_blueprint)

    # blueprint for auto_index routes in our app
    from .autoindex import autoindex as upload_autoindex
    app.register_blueprint(upload_autoindex, url_prefix='/files')

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # return UserBase.session[user_id]
        return UserBase.logins['user']

    return app

