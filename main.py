import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents,
                   case_insensitive=False,)
#tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():

    print(f'Bot is ready. Logged in as {bot.user}')
    await bot.load_extension("cogs.meme")

@bot.command()
async def sync(ctx):
    print("sync command")
    if ctx.author.id == 852579745300086835:
        await bot.tree.sync()
        await ctx.send('Command tree synced.')
    else:
        await ctx.send('You must be the owner to use this command!')

# Run the bot
bot.run(TOKEN)
