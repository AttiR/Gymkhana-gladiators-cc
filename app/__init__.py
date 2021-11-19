
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager
from config import Config
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_heroku import Heroku





#app = Flask(__name__)
#app.config.from_object(Config)




db=SQLAlchemy()
mail = Mail()
bcrypt=Bcrypt()
admin=Admin()
heroku=Heroku()

login_manager=LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category='info' # fro flash messages




def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)
  

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .public import public as public_blueprint
    from .models import User, Update, Controller
    from .commands import create_tables
    

    db.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    admin.init_app(app)
    admin.add_view(Controller(User, db.session))
    admin.add_view(Controller(Update, db.session))
    heroku.init_app(app)
    
    login_manager.init_app(app)

  

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(public_blueprint)
    app.cli.add_command(create_tables)

    return app