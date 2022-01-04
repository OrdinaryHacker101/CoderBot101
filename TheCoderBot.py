import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio

from youtube_dl import YoutubeDL

client = discord.Client()
client = commands.Bot(command_prefix='C~ ')

token = "OTIxNTY4MTM1MDUwNTcxODU3.Yb0zNQ.oayDydNkqGFdQURmnFFKHyEKAMI"

joined_voice_channel = False

@client.event
async def on_message(message):
    if message.content.find("Hello") != -1:
        await message.channel.send("Hi")

    await client.process_commands(message)

@client.command(name="join")
async def join(ctx):
    try:
        global joined_voice_channel
        channel = ctx.author.voice.channel
        joined_voice_channel = True
        await channel.connect()
    except:
        await ctx.send("You need to join a voice channel to use this command.")

@client.command(name="play")
async def play(ctx, url):
    if joined_voice_channel == True:
        YDL_SPECS = {"format": "bestaudio", "noplaylist": "True"}
        FFMPEG_OPTIONS = {"before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", "options": "-vn"}
        voice = get(client.voice_clients, guild=ctx.guild)

        if not voice.is_playing():
            with YoutubeDL(YDL_SPECS) as ydl:
                info = ydl.extract_info(url, download=False)
            URL = info["formats"][0]["url"]
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
        else:
            await ctx.send("Already playing song")
    else:
        await ctx.send("You need to join a voice channel to use this command.")

@client.command(name="leave")
async def leave(ctx):
    global joined_voice_channel
    joined_voice_channel = False
    await ctx.voice_client.disconnect()
client.run(token)            
