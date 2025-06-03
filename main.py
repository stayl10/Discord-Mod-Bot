import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load the token from the .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Define intents and bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# List of phrases to delete (case-insensitive)
PHRASES_TO_DELETE = [
    "secret phrase",
    "another bad phrase",
    "sensitive info"
]

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content_lower = message.content.lower()
    if any(phrase in content_lower for phrase in PHRASES_TO_DELETE):
        await message.delete()
        print(f"Deleted message from {message.author}: {message.content}")
        return

    await bot.process_commands(message)

# Run the bot with your secure token
bot.run(TOKEN)
