import sqlite3
import datetime
import discord
import asyncio
import os
from discord.ext import commands

from config import config, messages
config = config.Config
messages = messages.Messages

class Timetable(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def getTimetable(self, weekday):
        # TODO: Move timetable.dm name to config
        conn = sqlite3.connect("timetable.db")
        c = conn.cursor()

        daystr = "Dnesny rozvrh:"
        for line in c.execute('SELECT * FROM timetable WHERE day=?', str(weekday)):
            # TODO: Rewrite these awful lines
            iusweeks = [41, 43, 46]
            if str(line[0]) == "1" and line[1] == "IUS" and datetime.datetime.now().isocalendar()[1] not in iusweeks:
                continue

            daystr += f"\n`{line[1]} od {line[2]} do {line[3]} v [{line[4]}] : {line[5]}`"

        conn.close()
        return daystr

    @commands.command()
    async def rozvrh(self, ctx):
        if not os.path.isfile("timetable.db"):
            await ctx.send("Timetable database not found!")
            return

        await ctx.send(self.getTimetable(datetime.datetime.today().weekday()))

    @commands.command()
    async def timetable(self, ctx):
        if not os.path.isfile("timetable.db"):
            await ctx.send("Timetable database not found!")
            return

        await ctx.send(self.getTimetable(datetime.datetime.today().weekday()))

   


def setup(bot):
    bot.add_cog(Timetable(bot))
