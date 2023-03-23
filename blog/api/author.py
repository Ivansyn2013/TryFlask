from flask_combo_jsonapi import ResourceList, ResourceDetail
from blog.models.init_db import db
from blog.models.author import Author
from blog.schemas import AuthorSchema

class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }

class AuthorDetails(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }
