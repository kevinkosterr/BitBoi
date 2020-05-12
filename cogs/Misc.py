import discord
from discord.ext import commands
from bot import log_this
import requests, json
import re


class Misc(commands.Cog):
    "Misc commands"

    def prettify(self, amount, separator='.'):
        """Separate with predefined separator."""
        orig = str(amount)
        new = re.sub("^(-?\d+)(\d{3})", "\g<1>{0}\g<2>".format(separator), str(amount))
        if orig == new:
            return new
        else:
            return self.prettify(new)

    @commands.command(name='covid')
    async def covid_command(self, ctx, *subj):
        """check the latest known data of COVID-19"""
        try:
            response = requests.get('https://api.covid19api.com/summary').json()
            if not subj:
                embed = discord.Embed(
                    title='COVID-19 Global Data'
                )
                for key in response['Global'].keys():
                    keyname = re.findall('[A-Z][^A-Z]*', key)
                    embed.add_field(name=f'{keyname[0]} {keyname[1]}', value=self.prettify(response['Global'][key]),
                                    inline=False)
                log_this(f'COVID-19 data requested by: {ctx.message.author}')
                await ctx.send(embed=embed)
        except json.decoder.JSONDecodeError as e:
            log_this(e)
            await ctx.send('Oops, something went wrong...')


def setup(bot):
    bot.add_cog(Misc(bot))
