from discord.ext import commands
import discord


class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='beep')
    async def beep_command(self, ctx):
        await ctx.send('Boop!:robot:')

    @commands.command(name='serverinfo', aliases=['si', 's'])
    async def server_inf_command(self, ctx):
        embed = discord.Embed(
            description='Server information',
            color=discord.Color.blue()
        )
        embed.set_footer(text=f'Requested by {ctx.message.author}')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(BasicCommands(bot))
