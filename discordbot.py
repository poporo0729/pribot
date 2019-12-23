from discord.ext import commands
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

client.run(token)
