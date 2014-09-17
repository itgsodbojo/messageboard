from flask import Flask
from couchdbkit import Server,push

#init the flask app
app = Flask(__name__)


# server object
server = Server()

# create database
db = server.get_or_create_db("greeting")
userdb = server.get_or_create_db("user")


# create databases
db = server.get_or_create_db("post")
userdb = server.get_or_create_db("user")


# from models.post import Post
# from models.user import User
#
# # associate Models to the db
# Post.set_db(db)
# User.set_db(userdb)


#this is views we need on the server for searching and retrieving doc's
#push the to server
push('messageboard/designdocs/Post', db)

import models
from views import utils, post, user