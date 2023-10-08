from flask import Blueprint, render_template

web_en = Blueprint("en", __name__, template_folder="templates_en/", static_folder="static/")

@web_en.route("/")
def index_en():
    return render_template("index.html")