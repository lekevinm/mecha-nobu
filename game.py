import discord, asyncio, requests
from discord.ext import commands
import auth
import r6sapi
import random

class GameCommands:

	def __init__(self, bot: commands.Bot):
		self.bot = bot

	# simple dice roll
	# for DnD uses, may expand functionality
	@commands.command()
	async def d(self, ctx, number: int):
		roll = random.randint(1, number)
		await ctx.send(roll)

	#uses TRN Fortnite Tracker API to pull player data
	#planning to allow more options with this command but for now shows squad data
	@commands.command()
	async def fn(self, ctx, username):
 		r = requests.get('https://api.fortnitetracker.com/v1/profile/pc/{}'.format(username),headers={'TRN-Api-Key': auth.fntracker})
 		fnstats = r.json()
 		fnstats_array = {'p9', 'curr_p9'}
 		top1 = []
 		score = []
 		kd = []
 		winRatio = []
 		kpg = []
 		scorePerMatch = []

 		for entry in fnstats_array:
 			top1.append(fnstats['stats'][entry]['top1']['value'])
 			score.append(fnstats['stats'][entry]['score']['value'])
 			kd.append(fnstats['stats'][entry]['kd']['value'])
 			winRatio.append(fnstats['stats'][entry]['winRatio']['value'])
 			kpg.append(fnstats['stats'][entry]['kpg']['value'])
 			scorePerMatch.append(fnstats['stats'][entry]['scorePerMatch']['value'])

 		embed = discord.Embed(title=username, description="Squad Stats", color=0xeee657)
 		embed.add_field(name="Player Profile", value="https://fortnitetracker.com/profile/pc/{}".format(username), inline=False)
 		embed.add_field(name="1st Place Finishes", value="Current: {}, Lifetime: {}".format(top1[0], top1[1]), inline=False)
 		embed.add_field(name="Total Score", value="Current: {}, Lifetime: {}".format(score[0], score[1]), inline=False)
 		embed.add_field(name="K/D", value="Current: {}, Lifetime: {}".format(kd[0], kd[1]), inline=False)
 		embed.add_field(name="Win Ratio", value="Current: {}, Lifetime: {}".format(winRatio[0], winRatio[1]), inline=False)
 		embed.add_field(name="Kills per Game", value="Current: {}, Lifetime: {}".format(kpg[0], kpg[1]), inline=False)
 		embed.add_field(name="Score per Match", value="Current: {}, Lifetime: {}".format(scorePerMatch[0], scorePerMatch[1]), inline=False)
 		await ctx.send(embed=embed)

 	#uses r6sapi to pull player data
 	#also planning to allow more options with this command
	@commands.command()
	async def r6(self, ctx, username):
 		r6auth = r6sapi.Auth(auth.r6username, auth.r6password)
 		try:
 			player = await r6auth.get_player(username, r6sapi.Platforms.UPLAY)
 		except:
 			await ctx.send("Player was not found.")
 			return
 		rank = await player.load_rank("ncsa")
 		await player.load_level()
 		await player.load_general()
 		await player.load_queues()
 		kdr = (player.kills) / (player.deaths)
 		kdar = (player.kills + player.kill_assists) / (player.deaths)
 		wlr = player.matches_won / player.matches_lost
 		swlr = rank.wins / rank.losses
 
 		embed = discord.Embed(title=username, description="Level {}".format(player.level), color=0xeee657)
 		embed.add_field(name="Player Profile", value=player.url, inline=False)
 		embed.add_field(name="Rank", value = "{}".format(rank.rank), inline=False)
 		embed.add_field(name="MMR", value = "Current: {} Max: {}".format(format(rank.mmr, '.2f'), format(rank.max_mmr, '.2f')), inline=False)
 		embed.add_field(name="Stats", value = "Kills: {} Assists: {} Deaths: {}".format(player.kills, player.kill_assists, player.deaths), inline=False)
 		embed.add_field(name="Lifetime Matches", value = "Won: {} Lost: {} WL: {}".format(player.matches_won, player.matches_lost, format(wlr, '.2f')), inline=False)
 		embed.add_field(name="Seasonal Matches", value = "Won: {} Lost: {} WL: {}".format(rank.wins, rank.losses, format(swlr, '.2f')), inline=False)
 		embed.add_field(name="KD Ratio", value = "KD: {} KDA: {}".format(format(kdr, '.2f'), format(kdar, '.2f')), inline=False)
 		await ctx.send(embed=embed)

 	# basic stat retrieval using bo4tracker.com
 	# may add more options depending on demand
	@commands.command()
	async def bo4(self, ctx, username):
		username = username.replace('#', '%23', 1)
		
		r = requests.get('https://cod-api.theapinetwork.com/api/validate/bo4/{}/bnet'.format(username))
		try:
			bo4auth = r.json()
		except ValueError:
			await ctx.send("User not found in database.")
			return

		if bo4auth['success'] is False:
			await ctx.send("User not found in database.")
			return
		else:

 			r2 = requests.get('https://cod-api.theapinetwork.com/api/stats/bo4/{}/bnet'.format(username))
 			bo4stats = r2.json()

 			ign = bo4stats['user']['username']
 			level = bo4stats['stats']['level']
 			wins = bo4stats['stats']['wins']
 			losses = bo4stats['stats']['losses']
 			kills = bo4stats['stats']['kills']
 			ekia = bo4stats['stats']['ekia']
 			deaths = bo4stats['stats']['deaths']
 			wlr = wins / losses
 			kdar = ekia / deaths
 			kdr = kills / deaths

 			embed = discord.Embed(title=ign, description="Level {}".format(level), color=0xeee657)
 			embed.add_field(name="Stats", value = "Kills: {} EKIA: {} Deaths: {}".format(kills, ekia, deaths), inline=False)
 			embed.add_field(name="Win/Loss Ratio", value = "Won: {} Lost: {} WL: {}".format(wins, losses, format(wlr, '.2f')), inline=False)
 			embed.add_field(name="KD Ratio", value = "KD: {} KDA: {}".format(format(kdr, '.2f'), format(kdar, '.2f')), inline=False)
 			await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(GameCommands(bot))