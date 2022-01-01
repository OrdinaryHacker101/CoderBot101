import discord
from discord.ext import commands

import pafy
#import tensorflow as tf

client = discord.Client()
client = commands.Bot(command_prefix='!^!')

token = "NoTokenForYouYee"

@client.event
async def on_message(message):
    if message.content.find("Hello") != -1:
        await message.channel.send("Hi")
    elif message.content == "!users":
        await message.channel.send(f"""# of Members {server_ID.member_count}""")

    await client.process_commands(message)    

@client.command(name="join")
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command(name="leave")
async def leave(ctx):
    await ctx.voice_client.disconnect()
        
if __name__ == "__main__" :
    client.run(token)    
