import sys
from random import choice, randint
from typing import Optional
from discord import Member, File
from discord.ext.commands import Cog
from discord.ext.commands import command

OWNERS = ["618038532665114624", "623772185315639302"]


class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="qrgenerator", aliases=["qrgen"])
    async def leftspin(self, ctx, *link):
        
        

        #await ctx.send(link)
        return True

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")


def setup(bot):
    bot.add_cog(Fun(bot))
