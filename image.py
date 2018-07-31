import discord, requests, random
from discord.ext import commands

class ImageCommands:
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command()
	async def imagehelp(ctx):
 		"""
 		"""

	@commands.command()
	async def headpat(self, ctx):
		"""Posts a random headpat from headp.at"""
		pats = requests.get("http://headp.at/js/pats.json").json()
		pat = random.choice(pats)
		file = url_to_bytes("http://headp.at/pats/{}".format(pat))
		await ctx.send(file=discord.File(file["content"], file["filename"]))

def setup(bot):
    bot.add_cog(ImageCommands(bot))