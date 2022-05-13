import os

class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://oscar:1803@localhost/oneminpitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'


class ProdConfig(Config):
    
    
     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("://", "ql://", 1)
     DEBUG = True

class DevConfig(Config):
    
      pass
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}