import datetime

from mongoengine import Document, EmbeddedDocumentField, ListField
from mongoengine import StringField, DateTimeField

from backend.models.contact import Contact


class Ghummie(Document):
    name = StringField(max_length=100, required=True)
    address = StringField(max_length=120)
    contact_methods = ListField(EmbeddedDocumentField(Contact))
    created = DateTimeField(default=datetime.datetime.utcnow)