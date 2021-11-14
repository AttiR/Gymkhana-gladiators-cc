from . import admin
from flask import render_template

@admin.route("/admin/dashboard")
def dashboard():
    return render_template("admin/dashboard.html")

@admin.route("/admin/profile")
def profile():
    return render_template("admin/profile.html")  