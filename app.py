import random
from flask import Flask,request,redirect,render_template,session
from pymongo import Connection

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
def home():
    return render_template("main.html");

@app.route("/login", methods=["GET","POST"])
def login():
    return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
    return render_template("register.html")

@app.route("/page1", methods=["GET","POST"])
def page1():
    ##universal dict. combine get and post
    ud = dict(request.form.items() + request.args.items())
    
    if "username" not in ud or method == "GET":
        return render_template("page1.html", loggedin=False,username="")
    else:
        return render_template("page1.html",
                               loggedin=True,
                               username=ud["username"])

@app.route("/page2", methods=["GET","POST"])
def page2():
    return render_template("page2.html");

     
if __name__=="__main__":
    app.debug=True
    app.run();
