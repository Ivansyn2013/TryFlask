from flask_combo_jsonapi import ResourceList, ResourceDetail
from blog.models.init_db import db
from blog.models.article import Article
from blog.schemas import TagSchema

class ArticleList(ResourceList):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }

class TagDetails(ResourceDetail):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }
