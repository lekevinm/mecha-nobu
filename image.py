import discord, requests, random, json
from discord.ext import commands

class ImageCommands:
	def __init__(self, bot: commands.Bot):
		self.bot = bot
		dropbox = dict{'fate': 0, 'nobu': 0, 'scathach': 0, 'okita': 0, 'nero': 0, 'mashu': 0, 'anya_fgo': 0, 
		'miku': 0, 'racingmiku': 0, 'idol': 0, 'anya': 0,
		'persona': 0, 'rise': 0, 'makoto': 0,
		'misc': 0, 'rem': 0, 'emilia': 0, 'pripri': 0, 'nier': 0, 'madoka': 0, 'houseki': 0,
		'sumo': 0, 'yourname': 0, 'bbb': 0, 'biribiri': 0, 'overwatch': 0}

	@commands.command()
	async def imagehelp(self, ctx):
		embed = discord.Embed(title="Image Galleries", description="For non-external images use !image name", color=0xeee657)
		embed.add_field(name="Fate", value="!fate !nobu !scathach !okita !nero !mashu !anya_fgo", inline=False)
		embed.add_field(name="Miku & Idols", value="!miku !racingmiku !idol !anya", inline=False)
		embed.add_field(name="Persona", value="!persona !rise !makoto", inline=False)
		embed.add_field(name="Miscellaneous", value="!misc !rem !emilia !pripri !nier !madoka !houseki", inline=False)
		embed.add_field(name="More Miscellaneous", value=" !sumo !yourname !bbb !biribiri !overwatch", inline=False)
		embed.add_field(name="External Websites", value=" !headpat !safebooru !danbooru", inline=False)
		await ctx.send(embed=embed)

	@commands.command()
	async def image(self, ctx, image):
		if image in dropbox:
			image_number = randomImage(0, dropbox[image])
			#store the number of images per folder in a dictionary
			await ctx.send(file=discord.File('/Users/guest/Dropbox/{}/{} ({}).jpg'.format(image, image, image_number)))
		else:
			await ctx.send('\'{}\' is not a valid image command.'.format(image))

	@commands.group()
	async def imagetest(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send('Invalid image command passed...')

	@imagetest.command()
	async def test(self, ctx):
		image_number = randomImage(0,100)
		await ctx.send(file=discord.File('/Users/guest/Dropbox/nobu/nobu ({}).jpg'.format(image_number)))

def setup(bot):
    bot.add_cog(ImageCommands(bot))

def randomImage(min, max):
	return random.randint(min,max)