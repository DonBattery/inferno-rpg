# Szöveges kalandjáték Discord bot
# Ez a program fő file-ja. Ezt indítjuk el, itt importáljuk a package-ket,
# rakjuk össze és futtatjuk magát a Discord bot-ot

import os

import discord
from discord.ext import commands

import handlers

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

# Kivesszük az eredeti !help parancsot, hogy betehessük a sajátunkat.
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.command()
async def vicc(ctx: commands.Context):
    """Véletlen vicc"""
    await ctx.send(handlers.handle_vicc())

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

bot.run(os.getenv("DISCORD_TOKEN"))
