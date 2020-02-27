import discord
from discord.ext import commands
import time


class Admin(commands.Cog):
    """Admin commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick_command(self, ctx, member: discord.Member, reason=None):
        await member.kick(reason=reason)
        if reason is not None:
            await ctx.send(f'{member}, has been kicked from the server. Reason: {reason}')
        else:
            await ctx.send(f'{member}, has been kicked from the server.')

    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban_command(self, ctx, member: discord.Member, reason=None):
        await member.ban(reason=reason)
        if reason is not None:
            await ctx.send(f'{member}, has been banned from the server. Reason: {reason}')
        else:
            await ctx.send(f'{member}, has been banned from the server.')

    @commands.command(name='clear')
    @commands.has_permissions(manage_messages=True)
    async def clear_command(self, ctx, amount: int):
        deleted = await ctx.channel.purge(limit=amount+1)
        delete_msg = await ctx.send(f'{len(deleted) - 1} messages have been deleted.')
        time.sleep(1)
        await discord.Message.delete(delete_msg)


def setup(bot):
    bot.add_cog(Admin(bot))
