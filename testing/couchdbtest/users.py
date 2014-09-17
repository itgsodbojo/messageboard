import server

from models import User


#create user and saves it to hte database
new_user=User(name="kalle")

new_user.save()



print new_user.name, new_user.id


# delete user with

#del server.userdb[new_user.id]


#update a user
#get it
get_user = User.get(new_user.id)
#change the name
get_user.name="kallestrop"
#and save it
get_user.save()


print get_user.name, get_user.id