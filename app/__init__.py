
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


db=SQLAlchemy(app)
mail = Mail(app)




from app.main.routes import main
from app.admin.routes import admin
from app.auth.routes import auth
from app import errors_handlers


app.register_blueprint(main)
app.register_blueprint(admin)
app.register_blueprint(auth)
