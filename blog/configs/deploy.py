class Config(object):
    TESTING = False

class DevelopmemtConfig(Config):
    TESTING = True
    DATABASE_URI = ''