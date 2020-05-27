from flask import Flask

from configs import ConfigDealer


def create_app(config_name: str) -> Flask:
    """Создание объекта точки входа приложаения"""
    app = Flask(__name__)
    config = ConfigDealer.get_main(config_name)
    app.config.from_object(config)
    config.init_app(app)
    from .api import api
    app.register_blueprint(api, url_prefix='/api/v1')
    return app
