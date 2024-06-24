import discord
from discord.ext import commands
from utils.cog_loader import load_cogs
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
GUILD_ID = os.getenv("GUILD_ID")
APPLICATION_ID = os.getenv("APPLICATION_ID")

class MyClinet(commands.Bot) :
    def __init__ (self):
        super().__init__(command_prefix="/", intents=discord.Intents.all(),
                         case_insensitive=False, applpication_id = APPLICATION_ID)

    async def setup_hook(self):
        # Load cogs
        await load_cogs(self)  # Await the load_cogs function

        # Sync command tree with a specific guild
        await self.tree.sync(guild=discord.Object(id=GUILD_ID))

    async def on_ready(self):
        print(f'{self.user} is now Online!')


bot = MyClinet()



bot.run(TOKEN)
