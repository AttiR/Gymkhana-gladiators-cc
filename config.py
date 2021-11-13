import os
from dotenv import load_dotenv
load_dotenv()

# load dotenv in the base root
# APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
# dotenv_path = os.path.join(APP_ROOT, '.env')
# load_dotenv(dotenv_path)

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    DEBUG=False
    TESTING=False
    SECRET_KEY= os.getenv('SECRET_KEY')
    SECURITY_PASSWORD_SALT=os.getenv('SECURITY_PASSWORD_SALT')    

    SQLALCHEMY_TRACK_MODIFICATIONS= False
    SQLALCHEMY_DATABASE_URI=os.getenv('DEV_DATABASE_URL')
    #Email Setup
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS= True
    MAIL_USERNAME= 'attirehman388@gmail.com'
    MAIL_PASSWORD= os.getenv('EMAIL_PASS')
    
  

   
    
    
    
   


class ProductionConfig(Config):
    pass
     

class DevelopmentConfig(Config):
    DEBUG=True
    
       
class TestingConfig(Config):
    TESTING=True