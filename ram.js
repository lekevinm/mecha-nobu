const Discord = require('discord.js');
const client = new Discord.Client();

var config = require('./config.json');
client.login(config.token);

var dt = new Date();
var utcDate = dt.toLocaleTimeString();

var inVoice = false;
var musicQueue = [];
const ytdl = require('ytdl-core');
const streamOptions = { seek: 0, volume: 1 };
//var dispatcher = null;


// The token of your bot - https://discordapp.com/developers/applications/me
//const token = 'MzI2NjIxOTQxODQ0OTM0NjU3.DCpnMg.xu9E0Ot63CFP3uDjiy5WlmvHjsY';

/*
client.on('error', (e) => console.error(e));
client.on('warn', (e) => console.warn(e));
client.on('debug', (e) => console.info(e));
*/

/*
client.on('guildMemberAdd', (member) => {
  console.log(`New User "${member.user.username}" has joined "${member.guild.name}"` );
  member.guild.defaultChannel.send(`"${member.user.username}" has joined this server`);
});
*/

client.on('message', (message) => {
  // Set the prefix
  let prefix = config.prefix;
  const args = message.content.split(/\s+/g);

  var command = args[0].toLowerCase();
  var randomNumber = 0;

  dt = new Date();
  utcDate = dt.toLocaleTimeString();
  // Exit and stop if it's not there
 //if (!message.content.startsWith(prefix) || message.author.bot) return;

//if(message.author.id == "132473496793120768") {
    //message.channel.send("This user does not have power over Ram.");
//}
 switch (command) {
 	case prefix + 'rem':
 		/*console.log(message.author.username + " !rem");
 		randomNumber = Math.floor(Math.random()*2);
 		if (randomNumber == 0){
 			message.reply('<:maidJudge:334926137908264960>'); // custom emoji for the server this bot is used on
 		}
 		else if (randomNumber == 1){
 			message.reply('!rem does not work. Neither does !ram.');
 		}*/
 		randomNumber = Math.floor(Math.random()*253);
 		img_string = "/Users/Kevin Le/Pictures/rem/rem (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !rem, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
 	case prefix + 'emilia':
 		randomNumber = Math.floor(Math.random()*32);
 		img_string = "/Users/Kevin Le/Pictures/emilia/emilia (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !emilia, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
  	case prefix + 'racingmiku':
 		randomNumber = Math.floor(Math.random()*36);
 		img_string = "/Users/Kevin Le/Pictures/racingmiku/racingmiku (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !racingmiku, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
  	case prefix + 'biribiri':
 		randomNumber = Math.floor(Math.random()*45);
 		img_string = "/Users/Kevin Le/Pictures/biribiri/biribiri (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !biribiri, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
  	case prefix + 'fate':
 		randomNumber = Math.floor(Math.random()*88);
 		img_string = "/Users/Kevin Le/Pictures/fate/fate (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !fate, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
  	case prefix + 'idol':
 		randomNumber = Math.floor(Math.random()*125);
 		img_string = "/Users/Kevin Le/Pictures/idol/idol (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !idol, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
  	case prefix + 'misc':
 		randomNumber = Math.floor(Math.random()*355);
 		img_string = "/Users/Kevin Le/Pictures/misc/misc (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !misc, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
  	case prefix + 'overwatch':
 		randomNumber = Math.floor(Math.random()*59);
 		img_string = "/Users/Kevin Le/Pictures/overwatch/overwatch (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !overwatch, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
  	case prefix + 'miku':
 		randomNumber = Math.floor(Math.random()*48);
 		img_string = "/Users/Kevin Le/Pictures/miku/miku (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !miku, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
  	case prefix + 'yourname':
 		randomNumber = Math.floor(Math.random()*29);
 		img_string = "/Users/Kevin Le/Pictures/yourname/yourname (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !yourname, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
  	case prefix + 'madoka':
 		randomNumber = Math.floor(Math.random()*33);
 		img_string = "/Users/Kevin Le/Pictures/madoka/madoka (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !madoka, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
  	case prefix + 'sumo':
 		randomNumber = Math.floor(Math.random()*31);
 		img_string = "/Users/Kevin Le/Pictures/sumo/sumo (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !sumo, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
  	case prefix + 'makoto':
 		randomNumber = Math.floor(Math.random()*117);
 		img_string = "/Users/Kevin Le/Pictures/makoto/makoto (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !makoto, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
  	case prefix + 'anya':
 		randomNumber = Math.floor(Math.random()*78);
 		img_string = "/Users/Kevin Le/Pictures/anya/anya (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !anya, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
 	case prefix + 'persona':
 		randomNumber = Math.floor(Math.random()*201);
 		img_string = "/Users/Kevin Le/Pictures/persona/persona (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !persona, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
 	case prefix + 'pripri':
 		randomNumber = Math.floor(Math.random()*32);
 		img_string = "/Users/Kevin Le/Pictures/pripri/pripri (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !pripri, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
 	case prefix + 'scathach':
 		randomNumber = Math.floor(Math.random()*38);
 		img_string = "/Users/Kevin Le/Pictures/scathach/scathach (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !scathach, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
 	case prefix + 'mashu':
 		randomNumber = Math.floor(Math.random()*52);
 		img_string = "/Users/Kevin Le/Pictures/mashu/mashu (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !mashu, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
 	case prefix + 'nero':
 		randomNumber = Math.floor(Math.random()*20);
 		img_string = "/Users/Kevin Le/Pictures/nero/nero (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !nero, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
 	case prefix + 'okita':
 		randomNumber = Math.floor(Math.random()*65);
 		img_string = "/Users/Kevin Le/Pictures/okita/okita (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !okita, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
 	case prefix + 'nobu':
 		randomNumber = Math.floor(Math.random()*61);
 		img_string = "/Users/Kevin Le/Pictures/nobu/nobu (" + randomNumber + ").jpg";
 		console.log(utcDate + " - " + message.author.username + " !nobu, " + img_string);
 		message.channel.send({
 			file: img_string
 		});
 		break;
 	case prefix + 'help':
 		console.log(utcDate + " - " + message.author.username + " !help");
 		/*if (randomNumber <= 0){
 			message.reply('I do not require help. <:maidNo:334926151229243393>');
 		}
 		else if (randomNumber > 1){
 			message.reply('I think you can figure it out on your own. Ram believes in you. <:ahegaoBestGirl:328075922932629506>');
 		}*/
 		message.reply('\n !help - Review list of commands \n !timer - Set a timer using minutes \n !8ball - Ask a yes/no question \n !delete - Deletes user-given number of messages (developer tool) \n !voice - Joins/leaves current voice channel \n !play - Plays next song in queue or given link \n !queue - Adds song to queue (LIFO order) \n \n Try maid-bot\'s new image commands! \n !rem  !emilia  !racingmiku  !biribiri \n !fate  !idol  !misc  !overwatch \n !miku  !yourname  !madoka  !sumo \n !persona  !makoto  !anya');
 		break;
 	case prefix + 'compliment':
 		randomNumber = Math.floor(Math.random()*2);
 		console.log(utcDate + " - " + message.author.username + " !compliment" + randomNumber);
 		if (randomNumber == 0){
 			message.reply('Please stop doing that.');
 		}
 		else if (randomNumber == 1){
 			message.reply('Compliments will only get you so far in life.');
 		}
 		break;
 	case prefix + 'timer':
 		console.log(utcDate + " - " + message.author.username + " !timer");
 		if (args[1] == null){
 		message.reply('You must use !timer with a set number of minutes.');
 		}
 		else{
 		try{
 		var userid = message.author.id;
 		var timer = parseInt(args[1]);
 		} catch (e) {
 			message.channel.send('You must input an integer.');
 			console.log(message.author.username + " Error on !timer");
 		}
  		setTimeout(timerNotify, timer * 60000);
  		}
  		function timerNotify() {
    		message.channel.send('<@' + userid + '> Timer is finished.');
		}
 		break;
 	case prefix + '8ball':
 		console.log(utcDate + " - " + message.author.username + " !8ball");
 		var randomNumber = Math.floor(Math.random()*20);
 		switch (randomNumber) {
 			case 0:
 			message.reply('It is certain.');
 			break;
 			case 1:
 			message.reply('It is decidely so.');
 			break;
 			case 2:
 			message.reply('Without a doubt.');
 			break;
 			case 3:
 			message.reply('Yes definitely.');
 			break;
 			case 4:
 			message.reply('You may rely on it.');
 			break;
 			case 5:
 			message.reply('As I see it, yes.');
 			break;
 			case 6:
 			message.reply('Most likely.');
 			break;
 			case 7:
 			message.reply('Outlook good.');
 			break;
 			case 8:
 			message.reply('Yes.');
 			break;
 			case 9:
 			message.reply('Signs point to yes.');
 			break;
 			case 10:
 			message.reply('Reply hazy, try again.');
 			break;
 			case 11:
 			message.reply('Ask again later.');
 			break;
 			case 12:
 			message.reply('Better not tell you now.');
 			break;
 			case 13:
 			message.reply('Cannot predict now.');
 			break;
 			case 14:
 			message.reply('Concentrate and ask again.');
 			break;
 			case 15:
 			message.reply('Don\'t count on it.');
 			break;
 			case 16:
 			message.reply('My reply is no.');
 			break;
 			case 17:
 			message.reply('My sources say no.');
 			break;
 			case 18:
 			message.reply('Outlook not so good.');
 			break;
 			case 19:
 			message.reply('Very doubtful.');
 		}
 		break;
 	/*case prefix + 'id':
 		if (args[1] == null){
 		console.log(message.author.username + " !id");
 		message.reply(message.author.id);
 	}
 		else{
 			username = args[1];
 		}
 		break;*/
 	case prefix + 'delete':
 		if (args[1] == null){
 		console.log(utcDate + " - " + message.author.username + " !delete");
 		var messagecount = 1;
  		message.channel.fetchMessages({limit: messagecount}).then(messages => message.channel.bulkDelete(messages));
 		}
 		else{
 		console.log(utcDate + " - " + message.author.username + " !delete" + args[1]);
 		try{
 		var messagecount = parseInt(args[1]);
 		} catch (e) {
 			message.channel.send('You must input an integer.');
 			console.log(message.author.username + " Error on !delete");
 		}
  		message.channel.fetchMessages({limit: messagecount}).then(messages => message.channel.bulkDelete(messages));
  		}
 		break;
 	case prefix + 'voice':
 	//var dt = new Date();
	//var utcDate = dt.toUTCString();
 	console.log(utcDate + " - " + message.author.username + " !voice");
  		if (message.member.voiceChannel) {
  			if (!inVoice) {
  			inVoice = true; 
     		message.member.voiceChannel.join()
        	.then(connection => { // Connection is an instance of VoiceConnection
          		message.reply('I have successfully connected to the channel!');
        	})
        	.catch(console.log);
        }
        	else {
        		message.member.voiceChannel.leave();
        	}
    	} else {
      		message.reply('You need to join a voice channel first!');
    	}
 		break;
 	case prefix + 'play':
 		if (inVoice){
 			if (args[1] == null){ // check if !play contains a link argument
 			console.log(utcDate + " - " + message.author.username + " !play");
 				if (musicQueue.length != 0){
 					var link = musicQueue.pop(); 
   					try{
   						var stream = ytdl(link, { filter : 'audioonly' });
   						var dispatcher = message.guild.voiceConnection.playStream(stream, streamOptions);
   						dispatcher.on('end', () => {
   						console.log("VoiceDispatcher finished current song.");
   						console.log("Songs left in queue: " + musicQueue.length);
						if (musicQueue.length != 0){
							var link = musicQueue.pop();
							console.log("Next song in track: " + link);
   							try{
   								stream = ytdl(link, { filter : 'audioonly' });
   							} catch (e) {
   						console.log(e);
   					message.channel.send('Invalid link, can\'t play stream.');
   				}
   				dispatcher = message.guild.voiceConnection.playStream(stream, streamOptions);
				}
			});
   					} catch (e) {
   						message.channel.send('Invalid link, can\'t play stream.');
   						console.log(message.author.username + " Error on !play");
   					}
   				}
   			}
   			else{
   			console.log(utcDate + " - " + message.author.username + " !play " + args[1]);
   			try{
   			var stream = ytdl(args[1], { filter : 'audioonly' });
   			var dispatcher = message.guild.voiceConnection.playStream(stream, streamOptions);
   			dispatcher.on('end', () => {
   				console.log("VoiceDispatcher finished current song.");
   				console.log("Songs left in queue: " + musicQueue.length);
				if (musicQueue.length != 0){
					var link = musicQueue.pop();
					console.log("Next song in track: " + link);
   					try{
   						stream = ytdl(link, { filter : 'audioonly' });
   					} catch (e) {
   					console.log(e);
   					message.channel.send('Invalid link, can\'t play stream.');
   				}
   				dispatcher = message.guild.voiceConnection.playStream(stream, streamOptions);
				}
			});
   			} catch (e) {
   			message.channel.send('Invalid link, can\'t play stream.');
   			console.log(message.author.username + " Error on !play");
   			}
  			}
  		}
   		else{
   			message.reply('Please add me to your voice channel using !voice first.');
   		}
   		break;
   	case prefix + 'queue':
   		if (args[1] == null){
   			message.reply('You didn\'t link anything to queue.');
   		}
   		else{
   		musicQueue.push(args[1]);
   		console.log(utcDate + " - " + message.author.username + " !queue " + args[1]);
   	}
   		break;
   	case prefix + 'skip':
   		console.log(utcDate + " - " + message.author.username + " !skip");
   		message.reply('My creator is too lazy to copy/paste, just use !play to skip.');
 }
});

