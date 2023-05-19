from marshmallow_jsonapi import Schema, fields
from combojsonapi.utils import Relationship

class AuthorSchema (Schema):
    class Meta():
        type_ = "author"
        self_view = "author_detail"
        self_view_kwargs = {'id':'<id>'}
        self_view_many = "author_list"

    id = fields.String(as_string=True)

    #relations
    user = Relationship(
        nested="UserSchema",
        attribute="user",
        related_url="user_detail",
        related_url_kwargs={"id":"<id>"},
        schema="UserSchema",
        type_="user",
        many=False,
    )

    article = Relationship(
        nested="ArticleSchema",
        attribute="article",
        related_url="article_detail",
        related_url_kwargs={"id": "<id>"},
        schema="ArticleSchema",
        type_="article",
        many=True,
    )