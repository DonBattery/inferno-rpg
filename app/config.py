from decouple import config

DISCORD_TOKEN = config("DISCORD_TOKEN", None)

CONFIG_FOLDER = config("CONFIG_FOLDER", "game-config")

DATA_FOLDER = config("DATA_FOLDER", "app-data")

TEXT_BOX_MAX_WIDTH = config("TEXT_BOX_MAX_WIDTH", 42)
