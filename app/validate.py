# validate.py

# Ebben a file-ban validátor az az érvényesítő funkciók vannak, 
# ezek feladata, hogy bizonyos szempontok szerint megállapítsák, hogy egy bemeneti érték
# érvényes-e vagy sem. Például, hogy a karakter neve eélég hosszú-e, és nem használja-e senki más.
# Ezek a funkciók mindíg egy tuple-val térnek vissza amiben két érték van, az első egy boolean
# ami megmondja, hogy a bemeneti érték érvényes-e. A második egy string ami a hiba üzenetet tartalmazza,
# ennek csak akkor van értéke ha a bemeneti érték érvénytelen (pl.: "A Névnek legalább 3 karakter hosszúnak kell lennie.").

import regex
import re

import database
import game_world

def validate_name(name:str) -> tuple:
    if len(name) < 3:
        return (False, "A Névnek legalább 3 karakter hosszúnak kell lennie.")
    if len(name) > 28:
        return (False, "A Név nem lehet hosszabb mint 28 karakter.")
    if database.get_character_by_name(name):
        return (False, f"A {name} név már foglalt.")
    return (True, "")

def validate_race(race:str) -> tuple:
    if not race in game_world.races:
        return (False, f"A {race} nem játszható faj. Játszható fajok: {', '.join(game_world.races.keys())}")
    return (True, "")

def validate_job(job:str) -> tuple:
    if not job in game_world.jobs:
        return (False, f"A {job} nem játszható kaszt. Játszható kasztok: {', '.join(game_world.jobs.keys())}")
    return (True, "")

def validate_csonti_pinput(input_str:str) -> tuple:
    # Megnézzük vannak-e Emoji-k 🐸
    emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                "]+", flags=re.UNICODE)
    if emoji_pattern.search(input_str):
        return (False, "Csonti nem beszéli az emódzsík nyelvét...")

    # Csak Magyar szavakart engedünk, Arab számokat és alap írásjeleket.
    if regex.fullmatch(r'^[\w\s\p{P}]+$', input_str):
        return (True, "")
    else:
        return (False, "Csonti nem fog ilyen hieroglifákat mondani...")
