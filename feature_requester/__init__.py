from flask import Flask

from feature_requester.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from feature_requester.api.routes import api
    from feature_requester.site.routes import site

    app.register_blueprint(site)
    app.register_blueprint(api, url_prefix='/api')

    return app
