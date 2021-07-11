import os
import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix = "%")

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.command()
async def daniele(ctx):
  await ctx.send("Daniele stiga me qdosva!")
  await ctx.message.delete()

@client.command()
async def daniele1(ctx, *arg):
  result = "Daniele"
  for i in arg:
    result += " " + i
  await ctx.send(result)
  await ctx.message.delete()

@client.command()
async def lut(ctx):
  user = str(ctx.author)
  u = user[:-5]
  await ctx.send("Eeeeeeee " + u + " mnooo si lut, be lutko")
  await ctx.message.delete()

@client.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.format(member))

@client.command()
async def natupan(ctx):
  if ctx.message.author.voice is None:
    await ctx.send("Vlez v channel palavniko!")
  else:
    voice_channel = ctx.message.author.voice.channel
    voice_client = await voice_channel.connect()
    audio_src = discord.FFmpegPCMAudio('natupan.mp3')
    voice_client.play(audio_src)

@client.command()
async def misho(ctx):
  if ctx.message.author.voice is None:
    await ctx.send("Vlez v channel palavniko!")
  else:
    voice_channel = ctx.message.author.voice.channel
    voice_client = await voice_channel.connect()
    audio_src = discord.FFmpegPCMAudio('misho.mp3')
    voice_client.play(audio_src)
    
client.run(os.environ['TOKEN'])