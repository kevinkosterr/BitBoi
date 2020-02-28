from discord.ext import commands
import discord


class Basic(commands.Cog):
    """Basic commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help_command(self, ctx, *cmd):
        """shows help"""
        server = ctx.message.guild
        # if the category isn't given, will embed of available categories
        if not cmd:
            help_embed = discord.Embed(
                title='List of commands',
                description='Use `.help <category>` to see the commands of that category'
            )
            help_embed.set_thumbnail(url=server.icon_url)
            cogs_desc = ''
            # creates a category for every cog in the list of cogs
            # and uses their docstrings as description
            for cog in self.bot.cogs:
                cogs_desc += f'{cog} - {self.bot.cogs[cog].__doc__} \n'
            help_embed.add_field(name='Categories', value=cogs_desc, inline=True)
            await ctx.send(embed=help_embed)
        elif cmd:
            # shows an error if there is more than one category given
            if len(cmd) > 1:
                help_embed = discord.Embed(
                    title='Error!',
                    description='Can\'t show multiple categories',
                    color=discord.Color.red()
                )
                help_embed.set_thumbnail(url=server.icon_url)
                await ctx.send(embed=help_embed)
            else:
                found = False
                # looks if the specified category is the same as any one
                # of the existing cogs
                for cog in self.bot.cogs:
                    if cog.lower() == cmd[0].lower():
                        help_embed = discord.Embed(
                            title=cmd[0].capitalize() + ' command list',
                        )
                        help_embed.set_thumbnail(url=server.icon_url)
                        # looks through the commands in the specified category
                        for c in self.bot.get_cog(cog).get_commands():
                            # adds the command to the embed if the command is not hidden
                            if not c.hidden:
                                help_embed.add_field(name=c.name, value=c.help, inline=False)
                        found = True
                # shows an error if the given category is not found
                if not found:
                    help_embed = discord.Embed(
                        title='Error!',
                        description=f'The {cmd[0]} category doesn\'t exist',
                        color=discord.Color.red()
                    )
                    help_embed.set_thumbnail(url=server.icon_url)
                await ctx.send(embed=help_embed)

    @commands.command(name='serverinfo', aliases=['si', 's'])
    async def server_inf_command(self, ctx):
        """shows information about the server"""
        server = ctx.message.guild
        embed = discord.Embed(
            title=server.name,
            description='Server information',
            color=discord.Color.green()
        )
        embed.add_field(name='Created at:', value=f'{str(server.created_at).split(".")[0]}')
        embed.add_field(name='Member count:', value=f'{server.member_count}', inline=True)
        embed.add_field(name='Amount of channels:', value=f'{len(server.channels)}', inline=False)
        embed.add_field(name='Server region:', value=f'{str(server.region).upper()}')
        embed.set_thumbnail(url=server.icon_url)
        embed.set_footer(text=f'Requested by {ctx.message.author}')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Basic(bot))
