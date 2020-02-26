import discord
from discord.ext import commands
import sys
import cogs

bot = commands.Bot(command_prefix='.')


@bot.event
async def on_connect():
    try:
        # loads every cog inside the cogs folder
        for cog in cogs:
            bot.load_extension(cog)
    # if any exception occurs, raise it
    except Exception:
        raise


@bot.event
async def on_ready():
    game = discord.Game('with bits and bytes')
    # prints the name of the bot
    print('Logged in as', bot.user)
    # changes the presence of the bot
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.command()
@commands.has_role('Developer')
async def reload(ctx, message_id=discord.Message.id):
    for cog in cogs:
        bot.reload_extension(cog)
    await ctx.send('Cogs reloaded!:white_check_mark:')


if __name__ == '__main__':
    cogs = ['cogs.BasicCommands']
    # the token must be given as an argument
    __token__ = sys.argv[1]

    # tries to run the bot with the given token
    # if the token is wrong, it raises an exception
    if __token__:
        try:
            bot.run(__token__)
        except discord.errors.LoginFailure:
            raise
    else:
        raise ValueError()
