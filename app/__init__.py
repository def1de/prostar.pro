from flask import Flask
from .extentions import db, admin, login
from .routes.web.router import web
from .routes.admin.admin_route import web_admin


def create_app():
    app = Flask(__name__)
    app.register_blueprint(web)
    app.register_blueprint(web_admin, url_prefix="/admin")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    db.init_app(app)
    admin.init_app(app)
    login.init_app(app)

    return app