import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "%")

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

  '''@client.command(pass_context = True)
async def join(ctx):
  user = ctx.message.author
  voice_channel = user.voice.channel

  if voice_channel!= None:
    await client.join_channel(voice_channel)
  else:
      await client.say('Vlez v channel mrusniko!')'''

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

@client.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.format(member))

@client.command()
async def join(ctx):
  await client.connect()

client.run(os.environ['TOKEN'])