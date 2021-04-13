from flask import Flask
from weather_app.views import static, search_by


def create_app():
    app_ = Flask(__name__, instance_relative_config=True)
    app_.register_blueprint(static.mod)
    app_.register_blueprint(search_by.mod, url_prefix="/search/by")
    app_.config.from_mapping(
        SECRET_KEY="secret", WEATHER_API_KEY="376944731769fe3b16fb7cb9d65da026"
    )

    return app_


app = create_app()

# app.before_request
# def somefunction

# app.errorhandler(401)
# def somefunction