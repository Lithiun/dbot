import datetime
import discord
import asyncio
from discord.ext import commands
import util

from config import config, messages
config = config.Config
messages = messages.Messages

def command_list():
    with open("commands.md", "r", encoding="utf-8") as f:
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

        await ctx.send(messages.test_success)

    @commands.command()
    async def time(self, ctx):
        """Shows the current datetime"""
        
        dt = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        await ctx.send(messages.cmd_dt.format(datetime=dt))

    @commands.command()
    async def hug(self, ctx, user: discord.Member = None):
        """Because everyone likes hugs (totally not copied from rubbergod)"""

        if user is None:
            user = ctx.author
        
        user = discord.utils.escape_markdown(user.display_name)
        await ctx.send(messages.cmd_hug.format(user=user))

    @commands.command()
    async def remindme(self, ctx, t_val: int = 1, t_unit: str = "m", remindstring: str = "Reminder"):
        """Reminds the user in n timeunits, with a specified message.
        Valid timeunits are:
        s -> second(s)
        m -> minute(s)
        h -> hour(s)
        """

        if t_unit.startswith("s"):
            secs = t_val
        elif t_unit.startswith("m"):
            secs = t_val * 60
        elif t_unit.startswith("h"):
            secs = t_val * 3600
        else:
            await ctx.send(messages.err_arg_remindme)
            return

        await ctx.message.add_reaction("✅")

        await asyncio.sleep(secs)
        await ctx.send(f"<@{ctx.author.id}>  " + remindstring)

    @commands.command()
    async def week(self, ctx):
        """Identifies the current week"""

        weeknumber = datetime.datetime.now().isocalendar()[1]

        await ctx.send(messages.weeks_cz[weeknumber % 2])

    @commands.command()
    async def godhelp(self, ctx):
        """Directs the user to a psychologist"""

        await ctx.send(messages.godhelp_meme)

    #                         #
    #      Help commands      #
    #                         #

    @commands.command()
    async def command(self, ctx):
        """Shows available commands"""
        # NOTE: Help does not work (reserved)
        await ctx.send(util.command_list())


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
