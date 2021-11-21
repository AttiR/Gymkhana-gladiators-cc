from os import abort
from flask.helpers import flash
from flask.templating import render_template_string
from .import public
from flask import render_template, url_for, redirect,request
from flask_login import login_required, current_user
from .forms import UpdateForm
from ..models import Update
from ..import db


#Post/Updates views
@public.route('/updates')
def updates():
    # grab All updated data from posts
    # fetch all from Update table
    #updates=Update.query.all()
    # Flask Pagination
    page=request.args.get('page', 1, type=int) # how to get current page (default is 1)
    #updates=Update.query.paginate(page=page, per_page=4)
    # make a query like the latest post is on the top
    updates=Update.query.order_by(Update.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('updates/updates.html', updates=updates)


# Make New Post
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

    return render_template('updates/create_update.html', legend='Make Post', form=form) 

# creating a route to go om specific update dertails
@public.route('/detail_updates/<int:update_id>')#expecting id int
def detail_updates(update_id):
    update=Update.query.get_or_404(update_id) # if update with id does not exists give 404
    return render_template('updates/details_updates.html', update=update)


# Editing the update  
@public.route('/detail_updates/<int:update_id>/edit', methods=['POST', 'GET'])#expecting id int
@login_required
def edit(update_id):
    update=Update.query.get_or_404(update_id) # if update with id does not exists give 404
    if update.author!= current_user: # as author is admin so only admin will access
        abort(403)
    form=UpdateForm() # we will use the same form as for the create update
    if form.validate_on_submit():
        # make logic to update the data in database
        update.title=form.title.data
        update.content=form.content.data
        db.session.commit()
        flash('Post has been updated', 'success')
        return redirect(url_for('public.detail_updates', update_id=update_id))
    elif request.method == 'GET': # to populate the form already
        form.title.data= update.title
        form.content.data=update.content    
    # render the same form as did for creating the post
    return render_template('updates/create_update.html', title='Edit Post', legend='Edit Post', form=form) 

# Delete The Post/update
@public.route('/detail_updates/<int:update_id>/delete', methods=['POST', 'GET'])#expecting id int
@login_required
def delete(update_id):
    update=Update.query.get_or_404(update_id) # if update with id does not exists give 404
    if update.author!= current_user: # as author is admin so only admin will access
        abort(403)
    db.session.delete(update)
    db.session.commit()
    flash('Post has been delted', 'success')
    return redirect(url_for('public.updates', update_id=update.id))
   
   