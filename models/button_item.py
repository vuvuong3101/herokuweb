from mongoengine import *

class ButtonItem(Document):
    music = ListField(IntField())
    movie = ListField(IntField())
    book = ListField(IntField())
    clip = ListField(IntField())

    def to_dict(self):
        return {
            "music": list(self.music),
            "movie": list(self.movie),
            "book": list(self.book),
            "clip": list(self.clip)
        }