from .extentions import login
from .models import Admins

@login.user_loader
def load_user(user_id):
    return Admins.query.get(user_id)