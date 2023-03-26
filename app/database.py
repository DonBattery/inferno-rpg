characters=[]

def add_character(character):
    characters.append(character)

def get_character_by_id(id):
    for character in characters:
        if character["id"]==id:
            return character

def get_character_by_name(name):
    for character in characters:
        if character["name"]==name:
            return character

def remove_character_by_id(id):
    global characters
    characters = [character for character in characters if character.get("id") != id]
