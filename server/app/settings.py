def getURI(dbinfo):
    user = dbinfo.get("USER") or "root"
    password = dbinfo.get("PASSWORD")
    host = dbinfo.get("HOST")
    port = dbinfo.get("PORT")
    name = dbinfo.get("NAME")
    return "mysql+pymysql://{}:{}@{}:{}/{}".format(user, password, host, port, name)


class Config():
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "tpp"
    }
    SQLALCHEMY_DATABASE_URI = getURI(DATABASE)


class TestingConfig(Config):
    TESTING = True
    DATABASE = {
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "tpp"
    }
    SQLALCHEMY_DATABASE_URI = getURI(DATABASE)


class StageConfig(Config):
    DATABASE = {
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "tpp"
    }
    SQLALCHEMY_DATABASE_URI = getURI(DATABASE)


class ProductConfig(Config):
    DATABASE = {
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "tpp"
    }
    SQLALCHEMY_DATABASE_URI = getURI(DATABASE)


envs = {
    "develop": DevelopConfig,
    "default": DevelopConfig,
    'testing': TestingConfig,
    'stage': StageConfig,
    'product': ProductConfig,
}
