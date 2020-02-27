from discord.ext import commands
import discord


class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help_command(self, ctx, *cmd):
        author = ctx.message.author

        basic_embed = discord.Embed(
            color=discord.Color.blue(),
            description=f'the current prefix is: {self.bot.command_prefix}'
        )
        basic_embed.set_author(name='Basic commands')
        basic_embed.add_field(name='.beep', value='BOOP!', inline=False)
        basic_embed.add_field(name='.serverinfo', value='Shows server info', inline=False)

        minecraft_embed = discord.Embed(
            color=discord.Color.green()
        )
        minecraft_embed.set_author(name='Minecraft commands')
        minecraft_embed.add_field(name='.ip', value='Shows ip address of minecraft server', inline=False)

        admin_embed = discord.Embed(
            color=discord.Color.red()
        )
        admin_embed.set_author(name='Admin commands')
        admin_embed.add_field(name='.kick', value='Kicks the specified member', inline=False)
        admin_embed.add_field(name='.ban', value='Bans the specified member', inline=False)
        admin_embed.add_field(name='.clear', value='Deletes messages', inline=False)

        admin_role = discord.utils.find(lambda r: r.name == 'Bit-Developer', ctx.message.guild.roles)
        if admin_role in author.roles:
            await ctx.send(embed=basic_embed)
            await ctx.send(embed=minecraft_embed)
            await ctx.send(embed=admin_embed)
        else:
            await ctx.send(embed=basic_embed)
            await ctx.send(embed=minecraft_embed)

    @commands.command(name='beep')
    async def beep_command(self, ctx):
        await ctx.send('Boop!:robot:')

    @commands.command(name='serverinfo', aliases=['si', 's'])
    async def server_inf_command(self, ctx):
        embed = discord.Embed(
            description='Server information',
            color=discord.Color.blue()
        )
        embed.set_footer(text=f'Requested by {ctx.message.author}')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(BasicCommands(bot))
