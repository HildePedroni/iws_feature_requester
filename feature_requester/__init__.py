from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from feature_requester.config import Config

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    ma.init_app(app)

    from feature_requester.api.routes import api
    from feature_requester.site.routes import site

    app.register_blueprint(site)
    app.register_blueprint(api, url_prefix='/api')

    return app
