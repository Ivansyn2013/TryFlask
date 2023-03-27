from flask_combo_jsonapi import ResourceList, ResourceDetail
from blog.models.init_db import db
from blog.models.article import Article
from blog.schemas import ArticleSchema
from combojsonapi.event.resource import EventsResource

class ArticleListEvents(EventsResource):
    def event_get_count(self):
        return {'count': Article.query.count()}
class ArticleList(ResourceList):
    events = ArticleListEvents
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }

class ArticleDetails(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }
