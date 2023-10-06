from flask import Blueprint

web_en = Blueprint("en", __name__, template_folder="templates/", static_folder="static/")

@web_en.route("/")
def index_en():
    return "<p>Hello from EN</p>"