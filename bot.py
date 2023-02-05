# This example requires the 'members' privileged intent to use the Member converter
# and the 'message_content' privileged intent for prefixed commands.

import random

import discord
from discord.ext import commands
from vicc import új_vicc

description = """
Egyszerű szöveges kaland RPG
"""

intents = discord.Intents.default()
intents.members = True
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

bot.run("ide jön a Discord token")
