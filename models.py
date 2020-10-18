import datetime
from mongoengine import *

class Character(Document):
    character_name = StringField(required=True, max_length=200)
    character_level = IntField()
    date_of_release = DateTimeField(default=datetime.datetime.now)
    trait = StringField()
    description = StringField()

    def to_json(self):
        return {
            "id" : self.id,
            "character_name" : self.character_name,
            "character_level": self.character_level,
            "trait": self.trait,
            "description": self.description
        }