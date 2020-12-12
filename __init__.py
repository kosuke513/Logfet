import os

from flask import Flask
from database import db
from config import Local,Product


def create_app(test_config=None):
    try:
        import googleclouddebugger
        googleclouddebugger.enable(
            breakpoint_enable_canary=True
            )
    except ImportError:
        pass

    # create and configure the app
    app = Flask(__name__)

    if os.getenv("GAE_ENV", "").startswith("standard"):
        """Production in GAE."""
        app.config.from_object(Product)
        db.init_app(app)

    else:
        """Local Development Server."""
        app.config.from_object(Local)
        db.init_app(app)

        try:
            os.makedirs(app.instance_path)
        except OSError:
            pass

    return app


print(__name__)