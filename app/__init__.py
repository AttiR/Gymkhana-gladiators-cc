
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager
from config import Config
from flask_admin import Admin




#app = Flask(__name__)
#app.config.from_object(Config)




db=SQLAlchemy()
mail = Mail()
bcrypt=Bcrypt()
admin=Admin()

login_manager=LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category='info' # fro flash messages




def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .public import public as public_blueprint

    db.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    
    
    login_manager.init_app(app)

  

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(public_blueprint)

    return app