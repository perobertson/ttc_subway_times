__version__ = '0.1.0'

import os
from pathlib import Path

from flask import Flask


def create_app(test_config=None):
    """Create and configure the app."""
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    init_config(app, test_config=test_config)
    add_routes(app)

    return app


def init_config(app, test_config=None):
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        config_json = Path('config').joinpath("{}.json".format(app.env))
        app.config.from_json(config_json, silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)


def add_routes(app):
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
