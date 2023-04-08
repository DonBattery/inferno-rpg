# validate.py

# Ebben a file-ban validátor az az érvényesítő funkciók vannak, 
# ezek feladata, hogy bizonyos szempontok szerint megállapítsák, hogy egy bemeneti érték
# érvényes-e vagy sem. Például, hogy a karakter neve eélég hosszú-e, és nem használja-e senki más.
# Ezek a funkciók mindíg egy tuple-val térnek vissza amiben két érték van, az első egy boolean
# ami megmondja, hogy a bemeneti érték érvényes-e. A második egy string ami a hiba üzenetet tartalmazza,
# ennek csak akkor van értéke ha a bemeneti érték érvénytelen (pl.: "A Névnek legalább 3 karakter hosszúnak kell lennie.").

import re

import regex
import yaml

def validate_name(name:str, used_names:dict) -> tuple:
    if len(name) < 3:
        return False, "A Névnek legalább 3 karakter hosszúnak kell lennie."
    if len(name) > 28:
        return False, "A Név nem lehet hosszabb mint 28 karakter."
    if name in used_names:
        return False, f"A {name} név már foglalt."
    return True, ""

def validate_race(race:str, game_world:dict) -> tuple:
    if not race in game_world["races"]:
        return False, f"A {race} nem játszható faj. Játszható fajok: {', '.join(game_world['races'].keys())}"
    return True, ""

def validate_job(job:str, game_world:dict) -> tuple:
    if not job in game_world["jobs"]:
        return False, f"A {job} nem játszható kaszt. Játszható kasztok: {', '.join(game_world['jobs'].keys())}"
    return True, ""

def validate_csonti_pinput(input_str:str) -> tuple:
    # Megnézzük vannak-e Emoji-k 🐸
    emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                "]+", flags=re.UNICODE)
    if emoji_pattern.search(input_str):
        return False, "Csonti nem beszéli az emódzsík nyelvét..."

    # Csak betűket, számokat és írásjeleket engedünk.
    if regex.fullmatch(r'^[\w\s\p{P}]+$', input_str):
        return True, ""
    else:
        return False, "Csonti nem fog ilyen hieroglifákat mondani..."

def validate_game_config_file(config_file_path:str, game_element_types:list) -> tuple:
    try:
        with open(config_file_path, "r") as config_file:
            config_data = yaml.safe_load(config_file)
    except Exception as err:
        return False, f"{config_file_path}: nem lehet betölteni a konfigurációs file-t: {err}"

    if not isinstance(config_data, dict):
        return False, f"{config_file_path}: nem szabályos YAML file"

    for key in config_data:
        if not key in game_element_types:
            return False, f"{config_file_path}: a {key} nem ismert játék elem"

    return True, ""

def validate_game_config_files(config_files:list, game_element_types:list) -> tuple:
    errors = []

    for config_file_path in config_files:
        valid, msg = validate_game_config_file(config_file_path, game_element_types)
        if not valid:
            errors.append(msg)

    if errors:
        return False, "Hibás konfiguráció!\n" + '\n'.join(errors)

    return True, ""
