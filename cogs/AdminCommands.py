import discord
from discord.ext import commands


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    async def kick_command(self, ctx, member: discord.Member, reason=None):
        await ctx.kick(member)
        if reason is not None:
            await ctx.send(f'{member}, has been kicked from the server. Reason: {reason}')
        else:
            await ctx.send(f'{member}, has been kicked from the server.')

    @commands.command(name='clear')
    async def clear_command(self, ctx, amount: int):
        await ctx.send('Clearing messages.. this may take some time.')
        deleted = await ctx.purge(limit=amount)
        await ctx.send(f'Deleted {len(deleted)} messages')


def setup(bot):
    bot.add_cog(AdminCommands(bot))

