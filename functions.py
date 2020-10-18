from models import Character
from pymongo import MongoClient
import datetime 

from mongoengine import *
connect('TFT_database', host='localhost', port=27017)

def create_character(character_name,character_level ,trait ,description):
    charcter = Character(character_name = character_name,character_level = character_level, trait = trait ,description = description)
    charcter.save()
    print(f'The character {charcter.character_name} has been created')

def list_characters():
    characters = [character.to_json() for character in Character.objects()]
    number_of_characters = len(characters)
    return characters , number_of_characters

def delete_visitor(character_id):
    character = Character.objects(id=character_id).first().delete()
    print(f'Character with the id {character_id} has been deleted')

def update_visitor(character_id,field_update):
    character = Character.objects(id=character_id).first()
    character.update(**field_update)

def character_details(character_id):
    character = Character.objects(id=character_id).first()
    return character.to_json()

def delete_all():
    Character.objects().delete()

## TEST
# create_character(character_name='Ahri',character_level =4,trait='Spirit',description="Takes for ever to ult")
# create_character(character_name='Diana',character_level =1,trait='Moonlight',description="Strong when you have 2 other moonlight are on the board ")
# create_character(character_name='Zed',character_level =2,trait='Shade',description="Best fated champion if you get it early")
# create_character(character_name='Veigar',character_level =3,trait='Elderwood',description="BUSTED")
# create_character(character_name='Sett',character_level =5,trait='Brawler',description="Sits give HP")

# a, b = list_characters()
# print(a, b)


# print(character_details('5f8c1f5211697f0adb822822') )

# delete_visitor('5f8c1f5211697f0adb822822')
# a, b = list_characters()
# print(b)

# delete_all()

# update_visitor('5f8c27765198b3b141c02f03',{'character_name':'Lee Sin'})

# print(character_details('5f8c27765198b3b141c02f03') )

