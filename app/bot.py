# bot.py

# Ez a program fő file-ja. Ezt indítjuk futtatjuk a parancssorból, 
# itt rakjuk össze és indítjuk el, magát a Discord bot-ot.

import os
import random
from datetime import datetime

import discord
from discord.ext import commands

import handlers

# Felpörgetjük a véletlen szám generátorunkat, hogy biztos véletlen legyen az a véletlen.
random.seed(datetime.now().timestamp())

# Létrehozzuk a bot objektumot
description = """
 ___    ____________
|- -|  /            \
 \|/ _| Inferno RPG |
 |||   \____________/
"""
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    description=description,
    intents=intents,
)

# Kivesszük az eredeti !help parancsot, hogy betehessük a sajátunkat.
bot.remove_command('help')

# Ha sikerül csatlakozni a Discord-hoz írjunk egy üzenetet a terminálra
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

# Innentől kezdve egyesével felpakoljuk a parancsokat a bot-ra. Lényegében minden
# parancs a neki megfelelő handler funkciónak fogja tovább passzolni a Discord kontextust (ctx: commands.Context)
# és az esetleges inputokat (*args). A kontextusból fogjuk tudni, hogy melyik Discord user írta be a parancsot
# és az inputokból fogjuk tudni, hogy mit írt a parancs után (pl. !újkarakter Tapsi manó ninja) ebben
# az esetben az args = ('Tapsi','manó','ninja')
# A handler funkciók minden esetben egy szöveggel térnek vissza, ezt vagy simán beírjuk a csatornába, 
# ahonnan a parancs jött, vagy előtte mention-oljuk (@kukaccal) a felhasználót aki beírta a parancsot.
@bot.command()
async def vicc(ctx: commands.Context):
    """Véletlen vicc"""
    await ctx.send(handlers.handle_vicc())

@bot.command()
async def csontimondja(ctx: commands.Context, *args):
    """Kimondatja Csontival az input-ot"""
    await ctx.send(handlers.handle_csontimondja(*args))

@bot.command(aliases=["test"])
async def teszt(ctx: commands.Context, *args):
    """Teszt parancs"""
    await ctx.send(f"{ctx.author.mention} {handlers.handle_teszt(*args)}")

@bot.command()
async def help(ctx: commands.Context, *args):
    """Teszt parancs"""
    await ctx.send(handlers.handle_help(*args))

@bot.command()
async def profil(ctx: commands.Context):
    """Karakter profil"""
    await ctx.send(f"{ctx.author.mention} {handlers.handle_profil(ctx.author.id)}")

@bot.command(aliases=["ujkarakter"])
async def újkarakter(ctx: commands.Context, *args):
    """Új karakter alkotás"""
    await ctx.send(f"{ctx.author.mention} {handlers.handle_újkarakter(ctx.author.id, *args)}")

@bot.command(aliases=["oljmegmost"])
async def öljmegmost(ctx: commands.Context):
    """Megöli a karaktered a lelkét elűzi a sötét síkra"""
    await ctx.send(f"{ctx.author.mention} {handlers.handle_öljmegmost(ctx.author.id)}")

# Végül elindítjuk magát a bot-ot. Megpróbál "betelefonálni" a Discord-ba a DISCORD_TOKEN segítségével.
# Ha sikerül akkor elérhető lesz azokon a szervereken (guild-ekben), amikhez hozzá lett adva. A program egy
# (végtelen) ciklusba kezd, ha bármi számára értelmes parancsot lát bárhol, megfuttatja a megfelelő handler
# funkciót és vissza küldi a választ oda ahonnan a parancs jött.
bot.run(os.getenv("DISCORD_TOKEN"))
