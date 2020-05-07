import discord
from discord.ext import commands

import sys
import os

bot = commands.Bot(command_prefix='.')
bot.remove_command('help')


@bot.event
async def on_connect():
    # start reading cogs from the cogs directory
    for cog in os.listdir('cogs'):
        # excluding __init__ and __pycache__
        if is_cog(cog):
            # splitting the cog name
            cog = cog.split('.py')[0]
            # adding cogs. before the cog name
            # this way you get cogs.PACKAGE_NAME
            # so the extension loader will load the cog
            cog = 'cogs.' + cog
            # append the cog to the list of cogs
            cogs.append(cog)
        else:
            pass
    try:
        # loads every cog inside the cogs folder
        for cog in cogs:
            bot.load_extension(cog)
        print(f'Cogs loaded: {cogs}')
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


def is_cog(filename: str):
    """
    Checks if the given filename is a valid cog
    """
    if not filename.startswith('__'):
        return True
    else:
        return False


def check_for_new_cogs():
    """
    Checks the cogs directory if there have been added any new cogs,
    if so it appends them to the cogs list.
    """
    # start reading cogs from the cogs directory
    for cog in os.listdir('cogs'):
        if is_cog(cog):
            # splitting the cog name
            cog = cog.split('.py')[0]
            # adding cogs. before the cog name
            # this way you get cogs.PACKAGE_NAME
            # so the extension loader will load the cog
            cog = 'cogs.' + cog
            # append the cog to the list of cogs if it doesn't
            # already exist
            if cog not in cogs:
                cogs.append(cog)
                print(f'New extension found named: {cog}')
            else:
                pass


@bot.command()
@commands.has_role('Bit-Developer')
async def reload(ctx):
    check_for_new_cogs()
    for cog in cogs:
        bot.reload_extension(cog)
    print(f'{ctx.message.author} reloaded the cogs.')
    await ctx.send('Cogs reloaded!:white_check_mark:')


if __name__ == '__main__':
    # this list will be filled automatically when
    # starting up the bot
    cogs = []

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
