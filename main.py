import discord
from discord.ext import commands
from discord.ui import Button, View

import config 


intents = discord.Intents().all()
client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print('Updating...')
    print("Update successfully")
    print("Bot online")
    
@client.command()
#@commands.has_permissions(administrator=True)
async def Hello(ctx):
    await ctx.message.delete()
    await ctx.send(f'Hello, {ctx.author.name}!')
    
client.run(config.TOKEN)