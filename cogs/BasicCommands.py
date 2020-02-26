from discord.ext import commands


class BasicCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='beep')
    async def beep_command(self, ctx):
        await ctx.send('Boop!:robot:')


def setup(bot):
    bot.add_cog(BasicCommands(bot))
