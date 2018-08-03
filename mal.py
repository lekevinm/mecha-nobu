import discord, auth
import requests, json
from discord.ext import commands

class AnimeCommands:
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.query = '''
            query ($id: Int, $page: Int, $perPage: Int, $search: String) {
                AnimeSearch: Page (page: $page, perPage: $perPage) {
                    pageInfo {
                        total
                        currentPage
                        lastPage
                        hasNextPage
                        perPage
                    }
                    media (id: $id, search: $search, type: ANIME) {
                        id
                        idMal
                        title {
                            romaji
                        }
                    }
                }
                MangaSearch: Page (page: $page, perPage: $perPage) {
                    pageInfo {
                        total
                        currentPage
                        lastPage
                        hasNextPage
                        perPage
                    }
                    media (id: $id, search: $search, type: MANGA) {
                        id
                        idMal
                        title {
                            romaji
                        }
                    }
                }
            }
            '''
        self.variables = {
            'search': '',
            'perPage': 1
        }
        self.url = 'https://graphql.anilist.co'

    #command that retrieves first anime result from Anilist and redirects to MyAnimeList
    @commands.command()
    async def anime(self, ctx, *, query):
        self.variables['search'] = query
        self.response = requests.post(self.url, json={'query': self.query, 'variables': self.variables})

        anime_dict = json.loads(self.response.text)

        for anime in anime_dict['data']['AnimeSearch']['media']:
            malURL = 'http://myanimelist.net/anime/' + str(anime['idMal'])
            await ctx.send(malURL)
    
    #command that retrieves first manga result from Anilist and redirects to MyAnimeList
    @commands.command()
    async def manga(self, ctx, *, query):
        self.variables['search'] = query
        self.response = requests.post(self.url, json={'query': self.query, 'variables': self.variables})

        manga_dict = json.loads(self.response.text)

        for manga in manga_dict['data']['MangaSearch']['media']:
            malURL = 'http://myanimelist.net/manga/' + str(manga['idMal'])
            await ctx.send(malURL)

def setup(bot):
    bot.add_cog(AnimeCommands(bot))