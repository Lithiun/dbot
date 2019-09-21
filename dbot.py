import datetime
import discord
from discord.ext import commands as cmds

import config
config = config.Config()

bot = cmds.Bot(command_prefix=config.command_prefix)

def command_list():
    with open("commands.md", "r") as f:
        txt = f.read()
    return txt

@bot.event
async def on_ready():
    """If DBOT is ready"""
    print("Ready")

# Commands
@bot.command()
async def test(ctx):
    await ctx.send(f"test successful!")

@bot.command()
async def dt(ctx):
    dt = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    await ctx.send(f"Current datetime is {dt}")

@bot.command()
async def commands(ctx):
        await ctx.send(command_list())

@bot.event
async def on_message(message):
    if message.content.startswith("uh oh") and not message.author.bot:
        channel = message.channel
        await channel.send("uh oh")

    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, cmds.errors.CommandNotFound):
        await ctx.send("Invalid command, try one of these:\n" + command_list())

bot.run(config.key)
