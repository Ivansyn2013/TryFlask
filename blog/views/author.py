from flask import Blueprint, render_template
from blog.models import Author

author_app= Blueprint("author_app", __name__)

@author_app.route("/", endpoint='list')
def author_list():
    authors = Author.query.all()
    return render_template("author/author.html", authors=authors)