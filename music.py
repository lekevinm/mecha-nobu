import discord, asyncio
from discord.ext import commands
from discord.voice_client import VoiceClient
import queue, youtube_dl, subprocess

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' 
}

ffmpeg_options = {
    'before_options': '-nostdin',
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class MusicCommands:
    def __init__(self, bot):
        self.bot = bot
        self.server_queues = {}

    def getQueue(self, ctx):
        queue = self.server_queues.get(ctx.guild.id)
        if queue is None:
            queue = MusicQueue(self.bot, ctx.voice_client, ctx.channel)
            self.server_queues[ctx.guild.id] = queue
        else:
            if not queue.voice_client.is_connected():
                queue.voice_client = ctx.voice_client
        return queue

    #join voice channel
    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        await channel.connect()

    #play youtube url or query
    @commands.command()
    async def play(self, ctx, *, url):
        queue = self.getQueue(ctx)
        player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
        await queue.song_queue.put(player)
        queue.song_titles.append(str(player.title))

    #adjust volume
    @commands.command()
    async def volume(self, ctx, volume: int):
        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")
        ctx.voice_client.source.volume = volume / 100
        await ctx.send("Changed volume to {}%".format(volume))

    #disconnect bot from voice channel
    @commands.command()
    async def stop(self, ctx):
        await ctx.voice_client.disconnect()
        try:
            self.clear_data(ctx.guild.id)
            del self.server_queues[ctx.guild.id]
        except:
            pass

    #pause current song
    @commands.command()
    async def pause(self, ctx):
        self.getQueue(ctx).voice_client.pause()
        await ctx.send("Song is paused.")

    #resume current song
    @commands.command()
    async def resume(self, ctx):
        self.getQueue(ctx).voice_client.resume()
        await ctx.send("Song resuming.")

    #skip current song
    @commands.command()
    async def skip(self, ctx):
        queue = self.getQueue(ctx)
        if not ctx.voice_client:
            await ctx.send("Nobu not in voice channel.")
            return
        if commands.is_owner():
            queue.voice_client.stop()
            await ctx.send("Song skipped by developer.")
        elif ctx.author == queue.current_song.requested:
            queue.voice_client.stop()
            await ctx.send("Song skipped by requested.")
        else:
            needed = 2
            voice_members = len([member for member in queue.voice_client.channel.members if not member.bot])
            if voice_members <= needed:
                needed = voice_members - 1
            if ctx.author.id not in queue.votes:
                queue.votes.append(ctx.author.id)
            else:
                await ctx.send("Duplicate vote!")
                return
            if len(queue.votes) >= needed:
                queue.voice_client.stop()
                await ctx.send("Song being skipped.")
            else:
                await ctx.send("{} votes to skip. {} needed in total.".format(len.queue.votes, needed))

    #check song queue
    @commands.command()
    async def queue(self, ctx):
        queue = self.getQueue(ctx)
        song_titles = ""
        if queue.current_song:
            if queue.voice_client is not None and not queue.voice_client.is_paused() and not queue.voice_client.is_playing():
                await ctx.send("Nothing is queued!")
                return
            else:
                song_titles = (queue.current_song.title)
        else:
            await ctx.send("Nothing is queued!")
            return
        if len(queue.song_titles) != 0:
            song_titles += "\n{}".format("\n".join(queue.song_titles))
        await ctx.send(song_titles)

    @play.before_invoke
    @volume.before_invoke
    @queue.before_invoke
    @skip.before_invoke
    @resume.before_invoke
    @pause.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You must be connected to a voice channel to use this command.")
                raise commands.CommandError("Author not connected to a voice channel.")

#class that streams songs from YouTube
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

#class that manages and plays songs in queue
class MusicQueue():
    def __init__(self, bot, voice_client, channel):
        self.bot = bot
        self.voice_client = voice_client
        self.channel = channel
        self.play_next = asyncio.Event()
        self.song_titles = []
        self.current_song = None
        self.song_queue = asyncio.Queue()
        self.audio_player = self.bot.loop.create_task(self.playNextSong())
        self.votes = []

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set())

    async def playNextSong(self):
        while True:
            self.play_next.clear()
            self.current_song = await self.song_queue.get()
            print(str(self.current_song.title))
            self.song_titles.remove(str(self.current_song.title))
            self.votes.clear()
            await self.channel.send('Now playing: {}'.format(self.current_song.title))
            self.voice_client.play(self.current_song, after=lambda e: self.play_next.set())
            await self.play_next.wait()

def setup(bot):
    bot.add_cog(MusicCommands(bot))