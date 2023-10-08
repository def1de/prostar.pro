from flask import Blueprint, render_template, request, redirect, make_response
from flask_login import login_required, current_user, login_user, logout_user

from app.models import *

web_admin = Blueprint("admin_panel", __name__, template_folder="templates/", static_folder="static/")

@web_admin.app_template_filter('make_shorter')
def make_shorter(filtering_str, filtering_width=40):
    return textwrap.shorten(filtering_str, width=filtering_width, placeholder="...")

@web_admin.app_template_filter('hide_password')
def hide_password(filtering_str):
    return '*'*len(str(filtering_str))

@web_admin.route('/dashboard')
@login_required
def administrator():
    return render_template('dashboard.html', user=Admins.query.get(current_user.get_id()), vacancies=Vacancies.query.order_by(Vacancies.id.desc()).limit(3), admins = Admins.query.limit(3), contact=Contact.query.order_by(Contact.id.desc()).limit(4))

@web_admin.route('/login', methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        for i in Admins.query.all():
            if username == i.username:
                if password == i.password:
                    user = i
                    login_user(user)
                    return redirect('/admin/dashboard')
        return redirect('/admin/login')
    else:
        if current_user.is_authenticated == True:
            return redirect('/admin/admin')
        else: return render_template('login.html')

@web_admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/admin/login')

#================================================================

@web_admin.route('/contact/', methods=["GET", "POST"])
@login_required
def data_contact():
    return render_template('contact.html', data=Contact.query.order_by(Contact.id.desc()).all(), user=Admins.query.get(current_user.get_id()))

@web_admin.route('/contact/<int:id>/done', methods=["GET", "POST"])
@login_required
def data_contact_read(id):
    Contact.query.get(id).isDone = True
    Contact.query.get(id).commit = f"Виконав(ла): {Admins.query.get(current_user.get_id()).name} Час: {time.strftime('%d.%m.%Y %H:%M', time.localtime())}"
    db.session.commit()
    flash(f"Звертання #{id} відмічено як виконане")
    return redirect('/admin/contact/')

#================================================================

@web_admin.route('/vacancies/', methods=["GET", "POST"])
@login_required
def data_vacancies():
    if request.method == "POST":
        title = request.form['title']
        location = request.form['location']
        hourly_rate = request.form['hourly_rate']
        salary = request.form['salary']
        vac_id = request.form['vac_id']
        schedule = request.form['schedule']
        description = request.form['description']
        img = request.files['img']
        binary = img.read()
        apply_link = request.form['apply_link']
        try:
            db.session.add(Vacancies(title = title, location = location, hourly_rate=hourly_rate, salary = salary, schedule=schedule, vac_id = vac_id, description=description, img = binary, apply_link = apply_link))
            db.session.commit()
            return redirect('/admin/vacancies')
        except: return "<h1>Error</h1>"

    else: return render_template('vacancies.html', data=Vacancies.query.order_by(Vacancies.id.desc()).all(), user=Admins.query.get(current_user.get_id()))

@web_admin.route('/vacancies/<int:id>/delete')
@login_required
def data_vacancies_delete(id):
    try:
        db.session.delete(Vacancies.query.get_or_404(id))
        db.session.commit()
        flash(f"Вакансія #{id} видалена")
    except:
        flash(f"Вакансія #{id} не видалена")
    finally:
        return redirect('/admin/vacancies')

@web_admin.route('/vacancies/<int:id>/hide')
@login_required
def data_vacancies_hide(id):
    if Vacancies.query.get(id).isAvalible == True:
        try:
            Vacancies.query.get(id).isAvalible = False
            db.session.commit()
            flash(f"Вакансія #{id} прихована")
        except:
            flash(f"Вакансія #{id} не прихована")
        finally:
            return redirect('/admin/vacancies')
    else:
        try:
            Vacancies.query.get(id).isAvalible = True
            db.session.commit()
            flash(f"Вакансія #{id} не прихована")
        except: 
            flash(f"Вакансія #{id} прихована")
        finally:
            return redirect('/admin/vacancies')

@web_admin.route('/vacancies/<int:id>/edit', methods=["GET", "POST"])
def data_vacancies_edit(id):
    if request.method == "POST":
        Vacancies.query.get(id).title = request.form['title']
        Vacancies.query.get(id).location = request.form['location']
        Vacancies.query.get(id).hourly_rate = request.form['hourly_rate']
        Vacancies.query.get(id).salary = request.form['salary']
        Vacancies.query.get(id).vac_id = request.form['vac_id']
        Vacancies.query.get(id).description = request.form['description']
        Vacancies.query.get(id).apply_link = request.form['apply_link']
        img = request.files['img']
        binary = img.read()
        if binary is not None: Vacancies.query.get(id).img = binary
        Vacancies.query.get(id).isAvalible = False
        try:
            db.session.commit()
            flash("Вакансія оновлена")
            return redirect('/admin/vacancies')
        except:
            flash("Помилка при збереженні данних. Спробуйте ще раз")
            return redirect('/admin/vacancies')

    else: return render_template('edit_vacancie.html', data=Vacancies.query.get(id), user=Admins.query.get(current_user.get_id()))

#================================================================

@web_admin.route('/admins', methods=["GET", "POST"])
@login_required
def data_admins():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        job_title = request.form['job_title']
        email = request.form['email']
        img = request.files['image']
        if not img:
            try:
                with app.open_resource(app.root_path + url_for('static', filename='img/admin/logo.png'), "rb") as f:
                    binary = f.read()
            except: return "<h1>Error</h1>"
        else:
            try:
                binary = img.read()
            except: return "<h1>Error</h1>"

        db.session.add(Admins(username=username, password=password, name=name, job_title=job_title, email=email, img=binary))
        db.session.commit()
        return redirect("/admins")

    else: return render_template('admins.html', data=Admins.query.all(), user=Admins.query.get(current_user.get_id()))

@web_admin.route('/admins/<int:id>/delete')
@login_required
def data_admins_delete(id):
    try:
        db.session.delete(Admins.query.get_or_404(id))
        db.session.commit()
        return redirect('/admin/admins')
    except:
        return "<h1>Error</h1"

@web_admin.route('/load_avatar/<int:id>')
def get_img(id):
    img = Admins.query.get(id).img
    h = make_response(img)
    h.headers['Content-Type'] = 'img/png'
    return h

#================================================================

@web_admin.route('/emails/')
@login_required
def data_emails(): return render_template('emails.html', data=Emails.query.order_by(Emails.id.desc()).all(), user=Admins.query.get(current_user.get_id()))

@web_admin.route('/emails/<int:id>/delete')
@login_required
def data_emails_delete(id):
    try:
        db.session.delete(Emails.query.get_or_404(id))
        db.session.commit()
        return redirect('/admin/emails')
    except:
        return "<h1>Error</h1"