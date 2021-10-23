from discord import Message, Webhook, AsyncWebhookAdapter, AllowedMentions
import aiohttp


async def send_webhook(msg: Message, webhook_url: str, channel_settings):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))

        if channel_settings.show_jump:
            prefix = f"[[jump]](<{msg.jump_url}>)\n"
        else:
            prefix = ""

        if channel_settings.add_channel:
            user_suffix = f" [#{msg.channel.name}]"
        else:
            user_suffix = ""

        # parse attachments
        attachments = []
        try:
            attachments.extend([f"[]({a})" for a in msg.attachments])
            attachments.extend([f"[]({s.image_url_as(256)})" for s in msg.stickers])
        except (AttributeError, KeyError, IndexError) as e:
            print(e)
        if attachments:
            attachments = "\n".join(attachments)
        else:
            attachments = ""

        # send
        await webhook.send(
            content=(prefix + msg.content + attachments) or ".",
            embeds=msg.embeds,
            avatar_url=msg.author.avatar_url or msg.author.default_avatar_url,
            username=(msg.author.nick or msg.author.name) + user_suffix,
            tts=msg.tts,
            allowed_mentions=AllowedMentions.none()
        )
