import discord
import os
import random
import datetime
import asyncio
from discord.ext import commands


client = commands.Bot(command_prefix= 'skittle ')

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('skittle info'))
  print('SkittleBot Is online and ready to Be the best discord bot ever!!!!')



#multiplication command
@client.command()
async def multiply(ctx, a: int, b: int):
  embed = discord.Embed(title="Correct answer :",description=a*b,color=0x00ff00)
  embed.set_footer(text="SkittleBot")
  await ctx.send(embed=embed)

#subtract command
@client.command()
async def subtract(ctx, a: int, b: int):
  embed = discord.Embed(title="Correct answer :",description=a-b,color=0x00ff00)
  embed.set_footer(text="SkittleBot")
  await ctx.send(embed=embed)
#divide command
@client.command()
async def divide(ctx, a: int, b: int):
  divide25 = (a/b)
  embed = discord.Embed(title="Correct answer :",description=str(divide25),color=0x00ff00)
  embed.set_footer(text="SkittleBot")
  await ctx.send(embed=embed)

#new calculator discord command addition
@client.command()
async def add(ctx, a: int, b: int):
  embed = discord.Embed(title="Correct answer :",description=a+b,color=0x00ff00)
  embed.set_footer(text="SkittleBot")
  await ctx.send(embed=embed)

#addition information
@client.command(name='addinfo')
async def addinfo(context):
  myEmbed = discord.Embed(title="info For add command " , description="Read below for how to start a add command", colour=0x0920Bea)
  myEmbed.add_field(name="How to Start",value="For add command you do skittle add <number> <number>" )
  myEmbed.add_field(name="Example", value="skittle add 23 85", inline=True)
  myEmbed.set_footer(text='Have fun the add command')
  myEmbed.set_author(name="SkittleBot") 

  await context.message.channel.send(embed=myEmbed)


#8ball information
@client.command(name='8ballinfo')
async def _8ballinfo(context):
  myEmbed = discord.Embed(title="info For 8ball command " , description="Read below for how to start a 8ball command", colour=0x00ff00)
  myEmbed.add_field(name="How to Start",value="For 8ball command you do skittle 8ball <question>" )
  myEmbed.add_field(name="Example", value="skittle 8ball is this a good command", inline=True)
  myEmbed.set_footer(text='Have fun the 8ball command')
  myEmbed.set_author(name="SkittleBot") 

  await context.message.channel.send(embed=myEmbed)



@client.command(name='ban')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f"{member} was banned!")

@client.command(name='kick')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f"{member} was kicked!")

@client.command(name='ginfo')
async def ginfo(context):
  myEmbed = discord.Embed(title="info For Giveaway", description="Below is how to make a giveaway. NOTE You need a owner role", colour=0x00ff00)
  myEmbed.add_field(name="How to Start",value="skittle gstart seconds prize" )
  myEmbed.add_field(name="Example", value="skittle gstart 10 Discord Nitro", inline=True)
  myEmbed.set_footer(text='Have fun with giveaway command!')
  myEmbed.set_author(name="SkittleBot") 

  await context.message.channel.send(embed=myEmbed)



@client.command(name='clearinfo')
async def clearinfo(context):
  myEmbed = discord.Embed(title="Info For Clear Command",description="The Clear Command is used to clear messages in a channel", colour=0x00ff00)
  myEmbed.add_field(name="Why is this command useful?", value="This command is great for clearing out messages in a channel", inline=True)
  myEmbed.set_footer(text='This is the info for the clear command')
  myEmbed.set_author(name="SkittleBot")

  await context.message.channel.send(embed=myEmbed)


@client.command(name='infoping')
async def infoping(context):
  myEmbed = discord.Embed(title="Info For Ping Command",description="The ping Command is used to check the latency of the Bot", colour=0x00ff00)
  myEmbed.add_field(name="Why is this command useful?", value="This command is greate for checking the latency of the bot", inline=True)
  myEmbed.set_footer(text='This is the info for the ping command')
  myEmbed.set_author(name="SkittleBot")

  await context.message.channel.send(embed=myEmbed)

#custom help command
@client.command(name='info')
async def info(context):
  myEmbed = discord.Embed(title="Type skittle <commandname>info for command help", description="These are the commands for the discord bot", colour=0x00ff00)
  myEmbed.add_field(name="Moderation",value="Clear" )
  myEmbed.add_field(name="Giveaway", value="Giveaway Command!")
  myEmbed.add_field(name="Maths", value="Add, Subtract, Multiply, Divide")
  myEmbed.add_field(name="Fun", value="Ping, 8ball", inline=True)
  myEmbed.set_footer(text='These are the commands for the bot so far')
  myEmbed.set_author(name="SkittleBot") 

  await context.message.channel.send(embed=myEmbed)



#Giveaway  
@client.command()
@commands.has_permissions(administrator=True)
async def gstart(ctx, mins : int, *, prize: str):
  embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

  end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60)

  embed.add_field(name = "Ends At:", value = f"{end} UTC")
  embed.set_footer(text = "🎉This is a giveaway!🎉")

  my_msg = await ctx.send(embed = embed)

  await my_msg.add_reaction("🎉")

  await asyncio.sleep(mins)

  new_msg = await ctx.channel.fetch_message(my_msg.id)

  users = await new_msg.reactions[0].users().flatten()
  users.pop(users.index(client.user))

  winner = random.choice(users)

  await ctx.send(f"Congratulations! {winner.mention} won {prize}! ")

#ping latency of the discord bot
@client.command()
async def ping(ctx):
  await ctx.send(f'🏓 Pong! {round(client.latency * 1000)}ms ')


#clear command
@client.command()
@commands.has_permissions(administrator=False)
async def clear(ctx, amount : int):
  await ctx.channel.purge(limit=amount)

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = ["It is certain.",
               "It is decidedly so.",
               "Without a doubt.",
               "Yes - definitely.",
               "You may rely on it.",
               "As I see it, yes.",
               "Most likely.",
               "Outlook good.",
               "Yes.",
               "Signs point to yes.",
               "Reply hazy, try again.",
               "Ask again later.",
               "Better not tell you now.",
               "Cannot predict now.",
               "Concentrate and ask again.",
               "Don't count on it.",
               "My reply is no.",
               "My sources say no.",
               "Outlook not so good.",
               "Very doubtful."]
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')             



@clear.error
async def clear_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Please specify every requirment for this command')

client.run(os.getenv('TOKEN'))  

