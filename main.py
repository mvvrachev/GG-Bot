import os
import discord
from discord.ext import commands
import random

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

'''@client.command()
async def natupan(ctx):
  if ctx.message.author.voice is None:
    await ctx.send("Vlez v channel palavniko!")
  else:
    voice_channel = ctx.message.author.voice.channel
    voice_client = await voice_channel.connect()
    audio_src = discord.FFmpegPCMAudio('./audio_files/natupan.mp3')
    voice_client.play(audio_src)
    while 1:
      if(voice_client.is_playing()):
        continue
      else:
        await voice_client.disconnect()
        break
    await ctx.message.delete()

@client.command()
async def misho(ctx):
  if ctx.message.author.voice is None:
    await ctx.send("Vlez v channel palavniko!")
  else:
    voice_channel = ctx.message.author.voice.channel
    voice_client = await voice_channel.connect()
    audio_src = discord.FFmpegPCMAudio('./audio_files/misho.mp3')
    voice_client.play(audio_src)
    while 1:
      if(voice_client.is_playing()):
        continue
      else:
        await voice_client.disconnect()
        break
    await ctx.message.delete()'''


@client.command(aliases=['p', 'paly', 'Play', 'P'])
async def play(ctx, *arg):
  if len(arg) == 0:
    await ctx.send('Utochni kakfo iskash da play-nesh vuv voice channela palavniko!')
  else:
    if ctx.message.author.voice is None:
      await ctx.send("Vlez v channel palavniko!")

    else:
      audio_src = None
      if arg[0] == 'misho':
        audio_src = discord.FFmpegPCMAudio('./audio_files/misho.mp3')
      elif arg[0] == 'natupan':
        audio_src = discord.FFmpegPCMAudio('./audio_files/natupan.mp3')
      else:
        await ctx.send("Nqma takuv nali4en fail palavniko!")

      if audio_src is not None:
        voice_channel = ctx.message.author.voice.channel
        voice_client = await voice_channel.connect()
        voice_client.play(audio_src)
        while 1:
          if(voice_client.is_playing()):
            continue
          else:
            await voice_client.disconnect()
            break
        await ctx.message.delete()

@client.command()
async def fart(ctx):
  if ctx.message.author.voice is None:
      await ctx.send("Vlez v channel palavniko!")
  else:
    voice_channel = ctx.message.author.voice.channel
    voice_client = await voice_channel.connect()
    fart_number = random.randint(1,108)
    audio_src = discord.FFmpegPCMAudio('./farts/fart' + str(fart_number) + '.mp3')
    voice_client.play(audio_src)
    while 1:
      if(voice_client.is_playing()):
        continue
      else:
        await voice_client.disconnect()
        break
    await ctx.message.delete()
 
client.run(os.environ['TOKEN'])