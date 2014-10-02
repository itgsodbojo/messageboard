from flask import render_template, request

from messageboard import app

from flask_login import current_user

from messageboard.models import User



@app.route('/settings', methods=["GET"])
def user_settings():
    if current_user.is_authenticated():
        return "Hello " + current_user.name + " this is your settings"
