# database.py

# Ez a file kezeli az adatbázist. Itt találhatóak azok a funkciók, amik dinamikus adatokat kezelnek.
# Például a játékos karakterek profiljait, az ismert helyszíneket, stb. Ezekkel a funkciókkal lehet
# kivenni, betenni és keresni az adatbázisban.

import os
from typing import Dict, Optional

from tinydb import TinyDB, Query

import config

os.makedirs(config.DATA_FOLDER, exist_ok=True)

class Database:
    def __init__(self, data_folder:str, guild_id:int) -> None:
        self.guild_id = guild_id
        self.file_path = os.path.join(data_folder, f"{guild_id}-database.json")
        self.tynydb = TinyDB(self.file_path)
        self.characters = self.tynydb.table("characters")

    def add_character(self, character:dict) -> None:
        self.characters.insert(character)

    def get_character_by_id(self, id:int) -> Optional[Dict]:
        return self.characters.get(Query().id == id)

    def get_character_by_name(self, name:str) -> Optional[Dict]:
        return self.characters.get(Query().name == name)

    def remove_character_by_id(self, id) -> None:
        self.characters.remove(Query().id == id)

    def get_all_character_names(self) -> list:
        names = []
        for character in self.characters.all():
            name = character["name"]
            if not name in names:
                names.append(name)
        return names

worlds = {}

def get_guild_database(guild_id:int) -> Database:
    if guild_id in worlds:
        return worlds[guild_id]
    new_world = Database(config.DATA_FOLDER, guild_id)
    worlds[guild_id] = new_world
    return new_world
