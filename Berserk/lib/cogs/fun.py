import os
import sys
import asyncio
import discord
from random import choice, randint
from typing import Optional
import discord
from discord import Member, File
from discord.ext.commands import Cog
from discord.ext.commands import command
from lib.scripts.qrgen import saveQrPng
from lib.scripts.imgdownload import downloadImg
from lib.scripts.qrdec import qrDec

OWNERS = [618038532665114624, 623772185315639302]


class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="qrencoder", aliases=["qrgenerator", "qrgen", "qrenc"])
    async def qrencode(self, ctx, link):
        saveQrPng(link)
        await asyncio.sleep(1)
        await ctx.send(file=discord.File(r'D:\GitHub\Berserk\Berserk\lib\qrcodeenc\{0}.png'.format(link)))
        await asyncio.sleep(1)
        os.remove(r'D:\GitHub\Berserk\Berserk\lib\qrcodeenc\{0}.png'.format(link))
        return True

    @command(name="qrdecoder", aliases=["qrdec"])
    async def qrdecode(self, ctx, url):
        try:
            downloadImg(url)
            await asyncio.sleep(1)
            await ctx.send(qrDec(r"D:\GitHub\Berserk\Berserk\lib\qrcodedec\image.png"))
            os.remove(r"D:\GitHub\Berserk\Berserk\lib\qrcodedec\image.png")
            return True
        except:
            await ctx.send("There is something wrong with the link you have provided!")

    @command(name="nuke", aliases=["bomball", "bomb"])
    async def nuke(safe, ctx):
        if ctx.message.author.top_role.permissions.administrator:
            msgs = []
            currentChannel = ctx.message.channel
            async for message in currentChannel.history(limit=None):
                msgs.append(message)
            await currentChannel.delete_messages(msgs)
            await ctx.send(file=File(r"D:\GitHub\Berserk\Berserk\lib\nuke.gif"))
        else:
            await ctx.send("You don't have server permissions!")

    @command(name="delete", aliases=["del", "Del", "DELETE", "DEL", "Delete"])
    async def delMessage(self, ctx, *args):
        if ctx.message.author.top_role.permissions.administrator:
            # !del all (delete all messages)
            # !del first x (delete first x messages)
            # !del last x (delete last x messages)
            # !del x (delete last x messages)
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
                        async for message in currentChannel.history(limit=None):
                            msgs.append(message)
                    if len(args) == 2:
                        try:
                            number = int(args[1])
                            if priority.lower() == "first":
                                messages = []
                                async for message in currentChannel.history(limit=None):
                                    messages.append(message)
                                messages.reverse()
                                for i in range(number):
                                    msgs.append(messages[i])
                            elif priority.lower == "last":
                                async for message in currentChannel.history(limit=number):
                                    msgs.append(message)
                        except ValueError:
                            await ctx.send(
                                "```!del all (delete all messages)\n!del first x (delete first x messages)\n!del last x (delete last x messages)\n!del x (delete last x messages)```")

                    elif len(args) > 2:
                        await ctx.send(
                            "```!del all (delete all messages)\n!del first x (delete first x messages)\n!del last x (delete last x messages)\n!del x (delete last x messages)```")
                await currentChannel.delete_messages(msgs)
            else:
                await ctx.send(
                    "```!del all (delete all messages)\n!del first x (delete first x messages)\n!del last x (delete last x messages)\n!del x (delete last x messages)```")
        else:
            await ctx.send("You don't have server permissions!")

    @command(name="lorem")
    async def lorem(self, ctx, limit):
        # +lorem x
        await ctx.message.delete()
        import lorem
        for i in range(int(limit)):
            await ctx.send(f"{i} --> {lorem.sentence()}")

    @command(name="ban")
    async def ban(self, ctx, *user: discord.Member):
        if ctx.message.author.top_role.permissions.administrator:
            try:
                await ctx.guild.ban(user[0])
            except:
                await ctx.send("Such user does not exist or you have a missing argument!")
        else:
            await ctx.send("You don't have server permissions!")


    @command(name="delchannel")
    async def delChannel(self,ctx,*channel_name:discord.channel.TextChannel):
        if ctx.message.author.top_role.permissions.administrator:
            try:
                await ctx.send("Deleting the channel `{0}`".format(channel_name[0]))
                await asyncio.sleep(1.5)
                await channel_name[0].delete()
                return True
            except:
                await ctx.send("Such channel does not exist!")
        else:
            await ctx.send("You don't have server permissions!")

    @command(name="users", aliases=["usersdiscord", "totalusers"])
    async def users_dc(self, ctx):
        await ctx.message.delete()
        if ctx.message.author.id in OWNERS:
            for i in OWNERS:
                user = await self.bot.fetch_user(int(i))
                userCount = 0
                for j in self.bot.guilds:
                    userCount += j.member_count
                try:
                    await user.send(
                        "There are {0} users in {1} servers using the bot!".format(userCount, len(self.bot.guilds)))
                except:
                    pass
        else:
            await ctx.send("You are not the owner of the bot! Only owners can access this command!")

    @command(name="servers", aliases=["server", "totalservers"])
    async def total_servers(self, ctx):
        await ctx.message.delete()
        if ctx.message.author.id in OWNERS:
            for i in OWNERS:
                user = await self.bot.fetch_user(int(i))
                try:
                    await user.send("BOT is currently in {0} servers!".format(len(self.bot.guilds)))
                except:
                    pass
        else:
            await ctx.send("Dear {0}, you are not the owner of the bot! Only owners can access this command!".format(
                ctx.message.author.name))


    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")


def setup(bot):
    bot.add_cog(Fun(bot))
