from .import public
from flask import render_template, url_for, redirect
@public.route('/updates')
def updates():
    return render_template('public/updates.html')
