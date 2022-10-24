from flask import Flask, make_response, redirect, render_template, url_for, request, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, current_user, login_required, login_user, logout_user
import textwrap
import time

#<============== INIT ==============>

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prostar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '0123456789'

@app.template_filter('make_shorter')
def make_shorter(filtering_str, filtering_width=40):
    return textwrap.shorten(filtering_str, width=filtering_width, placeholder="...")

@app.template_filter('hide_password')
def hide_password(filtering_str):
    return '*'*len(str(filtering_str))

db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = "log_in"


#<============== TABLES ==============>

class Admins(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    job_title = db.Column(db.String(255))
    img = db.Column(db.LargeBinary, default=None)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(255), default=time.strftime("%d.%m.%Y %H:%M", time.localtime()))
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    title = db.Column(db.String(255), default="-")
    message = db.Column(db.Text, default="-")
    isDone = db.Column(db.Boolean, default=False)
    commit = db.Column(db.String(255), default=None)

class Vacancies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable = False)
    post_time = db.Column(db.String(255), default=time.strftime("%d.%m.%Y", time.localtime()))
    schedule = db.Column(db.String(255), default="-")
    location = db.Column(db.String(255), default="-")
    hourly_rate = db.Column(db.String(255), default="-")
    salary = db.Column(db.String(255), default="-")
    vac_id = db.Column(db.String(255), default="-")
    description = db.Column(db.Text, default="-")
    isAvalible = db.Column(db.Boolean, default=False)
    img = db.Column(db.LargeBinary, default=None)
    apply_link = db.Column(db.Text, default=None)

class Emails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), default=None)

#<============== ADMIN-CLASSES ==============>

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('log_in'))

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('log_in'))

@login.user_loader
def load_user(user_id):
    return Admins.query.get(user_id)    

#<============== ADMIN-INIT ==============>

admin = Admin(app, index_view=MyAdminIndexView())

#<============== PAGES ==============>

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form['socialsEmail']
        try:
            db.session.add(Emails(email=email))
            db.session.commit()
            flash('Ви підписалися на розсилку.')
        except: flash('Помилка. Спробуйте ще раз.')
        return redirect('/')
    else: return render_template('index.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        title = request.form['title']
        message = request.form['message']
        db.session.add(Contact(name=name, email=email, title=title, message=message))
        db.session.commit()
        return redirect('/contact')
    else:
        qid = request.args.get('vac', default = '', type = str)
        if qid != "": return render_template('contact.html', question = f"Питання щодо вакансії \"{Vacancies.query.get(int(qid)).title}\" ({qid})")
        else: return render_template('contact.html', question = "")

@app.route('/vacancies')
def vacancies():
    return render_template('vacancies.html', data=Vacancies.query.order_by(Vacancies.id.desc()).all())

@app.route('/vacancies/<int:id>')
def post(id):
    if Vacancies.query.get_or_404(id).isAvalible == True:
        return render_template('single-vacancie.html', data=Vacancies.query.get(id), other_vac=Vacancies.query.limit(4))
    else: return abort(404)

@app.route('/vacancies/<int:id>/load_image')
def vacancie_img(id):
    img = Vacancies.query.get(id).img
    h = make_response(img)
    h.headers['Content-Type'] = 'img/png'
    return h

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

#<============== ADMIN-PAGES ==============>
@app.route('/admin/dashboard')
@login_required
def administrator():
    return render_template('/admin/dashboard.html', user=Admins.query.get(current_user.get_id()), vacancies=Vacancies.query.order_by(Vacancies.id.desc()).limit(3), admins = Admins.query.limit(3), contact=Contact.query.order_by(Contact.id.desc()).limit(4))

@app.route('/admin/login', methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        for i in Admins.query.all():
            if username == i.username:
                if password == i.password:
                    user = i
                    login_user(user)
                    return redirect('/admin')
        return redirect('/admin/login')
    else:
        if current_user.is_authenticated == True:
            return redirect('/admin')
        else: return render_template('/admin/login.html')

@app.route('/admin/logout')
@login_required
def logout():
    logout_user()
    return redirect('/admin/login')

#================================================================

@app.route('/admin/contact/', methods=["GET", "POST"])
@login_required
def data_contact():
    return render_template('/admin/contact.html', data=Contact.query.order_by(Contact.id.desc()).all(), user=Admins.query.get(current_user.get_id()))

@app.route('/admin/contact/<int:id>/done', methods=["GET", "POST"])
@login_required
def data_contact_read(id):
    Contact.query.get(id).isDone = True
    Contact.query.get(id).commit = f"Виконав(ла): {Admins.query.get(current_user.get_id()).name} Час: {time.strftime('%d.%m.%Y %H:%M', time.localtime())}"
    db.session.commit()
    flash(f"Звертання #{id} відмічено як виконане")
    return redirect('/admin/contact/')

#================================================================

@app.route('/admin/vacancies/', methods=["GET", "POST"])
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

    else: return render_template('/admin/vacancies.html', data=Vacancies.query.order_by(Vacancies.id.desc()).all(), user=Admins.query.get(current_user.get_id()))

@app.route('/admin/vacancies/<int:id>/delete')
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

@app.route('/admin/vacancies/<int:id>/hide')
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

@app.route('/admin/vacancies/<int:id>/edit', methods=["GET", "POST"])
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

    else: return render_template('/admin/edit_vacancie.html', data=Vacancies.query.get(id), user=Admins.query.get(current_user.get_id()))

#================================================================

@app.route('/admin/admins', methods=["GET", "POST"])
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
        return redirect("/admin/admins")

    else: return render_template('/admin/admins.html', data=Admins.query.all(), user=Admins.query.get(current_user.get_id()))

@app.route('/admin/admins/<int:id>/delete')
@login_required
def data_admins_delete(id):
    try:
        db.session.delete(Admins.query.get_or_404(id))
        db.session.commit()
        return redirect('/admin/admins')
    except:
        return "<h1>Error</h1"

@app.route('/admin/load_avatar/<int:id>')
def get_img(id):
    img = Admins.query.get(id).img
    h = make_response(img)
    h.headers['Content-Type'] = 'img/png'
    return h

#================================================================

@app.route('/admin/emails/')
@login_required
def data_emails(): return render_template('/admin/emails.html', data=Emails.query.order_by(Emails.id.desc()).all(), user=Admins.query.get(current_user.get_id()))

@app.route('/admin/emails/<int:id>/delete')
@login_required
def data_emails_delete(id):
    try:
        db.session.delete(Emails.query.get_or_404(id))
        db.session.commit()
        return redirect('/admin/emails')
    except:
        return "<h1>Error</h1"

#<============== START ==============>

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)