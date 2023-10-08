from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager

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

login = LoginManager()
admin = Admin(index_view=MyAdminIndexView())
db = SQLAlchemy()

@login.user_loader
def load_user(user_id):
    return Admins.query.get(user_id)