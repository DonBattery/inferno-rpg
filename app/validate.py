import database
import game_data

def validate_name(name:str) -> tuple:
    if len(name) < 3:
        return (False, "A Névnek legalább 3 karakter hosszúnak kell lennie.")
    if len(name) > 28:
        return (False, "A Név nem lehet hosszabb mint 28 karakter.")
    if database.get_character_by_name(name):
        return (False, f"A {name} név már foglalt.")
    return (True, "")

def validate_race(race:str) -> tuple:
    if not race in game_data.races:
        return (False, f"A {race} nem játszható faj. Játszható fajok: {', '.join(game_data.races.keys())}")
    return (True, "")

def validate_job(job:str) -> tuple:
    if not job in game_data.jobs:
        return (False, f"A {job} nem játszható kaszt. Játszható kasztok: {', '.join(game_data.jobs.keys())}")
    return (True, "")
