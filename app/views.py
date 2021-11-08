from app import app

from flask import render_template

@app.route("/")
def home():
    return render_template("public/home.html")

@app.route("/about")
def about():
    return render_template("public/about.html")  

@app.route("/contact")
def contact():
    return render_template("public/contact.html")    

@app.route("/signup")
def signup():
    return render_template("public/signup.html")  

@app.route("/login")
def login():
    return render_template("public/login.html")             