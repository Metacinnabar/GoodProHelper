from dotenv import dotenv_values
config = dotenv_values(".env")

from discord.ext import tasks
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user.name} ({self.user.id})")

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith("!"):
            msg = message.content[1:]
            if msg == "ping":
                await message.channel.send("Pong! Hello world!")
            if msg == "download":
                await message.delete()
                await message.channel.send("shut the fuck up", delete_after=3.0)


client = MyClient()
client.run(config.get("TOKEN"))
