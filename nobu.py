import discord
import auth
from discord.ext import commands

token = auth.token
owner = auth.owner
bot = commands.Bot(command_prefix='!')
bot.load_extension('misc')
bot.load_extension('music')
bot.load_extension('mal')
bot.load_extension('game')

@bot.event
async def on_ready():
    try:
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        await bot.change_presence(activity=discord.Activity(name="!help to see what\'s nobu", type=discord.ActivityType.playing))

    except Exception as e:
        print(e)

#checks for banned words in my personal server 
@bot.event
async def on_message(message):
    # NSFW filter
    await bot.process_commands(message)

bot.run(token, bot=True, reconnect=True)