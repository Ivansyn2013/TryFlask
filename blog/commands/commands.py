import os

from blog.models.init_db import db
from blog.models.user import User
from blog.models.author import Author
from flask import Blueprint
from dotenv import load_dotenv
load_dotenv()

my_cli_commands_app = Blueprint('my_commands', __name__)
@my_cli_commands_app.cli.command("init-db")
def init_db():
    '''
    command for init flask db
    '''
    #db.drop_all()
    db.create_all()
    print('Db is inited')

@my_cli_commands_app.cli.command("create-admin")
def create_user():
    '''
    Cli command for create Flask user in db
    > Created admin: user
    '''

    admin = User(first_name='admin1', is_staff=True, username='admin',
                 author=Author())
    admin.password = os.getenv('FLASK_ADMIN_PASSWORD') or '123'
    db.session.add(admin)
    db.session.commit()
    print('Success user created: ', admin)


@my_cli_commands_app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from blog.models import Tag
    for name in [
                    "flask",
                    "django",
                    "python",
                    "sqlalchemy",
                    "news",
                    ]:
        tag = Tag(name=name)
        db.session.add(tag)
        db.session.commit()
        print("created tags")