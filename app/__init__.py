
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager

from config import config
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap









#app = Flask(__name__)
#app.config.from_object(Config)




db=SQLAlchemy()
mail = Mail()
bcrypt=Bcrypt()
bootstrap=Bootstrap()
admin=Admin()



login_manager=LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category='info' # fro flash messages




def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
  

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .public import public as public_blueprint
    from .models import User, Update,UploadImg, Feedback, UploadVideo,  UserView, UpdateView, UploadView, FeedbackView, VideoView
    from .commands import create_tables

    
    config[config_name].init_app(app)
    db.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    admin.init_app(app)
    bootstrap.init_app(app)

    if app.config['SSL_REDIRECT']: 
        from flask_sslify import SSLify
        sslify = SSLify(app)


    # Flask Admin section Model views
    admin.add_view(UserView(User, db.session))
    admin.add_view(UpdateView(Update, db.session))
    admin.add_view(UploadView(UploadImg, db.session))
    admin.add_view(FeedbackView(Feedback, db.session))
    admin.add_view(VideoView(UploadVideo, db.session))
  
   
    
    login_manager.init_app(app)

  

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(public_blueprint)
    app.cli.add_command(create_tables)

    return app