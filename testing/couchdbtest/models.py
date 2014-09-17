from couchdbkit import Document, StringProperty, DateTimeProperty,ListProperty

class User(Document):
    name = StringProperty()

    @property
    def id(self):
        if self.new_document:
            return None
        return self._doc['_id']



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



