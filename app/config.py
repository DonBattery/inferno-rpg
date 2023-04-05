from decouple import config

DISCORD_TOKEN = config("DISCORD_TOKEN", None)

CONFIG_FOLDER = config("CONFIG_FOLDER", "../conf")

DATA_FOLDER = config("DATA_FOLDER", "../app-data")
