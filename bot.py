import discord
from discord.ext import commands
import sys
import cogs

client = commands.Bot(command_prefix='.')


@client.event
async def on_connect():
    try:
        for cog in cogs:
            client.load_extension(cog)
    except Exception:
        raise


@client.event
async def on_ready():
    game = discord.Game('with bits and bytes')
    print('Logged in as', client.user)
    await client.change_presence(status=discord.Status.online, activity=game)


__token__ = sys.argv[1]

if __token__:
    try:
        client.run(__token__)
    except discord.errors.LoginFailure:
        raise
else:
    raise ValueError()
