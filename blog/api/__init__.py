from flask_combo_jsonapi import Api
from blog.api.tag import TagList, TagDetails
from combojsonapi.spec import ApiSpecPlugin
def create_api_spec_plugin(app):
    api_spec_plugin = ApiSpecPlugin(
        app=app,
        tags={
            "Tag": "Tag ApI",
        }
    )
    return api_spec_plugin
def init_api(app):
    api_spec_plugin = create_api_spec_plugin(app)
    api=Api(app,
            plugins=[
                api_spec_plugin,
            ],
            )
    api.route(TagList, 'tag_list', '/api/tags/', tag='Tag')
    api.route(TagDetails, 'tag_detail', '/api/tags/<id>/', tag='Tag')

    return api
