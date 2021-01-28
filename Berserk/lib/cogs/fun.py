import os
import sys
import asyncio
import discord
from random import choice, randint
from typing import Optional
from discord import Member, File
from discord.ext.commands import Cog
from discord.ext.commands import command
from lib.bot.qrgen import saveQrPng
from lib.bot.imgdownload import downloadImg
from lib.bot.qrdec import qrDec

OWNERS = ["618038532665114624", "623772185315639302"]

as

class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="qrencoder", aliases=["qrgenerator", "qrgen", "qrenc"])
    async def qrencode(self, ctx, link):
        saveQrPng(link)
        await asyncio.sleep(1)
        await ctx.send(file=discord.File(r'D:\GitHub\Berserk\Berserk\qrcodeenc\{0}.png'.format(link)))
        os.remove(r'D:\GitHub\Berserk\Berserk\qrcodeenc\{0}.png'.format(link))
        return True

    @command(name="qrdecoder", aliases=["qrdec"])
    async def qrdecode(self, ctx, url):
        try:
            downloadImg(url)
            await asyncio.sleep(1)
            await ctx.send(qrDec(r"D:\GitHub\Berserk\Berserk\qrcodedec\image.png"))
            os.remove(r"D:\GitHub\Berserk\Berserk\qrcodedec\image.png")
            return True
        except:
            await ctx.send("There is something wrong with the link you have provided!")

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")


def setup(bot):
    bot.add_cog(Fun(bot))
