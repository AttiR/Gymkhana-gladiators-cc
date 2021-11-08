from flask import Flask

app = Flask(__name__)

#import (like views.py) files to package
from app import views 
from app import admin_views