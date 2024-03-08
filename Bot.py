from Jokes import read_text_file
import discord
from discord.ext import commands 
from DatabaseConfig import BOT_TOKEN

intents = discord.Intents.all()
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    filenames = ["Jokes/300RandomJokes.txt", "Jokes/DarkHumorJokes.txt"]
    
    for filename in filenames:
        read_text_file(filename)


bot.run(BOT_TOKEN)