# handlers.py

# Ebben a file-ban van az összes handler funkció. Ezek olyan funkciók amelyek egy egy
# Discord arancs kezeléséjér felelősek (handle = kezelni).

import config
import database
import validate
import game_engine
import text_utility

from vicc import új_vicc

def handle_vicc() -> str:
    return új_vicc()

def handle_teszt(*args) -> str:
    return f"Teszt: {args}"

def handle_csontimondja(*args) -> str:
    valid, message = validate.validate_csonti_pinput(''.join(args))
    if not valid:
        return text_utility.csonti_mondja2(*message.split(' '), max_width=config.TEXT_BOX_MAX_WIDTH)
    return text_utility.csonti_mondja2(*args, max_width=config.TEXT_BOX_MAX_WIDTH)

def handle_help(game_world:dict, *args) -> str:
    if len(args) == 0:
        return game_engine.generate_help()
    else:
        return game_engine.generate_help(args[0])

def handle_profil(guild_id:int, user_id:int) -> str:
    character = database.get_guild_database(guild_id).get_character_by_id(user_id)
    if character:
        return f"""a karaktered profilja:
```TEXT
Név            : {character['name']}
Faj            : {character['race']}
Kaszt          : {character['job']}
---
Szint          : {character['level']}
Tapasztalat    : {character['xp']}
Következő_szint: {character['next_level']}
---
Erő            : {character['strength']}
Ügyesség       : {character['agility']}
Okosság        : {character['cleverness']}
```"""
    else:
        return "Neked még nincs karaktered, de az `!újkarakter` paranccsal kreálhatsz egyet magadnak."

def handle_újkarakter(game_world:dict, guild_id:int, user_id:int, *args) -> str:
    guild_database = database.get_guild_database(guild_id)
    character = guild_database.get_character_by_id(user_id)
    if character:
        return f"Neked már van egy {character['level']} szintű {character['race']} {character['job']} karaktered (bizonyos {character['name']}). Előszőr meg kell őt ölnöd az `!öljmegmost` paranccsal, hogy újat kreálhass magadnak."
    else:
        if len(args) != 3:
            return "Az `!újkarakter` parancs pontosan három inputot vár: Név, Faj, Kaszt. Bővebb információt a `!help újkarakter` paranccsal kaphatsz."
        valid, msg = validate.validate_name(args[0], guild_database.get_all_character_names())
        if not valid:
            return msg
        valid, msg = validate.validate_race(args[1], game_world)
        if not valid:
            return msg
        valid, msg = validate.validate_job(args[2], game_world)
        if not valid:
            return msg
        new_character = game_engine.new_character(user_id, args[0], args[1], args[2])
        guild_database.add_character(new_character)
        return f"Új karaktered egy {new_character['race']} {new_character['job']} név szerint {new_character['name']} megkezdheti kalandozásait Infernó világán. A `!profil` parancsal megnézheted a profilod."

def handle_öljmegmost(guild_id:int, user_id:int) -> str:
    guild_database = database.get_guild_database(guild_id)
    character = guild_database.get_character_by_id(user_id)
    if character:
        guild_database.remove_character_by_id(user_id)
        return f"Karakteredet {character['name']} utolérte a végzete, lelke örökre elveszet a sötét síkon. De kreálhatsz magadnak egy újat az `!újkarakter` paranccsal."
    else:
        return "Neked még nincs karaktered de az `!újkarakter` parancsal kreálhatsz magadnak egyet."
