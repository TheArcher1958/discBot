import discord
from discord.ext import commands
import skywarsStats



Client = discord.Client() #Initialise Client
client = commands.Bot(command_prefix = "-") #Initialise client bot


@client.event
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called
# when the bot connects to the server

def getOnlineStats():
    pass
    #get stats
    #post stats

@client.event
async def on_message(message):
    if "-stats " in message.content[0:7] and str(message.author) != 'ArchersBot#2435':

        try:
            statsList = skywarsStats.getStats(message.content[7:])
            await message.channel.send("```Skywars Stats for " + message.content[7:] + ":" + "\n"
                                       + "Kills: " + statsList[0] + "\n"
                                       + "Deaths: " + statsList[1] + "\n"
                                       + "Wins: " + statsList[2] + "\n"
                                       + "Assists: " + statsList[3]+"```")
        except ValueError:
            await message.channel.send("```Could not find stats for player \"" + message.content[7:] + "\"```")

    elif "-online " in message.content[0:8] and str(message.author) != 'ArchersBot#2435':
        try:
            onlineStatusList = skywarsStats.status(message.content[8:])
            await message.channel.send("```Player " + message.content[8:] + " is " + onlineStatusList[1] + "\n"
                                       + message.content[8:] + " last logged in on " + onlineStatusList[0] + "```")
        except ValueError:
            await message.channel.send("```Could not find online status for player \"" + message.content[8:] + "\"```")
    elif "-sQuery " in message.content[0:8] and str(message.author) != 'ArchersBot#2435':
        try:
            onlineStatusList = skywarsStats.serverCount(message.content[8:])
            await message.channel.send("```Server " + message.content[8:] + " has " + onlineStatusList + " players online.```")
        except ValueError:
            await message.channel.send("```Could not find player count for server \"" + message.content[8:] + "\"```")




client.run(open("token.txt").read())