from flask_combo_jsonapi import ResourceList, ResourceDetail
from blog.models.init_db import db
from blog.models.author import Author
from blog.schemas import AuthorSchema
from combojsonapi.event import EventPlugin
from blog.models.article import Article


class AuthorDetailEvents(EventPlugin):
    def event_get_author_articles_count(self, **kwargs):
        return {'count':
                    Author.query.filter(
                        Article.author_id == kwargs['id']).count()}


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }


class AuthorDetails(ResourceDetail):
    events = AuthorDetailEvents
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }
