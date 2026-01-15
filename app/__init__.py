from flask import Flask
from app.extentions import db, admin, login
from app.routes.web.router import web
from app.routes.admin.admin_route import web_admin
from app.login_manager import load_user
from werkzeug.security import generate_password_hash
import os
from app.models import *
import click

app = Flask(__name__)
app.register_blueprint(web)
app.register_blueprint(web_admin, url_prefix="/admin")

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "")
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "")

db.init_app(app)
admin.init_app(app)
login.init_app(app)
login.login_view = "admin_panel.log_in" # type: ignore

@app.cli.command("init-db")
def init_db():
    """Initialize the database."""
    db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace('postgresql://', '')
    if not os.path.exists(db_path):
        with app.app_context():
            db.create_all()
            # Create the initial admin user
            if Admins.query.first() is None:
                admin_user = Admins()
                admin_user.username = os.environ.get("PROSTAR_ADMIN_USERNAME", "")
                admin_user.password = generate_password_hash(os.environ.get("PROSTAR_ADMIN_PASSWORD", ""), method='scrypt', salt_length=16)
                admin_user.name = "Administrator"
                admin_user.job_title = "Administrator"
                admin_user.email = "admin@prostar.pro"
                admin_user.img = None
                db.session.add(admin_user)
                db.session.commit()
            click.echo("Database tables created successfully.")
    else:
        click.echo("Database already exists.")
