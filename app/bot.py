# Szöveges kalandjáték Discord bot
# Ez a program fő file-ja. Ezt indítjuk el, itt importáljuk a package-ket,
# rakjuk össze és futtatjuk magát a Discord bot-ot

import os

import discord
from discord.ext import commands

from vicc import új_vicc
import database

description = """
Egyszerű szöveges kaland RPG
"""

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    description=description,
    intents=intents,
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.command()
async def vicc(ctx: commands.Context):
    """Véletlen vicc"""
    await ctx.send(új_vicc())

@bot.command()
async def profil(ctx: commands.Context):
    """Karakter profil"""
    character = database.get_character_by_id(ctx.author.id)
    if character:
        await ctx.send(f"Név: {character['name']} Nem: {character['sex']} Faj: {character['race']} Kaszt: {character['job']}")
    else:
        await ctx.send("Neked még nincs karaktered de az `!újkarakter` parancsal csinálhatsz egyet magadnak.")

@bot.command()
async def újkarakter(ctx: commands.Context, name, sex, race, job):
    """Új karakter alkotás"""
    character = database.get_character_by_id(ctx.author.id)
    if character:
        await ctx.send(f"Neked már van egy {character['name']} nevű karaktered előszőr meg kell ölnöd őt az `!öljmegmost` parancsal, hogy újat kreálhass.")
    else:
        new_character = database.new_character(ctx.author.id, name, sex, race, job)
        database.add_character(new_character)
        await ctx.send(f"Új karaktered a {new_character['sex']} {new_character['job']} {new_character['race']} név szerint {new_character['name']} megkezdheti kalandozásait a világban a `!profil` parancsal megtekintheted a profilod.")

@bot.command()
async def öljmegmost(ctx: commands.Context):
    """Megöli a karaktered a lelkét elűzi a sötét síkra"""
    character = database.get_character_by_id(ctx.author.id)
    if character:
        database.kill_character_by_id(ctx.author.id)
        await ctx.send(f"{character['name']} utolérte a végzet, lelke örökre elveszet a sötét síkon. De kreálhatsz magadnak egy új karaktert a `!újkarakter` paranccsal.")
    else:
        await ctx.send("Neked még nincs karaktered de az `!újkarakter` parancsal csinálhatsz egyet magadnak.")

bot.run(os.getenv("DISCORD_TOKEN"))
