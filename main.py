import asyncio
import json
from os.path import isfile

import discord

from config import Config
from send_utils import send_webhook

config = Config(json.load(open("config.json", "r")))
history = {} if not isfile("history.json") else json.load(open("history.json", 'r'))


class AnnouncerClient(discord.Client):
    async def channel_history(self, channel_id):
        history.setdefault(channel_id, 0)
        last_timestamp = history[channel_id]
        channel = self.get_channel(channel_id)
        channel_config = config.channel_map[channel_id]

        async for msg in channel.history(limit=10):
            timestamp = discord.utils.snowflake_time(msg.id).timestamp()
            if timestamp <= last_timestamp:
                continue
            if not channel_config.filter(msg):
                continue

            await send_webhook(msg, **dict(channel_config))
            history[channel_id] = max(history[channel_id], timestamp)

        if history[channel_id] == 0:  # remove if default
            del history[channel_id]

    async def on_ready(self):
        await self.change_presence(status=discord.Status.offline)

        # check history of all channels in config.json
        await asyncio.gather(*[self.channel_history(i) for i in config.channel_map.keys()])

    async def on_message(self, message: discord.Message):
        for entry in config.globals:
            if entry.filter(message):
                await send_webhook(message, **dict(entry))

        if message.channel.id not in config.channel_map.keys():
            return

        channel = config.channel_map[message.channel.id]
        if not channel.filter(message):
            return

        await send_webhook(message, **dict(channel))


client = AnnouncerClient()
try:
    client.run(config.token)
except BaseException as ex:
    print(ex)
with open("./history.json", "w+") as fp:
    history = {k:v+1 for k,v in history.items()}  # add +1 to all timestamps (this removes duplicates
    json.dump(history, fp)
