from flask import Blueprint
from .en_route import web_en

web = Blueprint("web", __name__)

web.register_blueprint(web_en, url_prefix="/en")