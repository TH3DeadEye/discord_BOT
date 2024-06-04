import discord
from discord.ext import commands
from discord import app_commands
import os
class MemeModal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="Create a Meme")

        self.top_text = discord.ui.TextInput(label="Top Text", style=discord.TextStyle.short)
        self.add_item(self.top_text)

        self.bottom_text = discord.ui.TextInput(label="Bottom Text", style=discord.TextStyle.short)
        self.add_item(self.bottom_text)

        self.image_url = discord.ui.TextInput(label="Image URL", style=discord.TextStyle.short)
        self.add_item(self.image_url)

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Here's your meme!", color=discord.Color.blue())
        embed.set_image(url=self.image_url.value)
        embed.add_field(name="Top Text", value=self.top_text.value, inline=False)
        embed.add_field(name="Bottom Text", value=self.bottom_text.value, inline=False)
        
        await interaction.response.send_message(embed=embed, ephemeral = True)

class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} cog loaded.')

    @app_commands.command(name="meme", description="Create a meme")
    async def meme(self, interaction: discord.Interaction):
        await interaction.response.send_modal(MemeModal())

async def setup(bot):
   await bot.add_cog(Meme(bot))
    
