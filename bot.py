import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio
from asyncio import sleep
#import utils.json
#from utils.document import document



load_dotenv()

client = commands.Bot(command_prefix="-")



cogs = ["cogs.automod","cogs.cmds", "cogs.bdev", "cogs.commands", "cogs.utils", "cogs.moderation"] ##add more cogs if needed 


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f"{len(client.guilds)} servers || ALPHA BOT"))
  print("Bot connected")

for cog in cogs:
  try:
    client.load_extension(cog)
  except Exception as e:
    print(f'Could not laod cog {cog}: {str(e)}')    

@client.command()
async def load(ctx, cogname = None):
  if cogname is None:
    await ctx.send("Please Enter a cog name")
    return
  else:
    try:
      client.unload_extension(cog)
    except Exception as e:
      print(f"Could not unlaod cog {cog}: {str(e)}")
      await ctx.send(f"Could not load cog {cog}")
    
    

@client.command()
async def unload(ctx, cogname = None):
  if cogname is None:
    await ctx.send("Please Enter a cog name")
    return
  else:
    try:
      client.unload_extension(cog)
      await ctx.send(f"unloaded {cog} succesfully")
    except Exception as e:
      print(f"Could not unlaod cog {cog}: {str(e)}")
      await ctx.send(f"Could not unload cog {cog}")



client.run(os.getenv("DISCORD_TOKEN"))



