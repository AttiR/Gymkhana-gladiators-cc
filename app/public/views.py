from .import public
from flask import render_template
@public.route('/updates')
def updates():
    return render_template('public/updates.html')
