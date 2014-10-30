import random
from flask import Flask,request,redirect,render_template,session
from pymongo import Connection
app=Flask(__name__)




@app.route("/", methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
def index():
    return render_template("main.html");

@app.route("/login", methods=["GET","POST"])
def forums():
    return render_template("login.html", topics = topics)

@app.route("/page1", methods=["GET","POST"])
def create():
    return render_template("page1.html")

@app.route("/page2", methods=["GET","POST"])
def table():
    return render_template("page2.html");

     
if __name__=="__main__":
    app.debug=True
    app.run();
