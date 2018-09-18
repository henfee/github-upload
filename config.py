class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    # SQLAlCHEMY_DATABASE_URI = "sqlite:///database.db"
    #Unix/Mac - 4 initial slashes in total
    # engine = create_engine('sqlite:////absolute/path/to/foo.db')
    SQLALCHEMY_DATABASE_URI = "sqlite:///flask.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
