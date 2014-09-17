from flask import render_template, request
from webbapp import app



@app.route('/', methods=["GET"])
def hello_world():


    return render_template("index.html",name = "bosse", title="Hello from flask")