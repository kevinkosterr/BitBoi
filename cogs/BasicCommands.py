from discord.ext import commands


class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='beep')
    async def beep_command(self, ctx):
        await ctx.send('Boop!:robot:')


def setup(bot):
    bot.add_cog(BasicCommands(bot))
