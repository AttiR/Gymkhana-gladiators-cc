from . import admin
from flask import render_template,url_for,flash, redirect
from flask_login import  login_required
from .forms import LoginForm
from flask import current_app



@admin.route("/6789876dashboard")

def dashboard():

    return render_template("admin/dashboard.html")

@admin.route("/admin", methods=['POST', 'GET'])
def adminlogin():
    form=LoginForm()  
   
    if form.validate_on_submit():
        if form.email.data == 'atti.rehmman@gmail.com' and form.password.data == current_app.config['ADMIN_PASSWORD']:
           
            return redirect(url_for('admin.dashboard'))
        else:
             return redirect(url_for('home'))
            
    return render_template('admin/admin.html', form=form)
   



    