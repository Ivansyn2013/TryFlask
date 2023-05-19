import os

from dotenv import load_dotenv

class Config(object):
    TESTING = False


class DevelopmemtConfig(Config):
    TESTING = True
    # DATABASE_URI = ''
    SQLALCHEMY_DATABASE_URI = 'sqlite:////db.db'
    SQLALCHEMY_MODIFICATIONS = False
    SECRET_KEY = 'abcdefg123456'

class DeployConfig(Config):
    load_dotenv()
    config = os.environ
    SQLALCHEMY_DATABASE_URI = config['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_MODIFICATIONS = config['SQLALCHEMY_MODIFICATIONS']
    SECRET_KEY = config['SECRET_KEY']
    POSTGRES_DB = config['POSTGRES_DB']
    POSTGRES_USER = config['POSTGRES_USER']
    POSTGRES_PASSWORD = config['POSTGRES_PASSWORD']
    PGDATA = config['PGDATA']
