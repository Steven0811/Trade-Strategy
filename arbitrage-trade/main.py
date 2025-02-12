from discord_bot.send_message import DiscordBot
import os
import dotenv
import logging

dotenv.load_dotenv()
logging.basicConfig(level=logging.INFO)

dc_bot = DiscordBot(os.getenv("DCBOT_TOKEN"), os.getenv("CHANNEL_ID"))
dc_bot.run("1101.TW", "DFF")