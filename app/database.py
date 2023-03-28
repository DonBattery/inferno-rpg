# database.py

# Ez a file kezeli az adatbázist. Itt találhatóak azok a funkciók, amik dinamikus adatokat kezelnek.
# Például a játékos karakterek profiljait, az ismert helyszíneket, stb. Ezekkel a funkciókkal lehet
# kivenni, betenni és keresni az adatbázisban.

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
