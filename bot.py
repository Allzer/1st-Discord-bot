import discord
from discord.ext import commands
from discord import File
import os
import random

class SlashBot(commands.Bot): #Объявление класса
    def __init__(self): #Функция класса
        super().__init__(command_prefix=".", intents=discord.Intents.default()) #Запускает функцию инит класса
        #self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        self.tree.copy_global_to(guild=discord.Object(id=12345678900987654))
        await self.tree.sync() #Функция для дальнейшего создания команд

bot = SlashBot() #Передаёт класс в переменную bot

@bot.tree.command(name="ping", description="...")
async def _ping(interaction: discord.Interaction) -> None:
    await interaction.response.send_message("pong")

@bot.tree.command(name='xd', description="...")
async def _xd(interaction: discord.Interaction):
    await interaction.response.send_message("XaXaXa")

@bot.tree.command(name='help', description="...")
async def _xd(interaction: discord.Interaction):
    await interaction.response.send_message("Я первый бот Дениса. Так что ждите чего-то мемного")


bot.run('токен')