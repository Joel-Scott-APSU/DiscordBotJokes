from Jokes import read_text_file, read_random_jokes, read_dark_jokes
import discord
from discord.ext import commands 
from DatabaseConfig import BOT_TOKEN
from DatabaseConfig import connect_to_database

db_cursor, db_connection = connect_to_database()

intents = discord.Intents.all()
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name = "Joke", help = "Tells a random joke")
async def tell_random_jokes(ctx):
    joke = read_random_jokes('alljokes')
    await ctx.send(joke)

@bot.command(name = "DarkJoke", help = "Tells a dark humored joke")
async def tell_dark_jokes(ctx):
    joke = read_dark_jokes('darkhumor')
    await ctx.send(joke)

@bot.event
async def on_ready():
    filenames = ["300RandomJokes.txt", "DarkHumorJokes.txt"]
    
    for filename in filenames:
        read_text_file(filename)

@bot.event
async def on_disconnect():
    db_cursor.close()
    db_connection.close()
    
bot.run(BOT_TOKEN)