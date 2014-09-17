from messageboard import db, userdb

from post import Post
from user import User
#
# # associate Models to the db
Post.set_db(db)
User.set_db(userdb)