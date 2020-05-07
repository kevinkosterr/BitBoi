from discord.ext import commands
import socket


class Minecraft(commands.Cog):
    """Minecraft commands"""

    def __init__(self, bot):
        self.bot = bot
        self.online = self.is_online()

    @commands.command(name='ip')
    async def ip_command(self, ctx):
        """gives the ip address of the server"""
        await ctx.send('play.minecraftsurvival.nl:cactus:')

    @commands.command(name='mcstatus')
    async def mcstatus_command(self, ctx):
        """shows if the server is online or not"""
        if self.online:
            await ctx.send('The server is online!')
        else:
            await ctx.send('The server is offline:cry:')

    @staticmethod
    def is_online():
        """
            Checks if the server is online.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        host = "play.minecraftsurvival.nl"
        port = 25565
        if s.connect_ex((host, port)):
            return False
        else:
            return True


def setup(bot):
    bot.add_cog(Minecraft(bot))
