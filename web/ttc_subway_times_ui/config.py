import os
from pathlib import Path


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
