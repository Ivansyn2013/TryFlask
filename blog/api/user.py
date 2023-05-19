from flask_combo_jsonapi import ResourceList, ResourceDetail
from blog.models.init_db import db
from blog.models.user import User
from blog.schemas import UserSchema

class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
    }

class UserDetails(ResourceDetail):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
    }
