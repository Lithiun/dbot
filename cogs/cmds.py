import datetime
import discord
from discord.ext import commands

def command_list():
    with open("commands.md", "r") as f:
        txt = f.read()
    return txt

class Cmds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #                            #
    #      General commands      #
    #                            #

    @commands.command()
    async def test(self, ctx):
        await ctx.send(f"test successful!")

    @commands.command()
    async def time(self, ctx):
        dt = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        await ctx.send(f"Current datetime is {dt}")

    @commands.command()
    async def hug(self, ctx, user: discord.Member = None):
        """Because everyone likes hugs (totally not copied from rubbergod)"""
        if user is None:
            user = ctx.author
        
        user = discord.utils.escape_markdown(user.display_name)
        await ctx.send("<:peepoHug:625338190911373318>" + f" **{user}**")

    #                         #
    #      Help commands      #
    #                         #

    @commands.command()
    async def command(self, ctx):
        await ctx.send(command_list())

    # NOTE: Help does not work (reserved)
    # @commands.command()
    # async def help(self, ctx):
    #     await ctx.send(command_list())

def setup(bot):
    bot.add_cog(Cmds(bot))
