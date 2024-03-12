from Jokes import read_text_file, read_jokes
import discord
from discord.ext import commands 
from DatabaseConfig import BOT_TOKEN

intents = discord.Intents.all()
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name = "Joke", help = "Tells a random joke")
async def tell_joke(ctx):
    joke = read_jokes('alljokes')
    await ctx.send(joke)

@bot.event
async def on_ready():
    filenames = ["Jokes/300RandomJokes.txt", "Jokes/DarkHumorJokes.txt"]
    
    for filename in filenames:
        read_text_file(filename)


bot.run(BOT_TOKEN)