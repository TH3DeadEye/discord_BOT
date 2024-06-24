import discord 
from discord.ext import commands 
from discord import app_commands

class test (commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name= "test", 
        description="This is a test command",

    )
    async def test(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("This is a test command!", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        test(bot), 
        guilds = [discord.Object(id =946701951771496508 )])