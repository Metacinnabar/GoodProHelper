from dotenv import dotenv_values
config = dotenv_values(".env")

import imageio
from imageio import imread

from discord.ext import tasks
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user.name} ({self.user.id})")

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.starts

client = MyClient()
client.run(config.get("TOKEN"))