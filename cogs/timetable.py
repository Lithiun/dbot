import sqlite3
import datetime
import discord
import asyncio
import os
from discord.ext import commands

class Timetable(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def getTimetable(self, weekday):
        # TODO: Move timetable.dm name to config
        conn = sqlite3.connect("timetable.db")
        c = conn.cursor()

        daystr = "Dnesny rozvrh:"
        for line in c.execute('SELECT * FROM timetable WHERE day=?', str(weekday)):
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
