import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from dotenv import load_dotenv
load_dotenv()




app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

#DataBase setup
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DEV_DATABASE_URL')
db=SQLAlchemy(app)

#Email Setup
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'attirehman388@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from app import views 
from app import admin_views

