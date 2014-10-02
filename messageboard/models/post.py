from couchdbkit import Document, StringProperty, DateTimeProperty,ListProperty
from messageboard.models.user import User

class Post(Document):
    author_id = StringProperty()
    content = StringProperty()
    content_hidden = StringProperty()
    date = DateTimeProperty()
    comments = ListProperty()

    @property
    def author(self):
        #return self.author_id
        #TODO: Check whats happends user is non existing
        return User.get(self.author_id).name