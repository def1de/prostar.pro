from .extentions import db

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