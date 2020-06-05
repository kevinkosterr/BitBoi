from discord.ext import commands
import discord
import logging


class Events(commands.Cog):
    """Events"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        role = discord.utils.get(member.guild.roles, name='Member')
        channel = self.bot.get_channel(707891514335821835)
        try:
            await member.add_roles(role)
        except Exception:
            logging.error(f'Something went wrong. {role} role can\'t be added to {member}', exc_info=True)
            raise
        await channel.send(f'Welcome to the party {member.mention}!:partying_face:')

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = self.bot.get_channel(707891514335821835)
        await channel.send(f'{member.display_name} left us:cry:')


def setup(bot):
    bot.add_cog(Events(bot))
