from flask import Blueprint, render_template, request, redirect, make_response, abort
from app.extentions import db
from app.models import Contact, Vacancies

web_en = Blueprint("en", __name__, template_folder="templates_en/", static_folder="static/")

@web_en.route("/")
def index_en():
    return render_template("index.html", jobs=Vacancies.query.order_by(Vacancies.id.desc()).limit(3))

@web_en.route('/jobs/')
def job_list():
    return render_template('job-list.html', data=Vacancies.query.
                           filter(Vacancies.isAvalible==1)
                           .order_by(Vacancies.id.desc())
                           .all()
                           )

@web_en.route('/jobs/<int:id>/')
def job_single(id):
    return render_template('job-single.html', data=Vacancies.query.get(id), other_vac=Vacancies.query.limit(4))

@web_en.route('/jobs/<int:id>/load_image')
def vacancie_img(id):
    img = Vacancies.query.get(id).img
    h = make_response(img)
    h.headers['Content-Type'] = 'img/png'
    return h

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

@web_en.route("/apply/", methods=["GET", "POST"])
def apply_en():
    return render_template("submit-listing.html")

@web_en.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')