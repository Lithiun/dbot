import discord
from discord.ext import commands

import config
config = config.Config

bot = commands.Bot(command_prefix=config.command_prefix)

@bot.event
async def on_ready():
    """If DBOT is ready"""
    print("Ready")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")

@bot.command()
async def unload(ctx, extension):
    bot.load_extension(f"cogs.{extension}")

for extension in config.extensions:
    bot.load_extension(f'cogs.{extension}')
    print(f'{extension} loaded')

bot.run(config.key)
