import os

class Config:
    
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://carol:lorac1234@localhost/blog"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    uri = os.getenv('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI = uri

class TestConfig(Config):
     SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://carol:lorac1234@localhost/blog"
    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://carol:lorac1234@localhost/blog"
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production': ProdConfig,
    'test':TestConfig
   
}