from flask import render_template
from . import public
from flask_login import login_required

@public.route('/user_account')
@login_required #only authenticated user access these route
def account():
    return render_template('public/Account.html')