# vicc.py

# Ebben a file-ban van az új_vicc parancs ami egy új véletlen vicc generálásáért felelős

import random

szereplők = [
    "rendőr",
    "pap",
    "munkás",
    "macska",
    "apáca",
    "zsidó",
    "cigány",
    "bohóc",
    "katona",
    "rokfortos pizza",
    "dinoszaurusz csontváz",
    "tengerbiológus",
    "kamikaze pilóta",
]

tevékenység = [
    "ül a vécén",
    "levitál",
    "ugróiskolázik",
    "horgászik",
    "cigizik",
    "kóborol",
    "kincset keres",
    "vadászik",
    "iszogat",
    "mozizik",
    "szotyizik",
]

helyszín = [
    "parkban",
    "üzletben",
    "fürdőkádban",
    "francia tengerparton",
    "a háború kellős közepén",
    "a világ végén",
    "a sárkány barlangjában",
    "egy csónakban a tenger közepén",
    "egy lakatlan szigeten",
    "egy oázisban",
    "a Madonna koncerten",
    "egy elsüllyedt hajóban",
    "egy lezuhant repülőben a dzungel közepén",
]

mondat_a = [
    "Dikk lesett a számítógépem!",
    "Fejbeverlek egy kuglival!",
    "ümmm de szaftos ez a csótány",
    "Kaszáltál már lekváros batyút szembeszélben?",
    "Hány éves a kapitány?",
    "Mikor jönnek a többiek?",
    "Hová lett a töpörtyű?",
]

mondat_b = [
    "Kostoldad már a kislábujam?",
    "Szerintem akkor is egy gila vagy.",
    "Nem! Lekváros!",
    "Éljen a kommunizmus!",
    "Nem! A válaszom: nem.",
    "Ez a vicc is de meg változott",
    "Vigyázzon édesapám! Saját maga felé dől!",
    "Denevéreset???",
]

def új_vicc():
    return f"""Két {random.choice(szereplők)} {random.choice(tevékenység)} a {random.choice(helyszín)}. 
Ígyszól az egyik: {random.choice(mondat_a)}
Mire a másik: {random.choice(mondat_b)}"""
