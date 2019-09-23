import datetime
import discord
import asyncio
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
        """Response test command"""

        await ctx.send(f"test successful!")

    @commands.command()
    async def time(self, ctx):
        """Shows the current datetime"""
        
        dt = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        await ctx.send(f"Current datetime is {dt}")

    @commands.command()
    async def hug(self, ctx, user: discord.Member = None):
        """Because everyone likes hugs (totally not copied from rubbergod)"""

        if user is None:
            user = ctx.author
        
        user = discord.utils.escape_markdown(user.display_name)
        await ctx.send("<:peepoHug:625338190911373318>" + f" **{user}**")

    @commands.command()
    async def remindme(self, ctx, t_val: int = 1, t_unit: str = "minute", remindstring: str = "reminder"):
        """Reminds the user in n minutes, valid formats are:
        n second(s)
        n minute(s)
        n hour(s)
        """

        if t_unit.startswith("second"):
            secs = t_val
        elif t_unit.startswith("minute"):
            secs = t_val * 60
        elif t_unit.startswith("hour"):
            secs = t_val * 3600
        else:
            await ctx.send("invalid time unit")
            return

        await ctx.message.add_reaction("✅")

        await asyncio.sleep(secs)
        await ctx.send(f"<@{ctx.author.id}>  " + remindstring)

    @commands.command()
    async def week(self, ctx):
        """Identifies the current week"""

        weeknumber = datetime.datetime.now().isocalendar()[1]

        await ctx.send("Lichý" if weeknumber % 2 else "Sudý")

    @commands.command()
    async def godhelp(self, ctx):
        """Directs the user to a psychologist"""

        await ctx.send("https://www.lli.vutbr.cz/psychologicke-poradenstvi")

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

    #                           #
    #      General methods      #
    #                           #

    # def parseTime(self, strtime):
    #     """Parses time from remindme parameters
    #     returns seconds
    #     """
    #     print(strtime)
    #     return strtime


def setup(bot):
    bot.add_cog(Cmds(bot))