client.on('ready', () => {
	console.log(utcDate + " - " + "Maid bot online.");
	client.user.setGame('!help for new commands');
});

client.on('voiceStateUpdate', (oldMember, newMember) => {
  dt = new Date();
  utcDate = dt.toLocaleTimeString();

	if (newMember.voiceChannel != null && newMember.id == 326621941844934657  && !newMember.selfMute && !newMember.selfDeaf && !newMember.serverMute && !newMember.serverDeaf){
		console.log(utcDate + " - " + "Ram has joined the voice channel.");
		//console.log(message.author.id + " !skip");
		inVoice = true;
	}
	else if (newMember.voiceChannel != null && newMember.id == 341494583739285507 && !newMember.selfMute && !newMember.selfDeaf && !newMember.serverMute && !newMember.serverDeaf){
		console.log(utcDate + " - " + "Niko voice state update.");

		if (!inVoice) {
  			inVoice = true; 
     		newMember.voiceChannel.join()
        	.then(connection => { // Connection is an instance of VoiceConnection
          		console.log("Ram has joined the voice channel.");
        	})
        	.catch(console.log);
        }

		console.log("Easter egg -!play www.youtube.com/watch?v=V1dzNzifPdY");
   			try{
   			var stream = ytdl('www.youtube.com/watch?v=V1dzNzifPdY', { filter : 'audioonly' });
   			var dispatcher = newMember.guild.voiceConnection.playStream(stream, streamOptions);
   			dispatcher.on('end', () => {
   				console.log("VoiceDispatcher finished current song.");
   				console.log("Songs left in queue: " + musicQueue.length);
				if (musicQueue.length != 0){
					var link = musicQueue.pop();
					console.log("Next song in track: " + link);
   					try{
   						stream = ytdl(link, { filter : 'audioonly' });
   					} catch (e) {
   					console.log(e);
   					//message.channel.send('Invalid link, can\'t play stream.');
   				}
   				dispatcher = newMember.guild.voiceConnection.playStream(stream, streamOptions);
				}
			});
   			} catch (e) {
   			//message.channel.send('Invalid link, can\'t play stream.');
   			console.log(e);
   			}
	}
	else if (oldMember.id == 326621941844934657 && newMember == null){
		console.log(utcDate + " - " + "Ram has left the voice channel.");
		inVoice = false;
	}
	/*else if (newMember.voiceChannel == null){
		console.log(utcDate + " - " + oldMember.user.username + " has left the voice channel.");
	}
	else if (newMember.voiceChannel != null && !newMember.selfMute && !newMember.selfDeaf && !newMember.serverMute && !newMember.serverDeaf){
		console.log(utcDate + " - " + newMember.user.username + " has joined the voice channel or unmuted.");
	}*/
});