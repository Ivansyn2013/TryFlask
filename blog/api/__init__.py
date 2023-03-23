from flask_combo_jsonapi import Api
from blog.api.tag import TagList, TagDetails

def init_api(app):
    api=Api(app)
    api.route(TagList, 'tag_list', '/api/tags/')
    api.route(TagDetails, 'tag_detail', '/api/tags/<id>/')

    return api
