from app import app

from flask import render_template, request, redirect, url_for
from app.forms import FeedbackForm
from app.models import Feedback
from app import db



@app.route("/")
def home():
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    return render_template("public/home.html")

@app.route("/about")
def about():
    return render_template("public/about.html")  

@app.route("/contact", methods=['POST', 'GET'])
def contact():
    form = FeedbackForm()
    if request.method == 'POST':
        req= request.form
        first_name= req['first_name']
        last_name= req['last_name']
        email=req['email']
        feedback=req['feedback']

        # databse entry
        data = Feedback(first_name, last_name, email, feedback)
        db.session.add(data)
        db.session.commit()
     

    return render_template("public/contact.html", form=form)    

@app.route("/signup")
def signup():
    return render_template("public/signup.html")  

@app.route("/login")
def login():
    return render_template("public/login.html")             

@app.route("/gallary")
def gallary():
    return render_template("public/gallary.html")  

@app.route("/club-members")
def members():
    return render_template("public/members.html")     

@app.route("/acheivements")
def acheievments():
    return render_template("public/acheivements.html") 
@app.route("/policy")
def policy():
    return render_template("public/policy.html")          