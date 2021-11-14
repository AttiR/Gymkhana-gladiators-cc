
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




from .main import main as main_blueprint
from .admin import admin as admin_blueprint
from .auth import auth as auth_blueprint



app.register_blueprint(main_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(auth_blueprint)

