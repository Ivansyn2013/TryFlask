from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from blog.models.init_db import db
from blog import models

class CustomAdminViews(ModelView):
    pass


admin = Admin(name='Blog Admin', template_mode='bootstrap4')
admin.add_view(CustomAdminViews(models.Tag, db.session, category='Models'))
