import random

szereplők = [
    "Rendőr",
    "Pap",
    "munkás",
    "macska",
]

tevékenység = [
    "ül a vécén",
    "levitál",
    "ugrik",
]

helyszín = [
    "parkban",
    "ünzletben",
    "fürdőkádban",
]

mondat_a = [
    "dikk lesett a számítógépem",
    "fejbeverlek egy kuglival",
    " ümmm de szaftos ez a csótány",
]

mondat_b = [
    "kostoldad már a kislábujam?",
    "szerintem akkor is egy gila vagy",
    "Nem! Lekváros!",
]

def új_vicc():
    return f"""Két {szereplők[random.randint(0, len(szereplők) - 1)]} {tevékenység[random.randint(0, len(tevékenység) - 1)]} a {helyszín[random.randint(0, len(helyszín) - 1)]}. 
Ígyszól az egyik: {mondat_a[random.randint(0, len(mondat_a) - 1)]}
Mire a másik: {mondat_b[random.randint(0, len(mondat_b) - 1)]}"""
