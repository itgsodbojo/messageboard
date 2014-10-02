from flask import Flask
from couchdbkit import Server,push
from flask_login import LoginManager

#init the flask app
app = Flask(__name__)

app.secret_key = "troleolol"

login_manager = LoginManager()
login_manager.init_app(app)





# server object
server = Server()


# create databases
db = server.get_or_create_db("post")
userdb = server.get_or_create_db("user")
emaildb = server.get_or_create_db("email")


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
from views import login, post, user, signup, home