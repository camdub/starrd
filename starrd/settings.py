class Config(object):
    GITHUB_CLIENT_ID = '410cc6a3e09f1773710f'
    GITHUB_CLIENT_SECRET = '157b8e015deb97d02e4f37344f5fbcd93cc32589'
    GITHUB_CALLBACK_URL = 'http://localhost:5000/auth'
    SECRET_KEY = 'woodmansee'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///starrd.db'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///starrd.db'
    DEBUG = True
    ASSETS_DEBUG = True
