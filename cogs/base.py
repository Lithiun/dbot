import discord
from discord.ext import commands

from config import config, messages
config = config.Config
messages = messages.Messages

def command_list():
    with open("commands.md", "r", encoding="utf-8") as f:
        txt = f.read()
    return txt

class Base(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #                          #
    #      Message parser      #
    #                          #

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel

        if message.content.lower().startswith(messages.uhoh) and not message.author.bot:
            await channel.send(messages.uhoh)

        elif "PR" in message.content:
            await channel.send(messages.pr_meme)

    #                                    #
    #      Invalid command handler       #
    #                                    #

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("Invalid command, try one of these:\n" + command_list())

def setup(bot):
    bot.add_cog(Base(bot))
