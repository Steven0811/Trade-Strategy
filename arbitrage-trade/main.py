from discord_bot.send_message import DiscordBot
import os
import dotenv

dotenv.load_dotenv()

dc_bot = DiscordBot(os.getenv("DCBOT_TOKEN"), os.getenv("CHANNEL_ID"))
dc_bot.run("1101.TW", "DFF", 25)