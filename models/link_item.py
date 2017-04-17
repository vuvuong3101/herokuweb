from mongoengine import *

class LinkItem(Document):
    item = ListField(StringField())