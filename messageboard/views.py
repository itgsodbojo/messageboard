from flask import render_template, request

from webbapp import app



#satndard get
@app.route('/', methods=["GET"])
def hello_world():
    return render_template("index.html",name = "bosse", title="Hello from flask")


# get parameters
@app.route('/hejsan', methods=["GET"])
def hejsan():

    name=request.args.get("name","dude")

    return "hejsan " + name

#this is restfull route's
@app.route('/user/<name>', methods=["GET"])
def user_home(name):

    return "Hello " + name

@app.route('/user/<name>/settings', methods=["GET"])
def user_setting(name):

    return "Hello " + name + " your settings"

#post
@app.route('/user', methods=["GET","POST"])
def user5():

    #return str(request.form.keys)
    name=request.form['name']



    return "Hello " + name


@app.route('/pnr', methods=["GET"])
def checkpnr():

    return render_template("checkpnr.html", title="personummerkoll")