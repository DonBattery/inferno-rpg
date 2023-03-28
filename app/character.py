# character.py

# Ebben a file-ban van minden a játékos karakterrel kapcsolatos funkció

def new_character(id, name, race, job, next_level):
    return {
        "id":id,
        "name": name,
        "race":race,
        "job": job,
        "level": 1,
        "xp": 0,
        "next_level": next_level,
    }
