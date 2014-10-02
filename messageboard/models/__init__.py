from messageboard import db, userdb, emaildb

from post import Post
from user import User
from email import Email
#
# # associate Models to the db
Post.set_db(db)
User.set_db(userdb)
Email.set_db(emaildb)