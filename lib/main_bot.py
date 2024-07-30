# Firstly we must connect the Bot to the Server using the Discord API
# Make sure to change DISCORD_TOKEN and DISCORD_GUILD in .env 

import os

import discord
from dotenv import load_dotenv
from discord.ext import commands



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot_name = "Apollo"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)


@bot.event

async def on_ready():

    guild_count = 0

    for guild in bot.guilds:

        print(f"- {guild.id} (name: {guild.name})")

        guild_count = guild_count + 1

    print(bot_name + " is in " + str(guild_count) + " guilds.")





# Testing connection
@bot.command(name='test1', aliases=['t1'])

async def test1(ctx):
    
    await ctx.channel.send("hey dirtbag")



bot.run(TOKEN)
