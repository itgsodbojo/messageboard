from flask import render_template, request

from messageboard import app
from messageboard.models.post import Post

#this is restfull route's
@app.route('/user/<name>', methods=["GET"])
def user_home(name):

    posts = Post.view('Post/all')

    resp = ""

    for post in posts:
        resp += post.content + "<br>"
        resp += post.author + "<br>"

    return resp