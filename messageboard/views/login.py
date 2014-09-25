from flask import render_template, request
from flask_login import login_user, login_required, logout_user, current_user
from messageboard.models.user import User
from messageboard.views.home import home

from messageboard import app
from messageboard import login_manager

@login_manager.user_loader
def load_user(userid):
    return User.get(userid)

@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated():
        return home()
    if request.method == "POST":

        if len(request.form.get("username")) == 0 or len(request.form.get("password")) == 0:
            return render_template("login.html", error="Username or password can not be blank")

        try:
            get_user = User.get(request.form.get("username").lower())
        except:
            return render_template("login.html", error="Incorrect username")

        try:
            user_pass = get_user.password

            if request.form.get("password") == user_pass:
                login_user(get_user)
            else:
                return render_template("login.html", error="Incorrect password")

        except Exception as e:
            return e

        return home()

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return home()

@login_manager.unauthorized_handler
def unauthorized():
    return "Error, user is unauthorized."
