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
bot.load_extension('image')
banned_words = auth.banned_words

@bot.event
async def on_ready():
    try:
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        await bot.change_presence(activity=discord.Activity(name="!help to see what\'s nobu", type=discord.ActivityType.playing))

    except Exception as e:
        print(e)

@bot.event
async def on_command(ctx):
	print("{} used \"{}\" in #{} of {}".format(ctx.message.author, ctx.message.content, ctx.message.channel, ctx.message.guild))

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
		await ctx.send("This command requires an input. Use !help to learn more.")

#checks for banned words in my personal server 
@bot.event
async def on_message(message):
    # NSFW filter
    if message.guild.id == auth.koquamserver and message.author.bot is False:
    	for word in banned_words:
    		if word in message.content.lower():
    			await message.channel.send('\"{}\" is a banned word. Repeated use is not recommended.'.format(word))
    			#await message.author.kick()
    			print('Kicking {} for toxic behavior'.format(message.author.name))
    await bot.process_commands(message)

bot.run(token, bot=True, reconnect=True)