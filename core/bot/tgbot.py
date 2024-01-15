import aiohttp

from . import BotBase, MsgType


class TelegramBot(BotBase):
    def __init__(self, bot_token, user_id, msg_type=MsgType.MARKDOWN) -> None:
        self.bot_token = bot_token
        self.user_id = user_id
        self.support_markdown = True
        self.message_type = msg_type

    async def send_message(self, message: str) -> tuple[bool, str]:
        """Send message via Telegram"""
        api_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        body = {
            "chat_id": self.user_id,
            "text": message,
        }
        if self.message_type == MsgType.MARKDOWN:
            body["parse_mode"] = "Markdown"
        elif self.message_type == MsgType.HTML:
            body["parse_mode"] = "HTML"
        async with aiohttp.ClientSession(trust_env=True) as session:
            async with session.post(api_url, json=body) as response:
                response.raise_for_status()
        return True
