import discord

from discord.ext import commands

description = 'Spicy Bot'
bot_prefix = '!'

client = commands.Bot(description=description, command_prefix=bot_prefix)

@client.event
async def on_ready():
    print('WHATS UP FUCKERZ')
    print('Name : {}'.format(client.user.name))
    print('ID : {}'.format(client.user.id))
    print(discord.__version__)

@client.command(pass_context=True)
async def spicy(ctx):
    await client.say(':fire: :fire: :fire: :fire: :fire: :fire: :fire: :hot_pepper: :hot_pepper: :hot_pepper: :fire: :fire: :fire: :fire: :fire: :fire: :fire:')

@client.command(pass_context=True)
async def spice(ctx):
    await client.say(':fire: :fire: :fire: :fire: :fire: :fire: :fire: :hot_pepper: :hot_pepper: :hot_pepper: :fire: :fire: :fire: :fire: :fire: :fire: :fire:')

@client.event
async def on_message (message) :
    if message.content == "spicy":
        await client.send_message(message.channel, ":fire: :fire: :fire: :fire: :fire: :fire: :fire: :hot_pepper: :hot_pepper: :hot_pepper: :fire: :fire: :fire: :fire: :fire: :fire: :fire:")



client.run('MzU5MTk0NjUwOTQ4NjY1MzQ0.DWAwAA.Qss10pPRjfkTSuSxnEbwo9ILXl4')
