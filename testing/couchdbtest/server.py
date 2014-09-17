from couchdbkit import Server,push


# server object
server = Server()



# create databases
db = server.get_or_create_db("post")
userdb = server.get_or_create_db("user")


from models import Post, User

# associate Models to the db
Post.set_db(db)
User.set_db(userdb)


#this is views we need on the server for searching and retrieving doc's
#push the to server
push('designdocs/Post', db)