import discord, requests, os, random, json
from discord.ext import commands

class ImageCommands:
	def __init__(self, bot: commands.Bot):
		self.bot = bot
		self.dropbox = loadDropbox()

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
	async def image(self, ctx, *args):
		image = args[0]
		if image in self.dropbox:
			if len(args) == 2:
				image_number = int(args[1])
				if (image_number >= 0) and (image_number <= self.dropbox[image]):
					await ctx.send('{}/{}'.format(image_number, self.dropbox[image]), file=discord.File('/Users/guest/Dropbox/{}/{} ({}).jpg'.format(image, image, image_number)))
				else:
					await ctx.send('Image \'{}\' was not found in the folder \'{}\'.'.format(image_number, image))
			else:
				image_number = randomImage(0, self.dropbox[image])
				await ctx.send('{}/{}'.format(image_number, self.dropbox[image]), file=discord.File('/Users/guest/Dropbox/{}/{} ({}).jpg'.format(image, image, image_number)))
		else:
			await ctx.send('\'{}\' is not a valid image command.'.format(image))
def setup(bot):
    bot.add_cog(ImageCommands(bot))

def randomImage(min, max):
	return random.randint(min,max)

def loadDropbox():
	folders = os.listdir("/Users/guest/Dropbox")
	imagelist = {}
	for folder in folders:
		if folder.startswith('.') is False and folder.endswith(('.png', '.jpg')) is False:
			files = os.listdir("/Users/guest/Dropbox/{}".format(folder))
			imagecount = len(files) - 1
			if os.path.isfile("/Users/guest/Dropbox/{}/.DS_Store".format(folder)):
				imagecount -= 1
			imagelist[folder] = imagecount
			#print("{}: {}".format(folder, imagecount))
	return imagelist
