characters=[]

def add_character(character):
    characters.append(character)

def new_character(id, name, sex, race, job):
    return {
        "id":id,
        "name": name,
        "sex": sex,
        "race":race,
        "job": job,
    }

def get_character_by_id(id):
    for character in characters:
        if character["id"]==id:
            return character

def kill_character_by_id(id):
    global characters
    characters = [character for character in characters if character.get("id") != id]
