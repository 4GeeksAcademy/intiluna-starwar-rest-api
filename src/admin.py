import os
from flask_admin import Admin
<<<<<<< HEAD
from models import db, User, Character
=======
from models import db, User
>>>>>>> e5b61a8c0b58ec68a018fd4ffcfe213623495b61
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
<<<<<<< HEAD
    admin.add_view(ModelView(Character, db.session))
=======
>>>>>>> e5b61a8c0b58ec68a018fd4ffcfe213623495b61

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))