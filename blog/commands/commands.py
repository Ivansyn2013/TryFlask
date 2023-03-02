from blog.models.init_db import db
from blog.models.user import User
from flask import Blueprint

my_cli_commands_app = Blueprint('my_commands', __name__)
@my_cli_commands_app.cli.command("init-db")
def init_db():
    '''
    command for init flask db
    '''
    db.create_all()
    print('Db is inited')

@my_cli_commands_app.cli.command("create-user")
def create_user():
    '''
    Cli command for create Flask user in db
    > Created user: user
    '''
    admin = User(user_name='admin', is_staff=True)
    db.session.add(admin)
    db.session.commit()
    print('Success user created: ', admin)