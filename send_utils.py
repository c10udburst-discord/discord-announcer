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
            pass
        if attachments:
            attachments = " " + " ".join(attachments)
        else:
            attachments = ""

        content = ""
        try:
            content = msg.content
        except AttributeError:
            pass
        content = prefix + content + attachments
        
        embeds = []
        try:
            embeds = msg.embeds
        except AttributeError:
            pass
        
        if not content and len(embeds)<1:
            content = f"[[jump]](<{msg.jump_url}>)\n"

        # send
        await webhook.send(
            content=content,
            embeds=embeds,
            avatar_url=get_avatar(msg.author),
            username=get_username(msg.author) + user_suffix,
            tts=msg.tts,
            allowed_mentions=AllowedMentions.none()
        )


def get_username(user) -> str:
    name = ""
    try:
        name = user.nick
    except AttributeError:
        pass
    try:
        name = user.name
    except AttributeError:
        pass
    if not name:
        name = "Unknown User"
    return name


def get_avatar(user) -> str:
    url = ""
    try:
        url = user.avatar_url
    except AttributeError:
        pass
    try:
        url = user.default_avatar_url
    except AttributeError:
        pass
    if not url:
        url = "https://discord.com/assets/1f0bfc0865d324c2587920a7d80c609b.png"
    return url
