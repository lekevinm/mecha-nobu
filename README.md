# Mecha Nobu mk III
Discord bot intended for personal server use, but can be added to other servers [here.](https://discordapp.com/oauth2/authorize?client_id=470992323057287188&scope=bot) This is a very early alpha version of Mecha Nobu so expect only basic functionality and some bugs. 

Currently hosting Mecha Nobu on my laptop so uptime is not guaranteed, may look into a Rasberry Pi or a cloud hosting solution in the future.

Written in Python and uses the discord.py API (rewritten version).

Can also be cloned and run on a local machine, but will require additional installs for full functionality.

Uses R6S API and TRN Fortnite Tracker for game stats, Anilist API to retrieve anime/manga links, and youtube_dl to stream YouTube audio.

Still adding and refining features, no official documentation until finished.

# Useful Commands

**YouTube playback:** !play *url or query* !volume *int* !skip !pause !resume !queue !stop

**Game stats:** !r6 *player* !fn *player*

**MyAnimeList:** !anime *query* !manga *query*

**Miscellaneous:** !poll *question option1 option2 etc* !timer *minutes* !help
