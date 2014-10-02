from flask import render_template, request

from messageboard import app
from messageboard.models.post import Post

#this is restfull route's
@app.route('/user/<name>', methods=["GET"])
def user_home(name):

    user_id="a9514e98427c8e708c00960e431f1afc"

    newpost=Post(
    author_id = user_id,
    content="Fish",
    date=datetime.utcnow()
    )

    newpost.save()


    posts = Post.view('Post/all')

    resp = ""

    for post in posts:
        if post.author == name:
            resp += "<li>" + post.content + "</li>"
            resp += "<li>" + post.author + "</li>"
    return render_template("index.html", posts=posts)

@app.route('/', methods=["GET"])
def index_setting():
    posts = Post.view('Post/all')
    return "list all post"
    post_list = "<ul>" + resp + "</ul>"

    return post_list

@app.route('/post/<post_id>/comments', methods=["GET", "POST"])
def show_comments_of_post(post_id):

    post = Post.get(post_id)

    _comments = ""

    for comment in post.comments:
        _comments += "<li>" + \
                        "<div id='comment_box'>" + \
                            "<a id='comment_author' href='/user/"+comment["user"]+"'>" + \
                                comment["user"] + \
                            "</a>" + \
                            "<p id='comment_text'>" + \
                                comment["comment_text"] + \
                            "</p>" + \
                        "</div>" + \
                    "</li>"

    comment_list = "<ul id='comment_list'>" + _comments + "</ul>"

    return comment_list + render_template("comments.html")

def count_comments(post_id):
    post = Post.get(post_id)

    return len(post.comments)

def show_all_posts():
    posts = Post.view("Post/all")

    resp = ""

    for post in posts:
        resp += "<li>" + \
                    "<div id='post_box'>" + \
                        "<a href='http://"+post._id+"' id='anchor_post_content'>" + \
                            post.content + \
                        "</a>" + \
                        "<p id='para_post_author'> Submitted by: " +\
                            "<a href='/user/"+post.author+"' id='anchor_post_author'>" + \
                                post.author + \
                            "</a>" + \
                        "</p>" + \
                        "<a href='/post/"+post._id+"/comments' id='anchor_post_comments'>" + \
                            str(count_comments(post._id)) + " comments" + \
                        "</a>" + \
                    "</div>" + \
                "</li>"

    post_list = "<ul id='post_list'>" + resp + "</ul>"

    return post_list