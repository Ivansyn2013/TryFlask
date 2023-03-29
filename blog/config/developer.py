import os

from dotenv import load_dotenv, dotenv_values

class Config(object):
    TESTING = False
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = 'cosmo'
    #настройки swagger
    OPENAPI_URL_PREFIX = '/api/swagger'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_VERSION = '3.22.0'


class DevelopmemtConfig(Config):
    TESTING = True
    # DATABASE_URI = ''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.db'
    SQLALCHEMY_MODIFICATIONS = False
    SECRET_KEY = 'abcdefg123456'

class DeployConfig(Config):
    load_dotenv()
    config = dotenv_values('.env')
    FLASK_DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = config['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_MODIFICATIONS = config['SQLALCHEMY_MODIFICATIONS']
    SECRET_KEY = config['SECRET_KEY']

class DeveloperPostgresConfig(Config):
    load_dotenv()
    config = dotenv_values('.env')
    TESTING = True
    FLASK_DEBUG = True
    SQLALCHEMY_DATABASE_URI = config['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_MODIFICATIONS = config['SQLALCHEMY_MODIFICATIONS']
    SECRET_KEY = config['SECRET_KEY']

    POSTGRES_DB = config['POSTGRES_DB']
    POSTGRES_USER = config['POSTGRES_USER']
    POSTGRES_PASSWORD = config['POSTGRES_PASSWORD']
    PGDATA = config['PGDATA']