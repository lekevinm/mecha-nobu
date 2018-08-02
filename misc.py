import discord, auth
from discord.ext import commands
from datetime import date
import asyncio

smash = date(2018, 12, 7)
ax = date(2019, 7, 4)

class MiscCommands:
	def __init__(self, bot: commands.Bot):
		self.bot = bot
		self.bot.remove_command('help')

	#debugging tool to clear up message clutter
	@commands.command()
	@commands.is_owner()
	async def delete(self, ctx, amount: int):
		await ctx.message.channel.purge(limit=amount)

	@commands.command()
	async def joined(self, ctx):
		await ctx.send(f'{ctx.message.author.display_name} joined on {ctx.message.author.joined_at}')

	@commands.command()
	async def hello(self, user : discord.Member):
		await ctx.send("Hello " + user.mention)

	#information command
	@commands.command()
	async def help(self, ctx):
		embed = discord.Embed(title="Mecha Nobu mk III", description="", color=0xeee657)
		embed.add_field(name="YouTube", value="!play !queue !skip !pause !resume !stop !volume", inline=False)
		embed.add_field(name="MyAnimeList", value="!anime !manga", inline=False)
		embed.add_field(name="Game Stats", value="!r6 !fn", inline=False)
		embed.add_field(name="Imageboards", value="!imagehelp", inline=False)
		embed.add_field(name="Miscellaneous", value="!poll !timer !whenissmash !whenisax !todo", inline=False)
		await ctx.send(embed=embed)

	#planned features for mecha nobu
	@commands.command()
	async def todo(self, ctx):
		embed = discord.Embed(title="Things Planned for Mecha Nobu", description="", color=0xeee657)
		embed.add_field(name="YouTube", value="Looking for suggestions", inline=False)
		embed.add_field(name="MyAnimeList", value="Looking for suggestions", inline=False)
		embed.add_field(name="Game Stats", value="Looking for suggestions", inline=False)
		embed.add_field(name="Imageboards", value="Add image boards and developer curated images", inline=False)
		embed.add_field(name="Miscellaneous", value="NSFW filter (temp bans for words like Civ and Overwatch)", inline=False)
		await ctx.send(embed=embed)

	#bot info
	@commands.command()
	async def info(self, ctx):
		embed = discord.Embed(title="Mecha Nobu mk III", description="", color=0xeee657)
		embed.add_field(name="Author", value="RacingMiku14")
		embed.add_field(name="Server count", value=f"{len(self.bot.guilds)}")
		embed.add_field(name="Invite", value="[Invite link](https://discordapp.com/oauth2/authorize?client_id=470992323057287188&scope=bot)")
		await ctx.send(embed=embed)

	#days till smash ultimate
	@commands.command()
	async def whenissmash(self, ctx):
		await ctx.send("{} days left until Smash.".format((smash - date.today()).days))

	#days till anime expo 2019
	@commands.command()
	async def whenisax(self, ctx):
		await ctx.send("{} days left until Anime Expo.".format((ax - date.today()).days))

	@commands.command()
	async def nobu(self, ctx):
		await ctx.send(file=discord.File('nobu.gif'))

	@commands.command()
	async def rem(self, ctx):
		await ctx.send(file=discord.File('rem.gif'))

	#poll feature (ex: !poll "Hangout tonight?" yes no)
	@commands.command()
	async def poll(self, ctx, question, *options: str):
 		if len(options) <= 1:
 			await ctx.send('Nobu needs more than one option to create the poll.')
 			return
 		if len(options) > 10:
 			await ctx.send('Nobu cannot make a poll with more than ten options!')
 			return
 		if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
 			if ctx.message.guild.id == auth.koquamserver:
 				reactions = ['<:maidFive1:361559302189613056>', '<:maidFive2:361559310452654081>']
 			elif ctx.message.guild.id == auth.privateserver:
 				reactions = ['<:yes:454003160843812864>', '<:no:454003146864197635>']
 			else:
 				reactions = ['👍', '👎']
 		else:
 			reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

 		description = []
 		for x, option in enumerate(options):
 			description += '\n {} {}'.format(reactions[x], option)
 		embed = discord.Embed(title=question, description=''.join(description))
 		react_message = await ctx.send(embed=embed)
 		for reaction in reactions[:len(options)]:
 			if reaction.startswith('<'):
 				reaction = reaction[1:-1]
 				await react_message.add_reaction(reaction)
 			else:
 				await react_message.add_reaction(reaction)

 	#timer in minutes
	@commands.command()
	async def timer(self, ctx, minutes: int):
		await ctx.send('Setting timer for {} minute(s).'.format(minutes))
		await asyncio.sleep(minutes * 60)
		await ctx.send('Timer is done ' + ctx.message.author.mention + '.')

def setup(bot):
    bot.add_cog(MiscCommands(bot))