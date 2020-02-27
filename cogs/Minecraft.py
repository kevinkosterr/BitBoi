from discord.ext import commands
import socket


class Minecraft(commands.Cog):
    """Minecraft commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ip')
    async def ip_command(self, ctx):
        await ctx.send('minecraftsurvival.nl:cactus:')

    @commands.command(name='mcstatus')
    async def ip_command(self, ctx):
        if is_online():
            await ctx.send('The server is online!')
        else:
            await ctx.send('The server is offline')


def is_online():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    host = "minecraftsurvival.nl"
    port = 25565

    if s.connect_ex((host, port)):
        return False
    else:
        return True


def setup(bot):
    bot.add_cog(Minecraft(bot))
