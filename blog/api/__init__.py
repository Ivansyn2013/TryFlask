from flask_combo_jsonapi import Api
from blog.api.tag import TagList, TagDetails
from blog.api.user import UserList, UserDetails
from blog.api.author import AuthorList, AuthorDetails
from blog.api.article import ArticleDetails, ArticleList
from combojsonapi.spec import ApiSpecPlugin


def create_api_spec_plugin(app):
    api_spec_plugin = ApiSpecPlugin(
        app=app,
        tags={
            "Tag": "Tag ApI",
            "Article": "Article aPI",
            "User": "UserApi",
            "Author": "Author Api",
        }
    )
    return api_spec_plugin


def init_api(app):
    api_spec_plugin = create_api_spec_plugin(app)
    api = Api(app,
              plugins=[
                  api_spec_plugin,
              ],
              )
    api.route(TagList, 'tag_list', '/api/tags/', tag='Tag')
    api.route(TagDetails, 'tag_detail', '/api/tags/<id>/', tag='Tag')
    api.route(UserDetails, 'user_detail', '/api/user/<id>', tag='User')
    api.route(ArticleDetails, 'article_detail', '/api/article/<id>',
              tag='Article')
    api.route(AuthorDetails, 'author_detail', '/api/author/<id>', tag='Author')
    api.route(UserList, 'user_list', '/api/users', tag='User')
    api.route(ArticleList, 'article_list', '/api/article', tag='Article')
    api.route(AuthorList, 'author_list', '/api/author', tag='Author')
    return api
