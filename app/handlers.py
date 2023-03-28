# handlers.py

# Ebben a file-ban van az összes handler funkció. Ezek olyan funkciók amelyek egy egy
# Discord arancs kezeléséjér felelősek (handle = kezelni).

from vicc import új_vicc
import game_world
import database
import validate
import utility

def handle_vicc() -> str:
    return új_vicc()

def handle_teszt(*args) -> str:
    return f"Teszt: {args}"

def handle_csontimondja(*args) -> str:
    return utility.csonti_mondja(*args)

def handle_help(*args) -> str:
    if len(args) == 0:
        return game_world.generate_help()
    else:
        return game_world.generate_help(args[0])

def handle_profil(id:int) -> str:
    character = database.get_character_by_id(id)
    if character:
        return f"""a karaktered profilja:
```TEXT
Név: {character['name']}
Faj: {character['race']}
Kaszt: {character['job']}
```"""
    else:
        return "Neked még nincs karaktered, de az `!újkarakter` paranccsal kreálhatsz egyet magadnak."

def handle_újkarakter(id:int, *args) -> str:
    character = database.get_character_by_id(id)
    if character:
        return f"Neked már van egy {character['name']} nevű {character['race']} {character['job']} karaktered. Előszőr meg kell ölnöd őt az `!öljmegmost` parancsal, hogy újat kreálhass."
    else:
        if len(args) != 3:
            return "Az `!újkarakter` parancs pontosan három paramétert vár: Név, Faj, Kaszt. Bővebb információt a `!help újkarakter` paranccsal kaphatsz."
        valid, msg = validate.validate_name(args[0])
        if not valid:
            return msg
        valid, msg = validate.validate_race(args[1])
        if not valid:
            return msg
        valid, msg = validate.validate_job(args[2])
        if not valid:
            return msg
        new_character = game_world.new_character(id, args[0], args[1], args[2])
        database.add_character(new_character)
        return f"Új karaktered a {new_character['job']} {new_character['race']} név szerint {new_character['name']} megkezdheti kalandozásait Infernó világán. A `!profil` parancsal megtekintheted a profilod."

def handle_öljmegmost(id:int) -> str:
    character = database.get_character_by_id(id)
    if character:
        database.remove_character_by_id(id)
        return f"Karakteredet {character['name']} utolérte a végzete, lelke örökre elveszet a sötét síkon. De kreálhatsz magadnak egy újat az `!újkarakter` paranccsal."
    else:
        return "Neked még nincs karaktered de az `!újkarakter` parancsal kreálhatsz egyet magadnak."
