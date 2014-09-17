import datetime
import server
from models import Post




user_id="075c974e3f1069cabc31c00acd5271c2"




# create a new greet
new_post = Post(
    author_id=user_id,
    content="Nice messageboard",
    date=datetime.datetime.utcnow()

)


new_post.save()
#loop an print all post's

posts = Post.view('Post/all')



print "list all post"

for post in posts:
    print post.author, post.content

    try:
        print post.comments
    except:
        print "No comment"