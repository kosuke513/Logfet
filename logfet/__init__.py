import os

from flask import Flask
from .database import db
from .views.user import user
from .views.post import post
import config

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = 'super secret key'

    app.config.from_object('config.Config')
    db.init_app(app)

    app.register_blueprint(user)
    app.register_blueprint(post)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app