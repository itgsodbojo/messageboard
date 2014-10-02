from couchdbkit import Document, StringProperty, DateTimeProperty,ListProperty

class Email(Document):
    email = StringProperty()
