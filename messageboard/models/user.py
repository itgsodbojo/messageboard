from couchdbkit import Document, StringProperty, DateTimeProperty,ListProperty

class User(Document):
    email = StringProperty()
    name = StringProperty()
    password = StringProperty()

    @property
    def id(self):
        if self.new_document:
            return None
        return self._doc['_id']

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.name)

    def __repr__(self):
        return '<User %r>' % (self.name)



