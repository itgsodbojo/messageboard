from flask import render_template, request

from messageboard import app

from messageboard.models.post import Post


@app.route('/user/<name>/settings', methods=["GET"])
def user_setting(name):
    return "Hello " + name + " your settings"