from flask import Blueprint

web_admin = Blueprint("admin_panel", __name__, template_folder="templates/", static_folder="static/")

@web_admin.route("/")
def index_admin():
    return "Hello from admin"