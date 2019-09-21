import datetime
import discord
from discord.ext import commands

import config
config = config.Config()

bot = commands.Bot(command_prefix = config.command_prefix)

@bot.event
async def on_ready():
    """If DBOT is ready"""
    print("Ready")

@bot.command()
async def test(ctx):
    await ctx.send(f"test successful!")

@bot.command()
async def dt(ctx):
    dt = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    await ctx.send(f"Current datetime is {dt}")

bot.run(config.key)
