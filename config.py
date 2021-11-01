from discord import Message
from typing import Dict, Optional
import re


def parse_filter(raw: str) -> str:
    raw = raw.replace("is_bot", "msg.author.bot")
    raw = raw.replace("is_webhook", "(msg.webhook_id is not None)")
    raw = raw.replace("has_embed", "(len(msg.embeds)>0)")
    return raw


class Channel:
    def __init__(self, data: Optional[Dict] = None):
        if data is None:
            self.webhook = ""
            self.id = 0
            self.show_jump = False
            self.add_channel = False
            self.filter_src = ""
        else:
            self.webhook = data['webhook']
            if isinstance(data['id'], list):
                self.id = [int(i) for i in data['id']]
            else:
                self.id = int(data['id'])
            self.show_jump = data.get('show_jump', False)
            self.add_channel = data.get('add_channel', False)
            self.filter_src = parse_filter(data.get('filter', ""))

        self.webhook = "/".join(self.webhook.split("/")[-2:])

    @property
    def webhook_url(self):
        return "https://discord.com/api/webhooks/" + self.webhook

    def filter(self, msg: Message) -> bool:
        if not self.filter_src:
            return True
        return eval(self.filter_src)


class Config:
    def __init__(self, data: Optional[Dict] = None):
        if data is None:
            self.token = ""
            self.channels = []
            self.show_jump = True
        else:
            self.token = data['token']
            self.channels = [Channel(c) for c in data.get('channels', [])]
            self.show_jump = data.get("show_jump", True)

        self.channel_map = {}
        for channel in self.channels:
            if isinstance(channel.id, list):
                for i in channel.id:
                    self.channel_map[i] = channel
            else:
                self.channel_map[channel.id] = channel
