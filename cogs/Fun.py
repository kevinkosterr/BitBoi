import discord
from discord.ext import commands

import random
import aiohttp
import json
import toml


def load_config(subj: str, part: str):
    """Loads the configuration"""
    config = toml.load('config.toml').get(subj).get(part)
    return config


class Fun(commands.Cog):
    """Fun commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='beep')
    async def beep_command(self, ctx):
        """boop!:robot:"""
        await ctx.send('Boop!:robot:')

    @commands.command(name='insultme')
    async def insult_command(self, ctx):
        """insults you"""
        author = ctx.message.author
        insults = ["you're ugly.",
                   "your mom gay.",
                   "you are proof that god has a sense of humor.",
                   "if i throw a stick, will you leave?:dog:",
                   "in the land of the retards, you will be king.",
                   "i'm jealous of all the people who haven't met you.",
                   "you pillock!",
                   "who let the simpleton out of the asylum?",
                   "you look like two of the ugliest animals merged together."
                   ]
        await ctx.send(f'{author.mention}, {random.choice(insults)}')

    @commands.command(name='gif')
    async def gif_command(self, ctx, *search: str):
        """sends a random GIF"""
        embed = discord.Embed(color=discord.Color.green())
        api_key = load_config('GIPHY', 'api_key')
        async with aiohttp.ClientSession() as session:
            if not search:
                response = await session.get(f'https://api.giphy.com/v1/gifs/random?api_key={api_key}')
                # loads the response data as json
                data = json.loads(await response.text())
                # sets the embed image to the
                # image from the response
                embed.set_image(url=data['data']['images']['original']['url'])
            else:
                response = await session.get(f'https://api.giphy.com/v1/gifs/search?q={search}&api_key={api_key}&limit=10')
                # loads the response data as json
                data = json.loads(await response.text())
                # chooses a random gif from the GIFS found by GIPHY
                gif_choice = random.randint(0, 9)
                # sets the embed image to the
                # image from the response
                embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))
