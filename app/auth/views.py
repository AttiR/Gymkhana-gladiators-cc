from .import auth

from flask import render_template, request, redirect, url_for, flash, abort
from .forms import RegistrationForm, LoginForm, PasswordresetForm, UpdateAccountForm
from ..models import  User
from ..import db, bcrypt
#from app import mail
#from flask_mail import Message
from ..emails import send_email
from .utilits import generate_confirmation_token, confirm_token
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required


import datetime

# Registration route
@auth.route("/signup", methods=['POST', 'GET'])
def signup():
    if current_user.is_authenticated: # if user is already login and registed try to sign up
        return redirect(url_for('main.home'))
    form=RegistrationForm()
    if form.validate_on_submit():

        name=form.name.data
        username=form.username.data
        email=form.email.data
        phonenumber=form.phonenumber.data
        password=form.password.data
        password_hash=bcrypt.generate_password_hash(password).decode('utf-8')
      

        user = User(name, username, email, phonenumber, password_hash, confirmed=False)
        #admin=User(name, username, email,phonenumber, password_hash, confirmed=True, admin=True, confirmed_on=datetime.datetime.now() )
        db.session.add(user)
        db.session.commit()
        # import from token .py
        token = generate_confirmation_token(user.email)
        confirm_url = url_for('auth.confirm_email', token=token, _external=True)
        html = render_template('mails/confirm.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(user.email, subject, html)

        flash('A confirmation email has been sent via email.', 'success')
        return redirect(url_for("main.home"))

    return render_template("auth/signup.html", form=form) 

# Token Genertaion for 
@auth.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed: # check if user confirmed is already True confirmed=True
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.confirmed = True
        user.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('auth.login'))


#Login Route
@auth.route("/login", methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated: # if user is already login and try to log in again
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        email=form.email.data
        password=form.password.data
        

    
        # make query for User databse
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=form.remember.data) # is user check remember it will return True else False
            # now lets say user want to access specipic page like user_account, he will be redirected to login page
            #We want that he should be redirected to desired page not home page for that we will check nxt_page
            next_page=request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home')) #python ternary operator
           

        else:
            flash('Unsuccessfull Login, please cehck email and password', 'danger')

    return render_template("auth/login.html", form=form)   

# Logout User
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))



# Password Reset Route
@auth.route("/passwordreset", methods=['POST', 'GET'])
def passwodreset():
    form= PasswordresetForm()
    if form.validate_on_submit():
        pass
    return render_template("auth/password_reset.htm", form=form)    


# Account/Profile
@auth.route("/account", methods=["POST", "GET"])
@login_required #only authenticated user access these route
def account():
   
    
    image_file= url_for('static', filename='img/profileimg/' +current_user.image_file)
    return render_template('auth/account.html', file= image_file)  


# Profile Update
@auth.route("/update", methods=["POST", "GET"])
@login_required #only authenticated user access these route
def update():
    form=UpdateAccountForm()
    if form.validate_on_submit():
      
        current_user.email=form.email.data
        current_user.phonenumber=form.phonenumber.data
        db.session.commit()
        flash('Your Account has been updated!', 'success')
        return redirect(url_for('auth.account'))

    elif request.method == 'GET':
       
        form.email.data = current_user.email    
        form.phonenumber.data=current_user.phonenumber
    
   
    return render_template('auth/updateprofile.html',  form=form)  
