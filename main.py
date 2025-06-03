import discord
from discord.ext import commands

# Hard-coded list of phrases to watch for (case-insensitive)
PHRASES_TO_DELETE = [
    "secret phrase",
    "another bad phrase",
    "sensitive info"
]

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Required for reading message content
bot = commands.Bot(command_prefix="!", intents=intents)

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

bot.run("YOUR_DISCORD_BOT_TOKEN")
