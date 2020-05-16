from .configs import ConfigFtp44, api_links, main_config

from os import environ
from flask import Flask


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(main_config[config_name])
    main_config[config_name].init_app(app)
    from .api import api
    app.register_blueprint(api, url_prefix='/api/v1')
    return app


app = create_app(environ.get('APP_MODE') or 'development')


@app.shell_context_processor
def make_shell_context():
    return dict()
