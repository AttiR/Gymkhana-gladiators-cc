from flask import render_template, url_for
from . import public
from flask_login import login_required, current_user

@public.route('/user_account')
@login_required #only authenticated user access these route
def account():
    image_file= url_for('static', filename='img/profileimg/' +current_user.image_file)
    return render_template('public/Account.html', file= image_file)