__version__ = '0.1.0'

import os

from flask import Flask

from .config import init_config
from .routes import init_routes


def create_app(test_config=None):
    """Create and configure the app."""
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    init_config(app, test_config=test_config)
    init_routes(app)

    return app
