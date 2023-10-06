from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

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

admin = Admin(app, index_view=MyAdminIndexView())
db = SQLAlchemy()