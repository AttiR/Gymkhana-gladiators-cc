from . import admin
from flask import render_template,url_for,flash, redirect
from flask_login import  login_required

from flask import current_app



@admin.route("/6789876dashboard")

def dashboard():

    return render_template("admin/dashboard.html")





    