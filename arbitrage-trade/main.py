from discord_bot.send_message import DiscordBot
from company import company
import os
import dotenv

dotenv.load_dotenv()

dc_bot = DiscordBot(os.getenv("DCBOT_TOKEN"), os.getenv("CHANNEL_ID"))
for stock_code, future_code in company:
    dc_bot.run(stock_code, future_code, 25)