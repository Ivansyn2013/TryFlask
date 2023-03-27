from marshmallow_jsonapi import Schema, fields
from combojsonapi.utils import Relationship

class ArticleSchema (Schema):
    class Meta():
        type_ = "article"
        self_view = "article_detail"
        self_view_kwargs = {'id':'<id>'}
        self_view_many = "article_list"

    id = fields.String(as_string=True)
    title = fields.String(allow_none=False)
    body = fields.String(allow_none=False)
    dt_created = fields.DateTime(allow_none=False)
    dt_updated =fields.DateTime(allow_none=False)

    #relations
    author = Relationship(
        nested="AuthorSchema",
        attribute="author",
        related_url="author_detail",
        related_url_kwargs={"id":"<id>"},
        schema="AuthorSchema",
        type_="author",
        many=False,
    )

    tags = Relationship(
        nested="TagSchema",
        attribute="tags",
        related_url="tag_detail",
        related_url_kwargs={"id": "<id>"},
        schema="TagSchema",
        type_="tag",
        many=True,
    )