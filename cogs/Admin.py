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
        """.kick <user> <reason>, kicks the specified user"""
        await member.kick(reason=reason)
        if reason is not None:
            print(f'{ctx.message.author} kicked {member}: {reason}')
            await ctx.send(f'{member}, has been kicked from the server. Reason: {reason}')
        else:
            print(f'{ctx.message.author} kicked {member}. UNKNOWN REASON')
            await ctx.send(f'{member}, has been kicked from the server.')

    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban_command(self, ctx, member: discord.Member, reason=None):
        """.ban <user> <reason>, bans the specified user"""
        await member.ban(reason=reason)
        if reason is not None:
            print(f'{ctx.message.author} has banned {member}: {reason}')
            await ctx.send(f'{member}, has been banned from the server. Reason: {reason}')
        else:
            print(f'{ctx.message.author} has banned {member}. REASON UNKNOWN')
            await ctx.send(f'{member}, has been banned from the server.')

    @commands.command(name='clear')
    @commands.has_permissions(manage_messages=True)
    async def clear_command(self, ctx, amount: int):
        """.clear <amount>, clears the amount of messages specified"""
        deleted = await ctx.channel.purge(limit=amount + 1)
        print(f'{ctx.message.author} has cleared {amount} messages.')
        delete_msg = await ctx.send(f'{len(deleted) - 1} messages have been deleted.')
        time.sleep(1)
        await discord.Message.delete(delete_msg)

    @commands.command(name='addrole', aliases=['ar'])
    @commands.has_permissions(manage_roles=True)
    async def addrole_command(self, ctx, rolename, member: discord.Member):
        """.addrole <role> <member>, adds a role to a user"""
        role = discord.utils.get(member.guild.roles, name=rolename)
        try:
            await member.add_roles(role)
            await ctx.send(f'Added {rolename} to {member.nick}\'s roles')
        except AttributeError as e:
            print(e)
            await ctx.send(f'The role \'{rolename}\' doesn\'t exist')

    @commands.command(name='removerole', aliases=['rr'])
    @commands.has_permissions(manage_roles=True)
    async def removerole_command(self, ctx, rolename, member: discord.Member):
        """.removerole <role> <member>, removes a role from a user"""
        role = discord.utils.get(member.guild.roles, name=rolename)
        try:
            await member.remove_roles(role)
            await ctx.send(f'Removed {rolename} from {member.nick}')
        except AttributeError as e:
            print(e)
            await ctx.send(f'The role \'{rolename}\' doesn\'t exist')


def setup(bot):
    bot.add_cog(Admin(bot))
