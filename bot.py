import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('MTUyMTIxNjY2NDEwMjc2ODk1Mg.GzJy29.MkdyADT7NEOp6pcEbsWy2prT78x3USG6-gLA6o')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} se ha conectado a Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.lower() == 'hola':
        await message.channel.send(f'¡Hola {message.author.name}! 👋')
    
    await bot.process_commands(message)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'🏓 Pong! Latencia: {round(bot.latency * 1000)}ms')

@bot.command(name='usuario')
async def usuario(ctx):
    embed = discord.Embed(title=f"Información de {ctx.author.name}", color=discord.Color.green())
    embed.add_field(name="ID", value=ctx.author.id, inline=False)
    await ctx.send(embed=embed)

bot.run(MTUyMTIxNjY2NDEwMjc2ODk1Mg.GzJy29.MkdyADT7NEOp6pcEbsWy2prT78x3USG6-gLA6o)
