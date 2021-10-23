import discord
import config
import json
from send_utils import send_webhook

config = config.Config(json.load(open('config.json', 'r', encoding='utf-8')))


class AnnouncerClient(discord.Client):
    async def on_ready(self):
        await self.change_presence(status=discord.Status.offline)

    async def on_message(self, message: discord.Message):
        if message.channel.id not in config.channel_map.keys():
            return

        channel = config.channel_map[message.channel.id]
        if not channel.filter(message):
            return

        await send_webhook(message, channel.webhook_url, channel)


client = AnnouncerClient()
client.run(config.token)
