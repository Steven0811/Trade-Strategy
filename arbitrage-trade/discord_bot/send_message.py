import discord
import time
from get_price.get_stock_price import get_current_stock_price
from get_price.get_futures_price import get_futures_price
from get_price.calculate_cost import calculate_cost
from discord_bot.config import Config
from logger.logger import Logger

class DiscordBot():
    def __init__(self, token: str, channel_id: int):
        self.token = token
        self.channel_id = channel_id
        self.client = discord.Client(intents=discord.Intents(guilds=True, messages=True))
    
    async def arbitrage(self, stock_code: str, future_code: str, future_fee: int):
        logger = Logger(__name__, "arbitrage").get_logger()

        while True:
            stock_price = get_current_stock_price(stock_code)
            future_price = get_futures_price(future_code)
            cost = calculate_cost(stock_price, future_price, future_fee)
            logger.debug(f"Fetching stock price: {stock_price}, future price: {future_price}, cost: {cost}")

            try:
                if(abs(stock_price - future_price) < cost):
                    channel = await self.client.fetch_channel(self.channel_id)
                    if channel is None:
                        logger.error(f"Channel not found or Bot has no access: {self.channel_id}")
                        return
                    profit = (stock_price - future_price - cost) * Config.stock_per_future if stock_price > future_price else (future_price - stock_price - cost) * Config.stock_per_future
                    await channel.send(f"# 🎉 套利進場通知 🎉\n"
                                    f"```diff\n"
                                    f"🚀 {stock_code} 🚀\n"
                                    f"```\n"
                                    f"**💹 現貨價格：** `{stock_price:.1f}` 元\n"
                                    f"**📉 期貨價格：** `{future_price:.1f}` 元\n"
                                    f"**💰 預估成本：** `{cost:.1f}` 元\n"
                                    f"**💵 預期獲利：** `{profit:.1f}` 元\n")

            except discord.NotFound:
                logger.error(f"Channel not found: {self.channel_id}")
            except discord.Forbidden:
                logger.error(f"Bot is not allow to access the channel ID: {self.channel_id}")
            except Exception as e:
                logger.error(f"Unexpected Error: {e}")
            time.sleep(30)

    def run(self, stock_code: str, future_code: str, future_fee: int):
        logger = Logger(__name__, "run").get_logger()

        @self.client.event
        async def on_ready():
            logger.debug(f"Logged in as {self.client.user}")
            logger.debug(f"Channel ID: {self.channel_id}")
            await self.arbitrage(stock_code, future_code, future_fee)
        
        self.client.run(self.token)