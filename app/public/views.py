from flask.helpers import flash
from flask.templating import render_template_string
from .import public
from flask import render_template, url_for, redirect
from flask_login import login_required, current_user
from .forms import UpdateForm
from ..models import Update
from ..import db

@public.route('/updates')
def updates():
    # grab All updated data from posts
    updates=Update.query.all() # fetch all from Update table
    return render_template('public/updates.html', updates=updates)

@public.route('/create_update', methods=['POST', 'GET'])
@login_required
def create_update():
    form=UpdateForm()
    if form.validate_on_submit():

        #update post in database
        post=Update(title=form.title.data, content=form.content.data, author=current_user) # backref=author
        db.session.add(post)
        db.session.commit()

        flash('Update has been updated successfully', 'info')
        return redirect(url_for('main.home'))

    return render_template('public/create_update.html', form=form)    

   
