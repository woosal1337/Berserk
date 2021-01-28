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


    @command(name="delete", aliases=["del","Del","DELETE","DEL","Delete"])
    async def delete(self, ctx, *args):
        # +del all (delete all messages)
        # +del first x (delete first x messages)
        # +del last x (delete last x messages)
        # +del x (delete last x messages)
        if len(args) != 0:
            await ctx.message.delete()
            msgs = []
            currentChannel = ctx.message.channel
            try:
                number = int(args[0])
                async for message in currentChannel.history(limit=number):
                    msgs.append(message)
            except ValueError:
                priority = args[0]
                if priority.lower() == "all":
                    async for message in currentChannel.history(limit=10000000000000000):
                        msgs.append(message)
                if len(args) == 2:
                    try:
                        number = int(args[1])
                        if priority.lower() == "first":
                            messages = []
                            async for message in currentChannel.history(limit=10000000000000000):
                                messages.append(message)
                            messages.reverse()
                            for i in range(number):
                                msgs.append(messages[i])
                        elif priority.lower == "last":
                            async for message in currentChannel.history(limit=number):
                                msgs.append(message)
                    except ValueError:
                        await ctx.send(
                            "`+del all (delete all messages)`\n`+del first x (delete first x messages)`\n`+del last x (delete last x messages)`\n`+del x (delete last x messages)`")

                elif len(args) > 2:
                    await ctx.send(
                        "`+del all (delete all messages)`\n`+del first x (delete first x messages)`\n`+del last x (delete last x messages)`\n`+del x (delete last x messages)`")
            
            await currentChannel.delete_messages(msgs)
        else:
            await ctx.send("`+del all (delete all messages)`\n`+del first x (delete first x messages)`\n`+del last x (delete last x messages)`\n`+del x (delete last x messages)`")
    @command(name="lorem")
    async def lorem(self,ctx,limit):
        # +lorem x
        await ctx.message.delete()
        import lorem
        for i in range(int(limit)):
            await ctx.send(f"{i} --> {lorem.sentence()}")

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")


def setup(bot):
    bot.add_cog(Fun(bot))
