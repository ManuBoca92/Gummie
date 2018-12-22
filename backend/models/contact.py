from mongoengine import EmbeddedDocument, URLField, EmailField
from mongoengine import IntField


class Contact(EmbeddedDocument):
    number = IntField(max_length=100, required=True)
    facebook = URLField(required=True)
    instagram = URLField(required=True)
    whatsapp = URLField(required=True)
    email = EmailField(required=True)