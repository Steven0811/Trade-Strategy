from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from crawler.config import Config
from logger.logger import Logger

class Crawler:
    def __init__(self):
        self.user_agent = Config.user_agent
        self.referer = Config.referer
        self.accept_language = Config.accept_language
    
    def create_driver(self) -> webdriver.Chrome:
        logger = Logger(__name__, "create_driver").get_logger()
        try:
            options = webdriver.ChromeOptions()
            options.add_argument(self.user_agent)
            options.add_argument(self.referer)
            options.add_argument(self.accept_language)
            for setting in Config.other_setting:
                options.add_argument(setting)
            options.add_argument(Config.user_data_dir)

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            logger.debug("Driver is created successfully")
            
        except Exception as e:
            logger.error(f"Unexpected error occurred: {e}")
            return None
        return driver