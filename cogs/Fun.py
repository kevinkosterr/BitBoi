from discord.ext import commands
import random


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


def setup(bot):
    bot.add_cog(Fun(bot))
