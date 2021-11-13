from flask import render_template, request, redirect, url_for, flash, abort
from app.forms import FeedbackForm, RegistrationForm, LoginForm, PasswordresetForm
from app.models import Feedback, User
from app import db
#from app import mail
#from flask_mail import Message
from app.emails import send_email
from app.token import generate_confirmation_token, confirm_token
from werkzeug.security import generate_password_hash
from flask_login import login_user, logout_user, login_required
from app import app
import datetime

# Registration route
@app.route("/signup", methods=['POST', 'GET'])
def signup():
    form=RegistrationForm()
    if form.validate_on_submit():
        req=request.form
        name=req['name']
        username=req['username']
        email=req['email']
        password=req['password']
        password_hash=generate_password_hash(password)

        user = User(name, username, email, password_hash, confirmed=False)
        #admin=User(name, username, email, password_hash, confirmed=True, admin=True, confirmed_on=datetime.now() )
        db.session.add(user)
        db.session.commit()
        # import from token .py
        token = generate_confirmation_token(user.email)
        confirm_url = url_for('confirm_email', token=token, _external=True)
        html = render_template('mails/confirm.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(user.email, subject, html)

        

        flash('A confirmation email has been sent via email.', 'success')
        return redirect(url_for("home"))



       

    return render_template("auth/signup.html", form=form) 


@app.route('/confirm/<token>')

def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.confirmed = True
        user.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('login'))

