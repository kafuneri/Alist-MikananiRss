import aiohttp

from . import BotBase


class TelegramBot(BotBase):
    def __init__(self, bot_token, user_id) -> None:
        self.bot_token = bot_token
        self.user_id = user_id
        self.support_markdown = False

    async def send_message(self, message: str) -> bool:
        """Send message via fwalert"""
        api_url = f"https://fwalert.com/{self.bot_token}"
        body = {"chat_id": self.user_id, "text": message, "parse_mode": "HTML"}
        async with aiohttp.ClientSession(trust_env=True) as session:
            async with session.post(api_url, json=body) as response:
                response.raise_for_status()
        return True
