from texttable import Texttable

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
    "harcos":{},
    "vadász":{},
    "varázsló":{},
    "pap":{},
    "druida":{},
    "íjász":{},
    "bányász":{},
    "szerzetes":{},
    "ninja":{},
}

levels = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

def new_character(id, name, race, job):
    return {
        "id":id,
        "name": name,
        "race":race,
        "job": job,
        "level": 1,
        "xp": 0,
        "next_level": levels[0],
    }

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

def to_text_box(input_text:str) ->str:
    "Egy Discord-os szöveg dobozt csinál a bemeneti szövegből"
    return f"""```TEXT
{input_text}
```"""

def available_commands() -> str:
    "Csinál egy szépen rendezett táblázatot a hozzáférhető parancsokból"
    tab = Texttable(max_width=120)
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