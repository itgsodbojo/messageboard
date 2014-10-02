from messageboard import app
from flask import render_template
from flask_login import current_user
from messageboard.views.post import show_all_posts

@app.route('/', methods=["GET"])
def home():
    if current_user.is_authenticated():
        return show_all_posts() + render_template("index.html", name="ReddITG", title="ReddITG", user=current_user.name)
    return show_all_posts() + render_template("index.html",name="ReddITG", title="ReddITG")