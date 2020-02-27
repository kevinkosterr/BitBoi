from discord.ext import commands
import discord


class Basic(commands.Cog):
    """Basic commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help_command(self, ctx, *cmd):
        if not cmd:
            help_embed = discord.Embed(
                title='List of commands',
                description='Use `.help <category>` to see the commands of that category'
            )
            cogs_desc = ''
            for cog in self.bot.cogs:
                cogs_desc += f'{cog} - {self.bot.cogs[cog].__doc__} \n'
            help_embed.add_field(name='Categories', value=cogs_desc, inline=True)
            cmd_desc = ''
            for cog in self.bot.walk_commands():
                if not cog.cog_name and not cog.hidden:
                    cmd_desc += f'{cog.cog_name} - {cog.help} \n'
                    help_embed.add_field(name='Uncategorized commands', inline=False)
                    help_embed.add_field(name=str(cog), value=cog.get_commands().__doc__)
            await ctx.send(embed=help_embed)
        elif cmd:
            if len(cmd) > 1:
                help_embed = discord.Embed(
                    title='Error!',
                    description='Can\'t show multiple categories',
                    color=discord.Color.red()
                )
                await ctx.send(embed=help_embed)
            else:
                found = False
                for cog in self.bot.cogs:
                    if cog.lower() == cmd[0].lower():
                        help_embed = discord.Embed(
                            title=cmd[0].capitalize() + ' command list',
                        )
                        for c in self.bot.get_cog(cog).get_commands():
                            if not c.hidden:
                                help_embed.add_field(name=c.name, value=c.help, inline=False)
                        found = True
                if not found:
                    help_embed = discord.Embed(
                        title='Error!',
                        description=f'The {cmd[0]} category doesn\'t exist',
                        color=discord.Color.red()
                    )
                await ctx.send(embed=help_embed)

    @commands.command(name='serverinfo', aliases=['si', 's'])
    async def server_inf_command(self, ctx):
        embed = discord.Embed(
            description='Server information',
            color=discord.Color.blue()
        )
        embed.set_footer(text=f'Requested by {ctx.message.author}')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Basic(bot))