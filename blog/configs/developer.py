class Config(object):
    TESTING = False

class DevelopmemtConfig(Config):
    TESTING = True
    #DATABASE_URI = ''
    SQLALCHEMY_DATABASE_URI = 'sqlite:////db.db'
    SQLALCHEMY_MODIFICATIONS = False