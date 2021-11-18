from flask.helpers import flash
from flask.templating import render_template_string
from .import public
from flask import render_template, url_for, redirect,request
from flask_login import login_required, current_user
from .forms import UpdateForm
from ..models import Update
from ..import db

@public.route('/updates')
def updates():
    # grab All updated data from posts
    # fetch all from Update table
    #updates=Update.query.all()
    #Flask Pagination
    page=request.args.get('page', 1, type=int) # how to get current page (default is 1)
    updates=Update.query.paginate(page=page, per_page=4)
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

   
