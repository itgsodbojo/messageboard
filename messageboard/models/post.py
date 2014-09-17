from couchdbkit import Document, StringProperty, DateTimeProperty,ListProperty
from messageboard.models.user import User

class Post(Document):
    author_id = StringProperty()
    content = StringProperty()
    date = DateTimeProperty()
    comments = ListProperty()

    # def __int__(self,msg):
    #     super(Post, self).init()

    @property
    def author(self):
        #return self.author_id
        #TODO: Check whats happends user is non existing
        return User.get(self.author_id).name