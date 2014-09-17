from couchdbkit import Document, StringProperty, DateTimeProperty,ListProperty

class User(Document):
    name = StringProperty()

    @property
    def id(self):
        if self.new_document:
            return None
        return self._doc['_id']



