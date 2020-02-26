import discord
import sys


class BitBoi(discord.Client):
    async def on_ready(self):
        game = discord.Game('with bits and bytes')
        print('Logged in as', self.user)
        await self.change_presence(status=discord.Status.online, activity=game)


client = BitBoi()

if sys.argv[1]:
    client.run(sys.argv[1])
else:
    raise ValueError()
