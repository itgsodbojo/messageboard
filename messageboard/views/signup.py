from flask import render_template, request
from flask_login import current_user, login_user

from messageboard import app
from messageboard.models.user import User
from messageboard.models.email import Email
from messageboard.views.home import home

from couchdbkit.exceptions import ResourceNotFound

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated():
        return home()
    if request.method == "POST":

        email_signup = request.form.get("email_signup")
        username = request.form.get("username_signup").lower()
        password = request.form.get("password_signup")

        try:

            user_exist = User.get(username)
            #email_exist = Email.get(email_signup)

            return "Sorry, a user with that name or email already exist."
        except ResourceNotFound:

            #create user
            new_user = User(email=email_signup, name=username, password=password)
            new_user._id = username
            new_user.save()

            login_user(User.get(username.lower()))

            return home()

            #new_email = Email(email=email_signup)
            #new_email._id = email_signup
            #new_email.save()
        except Exception as e:

            return e

    return render_template("signup.html")