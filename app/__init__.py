from flask import Flask
from .extentions import db, admin, login
from .routes.web.router import web
from .routes.admin.admin_route import web_admin
from .login_manager import load_user
import os
from .models import *
import click

app = Flask(__name__)
app.register_blueprint(web)
app.register_blueprint(web_admin, url_prefix="/admin")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///prostar.sqlite3"
app.config['SECRET_KEY'] = '0123456789'

db.init_app(app)
admin.init_app(app)
login.init_app(app)
login.login_view = "admin_panel.log_in"

@app.cli.command("init-db")
def init_db():
    """Initialize the database."""
    db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', '')
    if not os.path.exists(db_path):
        with app.app_context():
            db.create_all()
            # Create the initial admin user
            admin_user = Admins(username="admin", password="admin", name="Administrator", job_title="Administrator", email="admin@prostar.pro", img=None)
            db.session.add(admin_user)
            db.session.commit()
            click.echo("Database tables created successfully.")
    else:
        click.echo("Database already exists.")
