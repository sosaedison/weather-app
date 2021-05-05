from flask import Flask
from flask_caching import Cache
from weather_app.views import static, search_by


def create_app():
    app_ = Flask(__name__, instance_relative_config=True)
    app_.register_blueprint(static.mod)
    app_.register_blueprint(search_by.mod, url_prefix="/search_by")

    config = {
        "DEBUG": True,
        "CACHE_TYPE": "SimpleCache",
        "CACHE_DEFAULT_TIMEOUT": 300,
        "SECRET_KEY": "secret",
    }

    app_.config.from_mapping(config)

    cache = Cache(app_)
    return app_


app = create_app()
