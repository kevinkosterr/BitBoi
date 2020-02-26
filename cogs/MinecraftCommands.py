from discord.ext import commands


class MinecaftCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ip')
    async def ip_command(self, ctx):
        await ctx.send('minecraftsurvival.nl:cactus:')


def setup(bot):
    bot.add_cog(MinecaftCommands(bot))
