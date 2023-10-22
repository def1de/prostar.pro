from flask import Blueprint, redirect
import textwrap
from .en_route import web_en

lang_list = ["en"]
web = Blueprint("web", __name__)

web.register_blueprint(web_en, url_prefix="/en")

@web.app_template_filter('make_shorter')
def make_shorter(filtering_str, filtering_width=40):
    return textwrap.shorten(filtering_str, width=filtering_width, placeholder="...")

@web.route("/")
@web.route("/<path:url>")
def redirect_lang(url=""):
    if url.split('/')[0] in lang_list:
        return redirect(f"/{url}")
    else: return redirect(f"/en/{url}")
