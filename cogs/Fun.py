from discord.ext import commands


class Fun(commands.Cog):
    """Fun commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='beep')
    async def beep_command(self, ctx):
        """boop!:robot:"""
        await ctx.send('Boop!:robot:')


def setup(bot):
    bot.add_cog(Fun(bot))
