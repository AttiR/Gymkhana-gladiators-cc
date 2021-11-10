from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail, Message



app = Flask(__name__)



if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')

elif  app.config['ENV'] == 'testing':
    app.config.from_object('config.TestingConfig')  
else:
    app.config.from_object('config.DevelopmentConfig')
db=SQLAlchemy(app)
mail = Mail()

from app import views 
from app import admin_views
from app import forms
from app import models
from app import emails