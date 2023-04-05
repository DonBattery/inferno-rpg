# game_world.py

# Ebben a file-ban konstans adatok vannak Inferno világáról. Itt található az összes help szöveg is
# és a hozzá tartozó generáló funkciók is. Illetve az új adatok készítéséhez használt funkciók.

import random

from texttable import Texttable

from utility import to_text_box

import json

# Fajok
races = {
    "ember": {
        "race_type": "humanoid",
        "min_strength": 3,
        "max_strength": 18,
        "min_agility": 3,
        "max_agility": 19,
        "min_cleverness": 3,
        "max_cleverness": 20,
    },
    "gyíklény": {
        "race_type": "humanoid",
        "min_strength": 4,
        "max_strength": 19,
        "min_agility": 5,
        "max_agility": 20,
        "min_cleverness": 1,
        "max_cleverness": 16,
    },
    "manó": {
        "race_type": "humanoid",
        "min_strength": 1,
        "max_strength": 13,
        "min_agility": 3,
        "max_agility": 20,
        "min_cleverness": 2,
        "max_cleverness": 20,
    },
    "farkasember": {
        "race_type": "humanoid",
        "min_strength": 7,
        "max_strength": 20,
        "min_agility": 5,
        "max_agility": 20,
        "min_cleverness": 2,
        "max_cleverness": 15,
    },
}

# Kasztok
jobs = {
    "harcos":{
        "inventory": [
            {
                "item_type": "weapon",
                "min_damage":1,
                "max_damage":2, 
            },
        ],
        "skill": [
            {
                "skill_name": "vadászat",
                "skill_level": 3,
            },
            {
                "skill_name": "halászat",
                "skill_level": 2,
            },
            {
                "skill_name": "gyógynövény_keresés",
                "skill_level": 1,
            },
            {
                "skill_name": "kraft",
                "skill_level": 2,
            },
        ],
        "bonus": [
            {
                "bonus_type": "strength",
                "bonus_value": 2,
            },
            {
                "bonus_type": "agility",
                "bonus_value": 1,
            },
        ],
    },
    "vadász":{
        "bonus": [
            {
                "bonus_type": "strength",
                "bonus_value": 1,
            },
            {
                "bonus_type": "agility",
                "bonus_value": 2,
            },
        ],
    },
    "varázsló":{
        "bonus": [
            {
                "bonus_type": "cleverness",
                "bonus_value": 3,
            },
        ],
    },
    "pap":{
        "bonus": [
            {
                "bonus_type": "strength",
                "bonus_value": 1,
            },
            {
                "bonus_type": "cleverness",
                "bonus_value": 2,
            },
        ],
    },
    "druida":{
        "bonus": [
            {
                "bonus_type": "strength",
                "bonus_value": 1,
            },
            {
                "bonus_type": "agility",
                "bonus_value": 1,
            },
            {
                "bonus_type": "cleverness",
                "bonus_value": 1,
            },
        ]
    },
    "íjász":{
        "bonus": [
    
            {
                "bonus_type": "agility",
                "bonus_value": 3,
            },
        ]
    },
    "bányász":{
        "bonus": [
            {
                "bonus_type": "strength",
                "bonus_value": 3,
            },
        ]
    },
    "szerzetes":{
        "bonus": [
            {
                "bonus_type": "strength",
                "bonus_value": 3,
            },
        ]
    },
    "ninja":{
        "bonus": [
            {
                "bonus_type": "agility",
                "bonus_value": 2,
            },
        ]
    },
}

levels = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

help_texts = {
    "commands": {
        "help": {
            "short": "kiírja ezt az üzenetet. !help <másik_parancs> bővebb infromációt kaphatsz a másik_parancs-ról",
            "long": """A !help paranccsal információt kaphatsz a játékban használható parancsokról.

Ha paraméter nélkül adod ki a !help parancsot akkor egy listát kapsz az összes kiadható paranccsal
és rövid leírásukkal.

Hogyha egy másik parancs nevét adod meg a !help parancsnak praméterül (például: !help profil) akkor annak a parancsnak a hosszú leírását fogod visszakapni.""",
        },
        "vicc": {
            "short": "generál egy új viccet",
            "long": "A !vicc parancs generál egy új viccet véletlen szereplőkkel, helyszínnel, tevékenységgel és mondatokkal"
        },
        "profil": {
            "short": "kiírja a karaktered profilját",
        },
        "újkarakter": {
            "short": "kreál neked egy új karaktert, ha még nincs. Szükséges paraméterek: Név, Faj, Kaszt",
            "long":f"""Az !újkarakter parancsal kreálhatsz magadnak egy új karaktert, amennyiben még nincs.
            
A parancs három paramétert vár: Név, Faj, Kaszt
A név nem lehet rövidebb mint 3 és nem lehet hosszabb mint 28 karakter. És nem lehet olyan amit egy másik karakter már használ.
Játszható fajok: {', '.join(races.keys())}
Játszható kasztok: {', '.join(jobs.keys())}"""
        },
        "öljmegmost": {
            "short": "megöli a karaktered, lekét még a Sötét Síkon is túl űzi, már a Démon Urak sem segíthetnek megtalálni",
        },
    },
}

def available_commands() -> str:
    "Csinál egy szépen rendezett táblázatot a hozzáférhető parancsokból"
    tab = Texttable(max_width=42)
    tab.header(["Parancs", "Leírás"])
    for command in help_texts["commands"]:
        tab.add_row(["!" + command, help_texts["commands"][command]["short"]])
    return tab.draw()

def generate_help(command_name:str = "") -> str:
    """
    Ez a funkció legenereálja a help üzenetet a bemeneti command_name, az az parancs név alapján.
    Ha nincs input akkor egy álltalános listát kapunk vissza az összes hozzáférhető paranccsal és a rövid leírásukkal,
    ha ismeretlen parancsnév az input, akkor az output-ban ezt közöljük és visszaküldjük a fenti istát,
    ha az input parancs név ismert akkor annak a hosszú leírását kapjuk vissza.
    """
    if not command_name:
        return f"""InfernoRPG Help
Magyar szöveges kalandjáték a Discordon!

Használható parancsok:
{to_text_box(available_commands())}"""

    elif not command_name in help_texts["commands"]:
        return f"""A `!{command_name}` nem ismert parancs.

Használható parancsok:
{to_text_box(available_commands())}"""

    else:
        out = help_texts["commands"][command_name]["short"]
        if "long" in help_texts["commands"][command_name]:
            out = help_texts["commands"][command_name]["long"]
        return to_text_box(out)

def new_character(id, name, race, job):
    character = {
        "id":id,
        "name": name,
        "race":race,
        "job": job,
        "level": 1,
        "xp": 0,
        "next_level": levels[0],
        "strength": random.randint(races[race]["min_strength"], races[race]["max_strength"]),
        "agility": random.randint(races[race]["min_agility"], races[race]["max_agility"]),
        "cleverness": random.randint(races[race]["min_cleverness"], races[race]["max_cleverness"]),
    }
    for bonus in jobs[job]["bonus"]:
        character[bonus["bonus_type"]] += bonus["bonus_value"]
    return character
