from marshmallow_jsonapi import Schema, fields
from combojsonapi.utils import Relationship

class UserSchema (Schema):
    class Meta():
        type_ = "user"
        self_view = "user_detail"
        self_view_kwargs = {'id':'<id>'}
        self_view_many = "user_list"

    id = fields.String(as_string=True)
    first_name = fields.String(allow_none=False)
    last_name = fields.String(allow_none=False)
    email = fields.String(allow_none=False)
    is_staff = fields.Boolean(allow_none=False)

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

