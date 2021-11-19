import os
from dotenv import load_dotenv


# load dotenv in the base root
# APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
# dotenv_path = os.path.join(APP_ROOT, '.env')
# load_dotenv(dotenv_path)

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    DEBUG=False
    TESTING=False
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SECURITY_PASSWORD_SALT=os.environ.get('SECURITY_PASSWORD_SALT')    
   
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    #Email Setup
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS= True
    MAIL_USERNAME= os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD= os.environ.get('EMAIL_PASS')
    ADMIN_PASSWORD=os.environ.get('ADMIN_PASS')
    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
   
    DEBUG=True
     

class DevelopmentConfig(Config):
    DEBUG=True
    
       
class TestingConfig(Config):
    TESTING=True





config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
    
}    