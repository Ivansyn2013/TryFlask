from flask import Flask
from flask import request
from flask import g

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/user/')
def read_user():  # put application's code here
    name = request.args.get('name')
    surname = request.args.get('surname')
    return f"Username {name or ['noname']} Usersurname {surname or ['nosurname']}"
