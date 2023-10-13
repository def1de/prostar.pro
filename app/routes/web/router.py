from flask import Blueprint, redirect
from .en_route import web_en

lang_list = ["en"]
web = Blueprint("web", __name__)

web.register_blueprint(web_en, url_prefix="/en")

# @web.route("/")
# def set_lang():
#     return redirect("/en")

@web.route("/")
@web.route("/<path:url>")
def redirect_lang(url=""):
    if url.split('/')[0] in lang_list:
        return redirect(f"/{url}")
    else: return redirect(f"/en/{url}")
