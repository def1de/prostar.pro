from flask import Blueprint, render_template, request, redirect
from ...extentions import db
from ...models import Contact

web_en = Blueprint("en", __name__, template_folder="templates_en/", static_folder="static/")

@web_en.route("/")
def index_en():
    return render_template("index.html")

@web_en.route("/contact/", methods=["GET", "POST"])
def contact_en():
    if request.method == "POST":
        name = request.form['fname']
        email = request.form['email']
        title = request.form['subject']
        message = request.form['comment']
        db.session.add(Contact(name=name, email=email, title=title, message=message))
        db.session.commit()
        return redirect('/contact')
    else:
        return render_template("contact-us.html")