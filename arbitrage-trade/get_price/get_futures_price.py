from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from crawler.crawler import Crawler
from get_price.config import FutureConfig
from logger.logger import Logger
import time

def get_futures_price(future_code : str) -> float:
    logger = Logger(__name__, "get_futures_price").get_logger()
    driver = Crawler().create_driver()

    driver.get(FutureConfig.url)

    time.sleep(FutureConfig.crawler_sleep_time)
    driver.find_element(By.CLASS_NAME, FutureConfig.button_class_name).click()

    time.sleep(FutureConfig.crawler_sleep_time)
    select_element = driver.find_element(By.CLASS_NAME, FutureConfig.select_class_name)
    select_element.click()
    select = Select(select_element)
    select.select_by_value(future_code)

    time.sleep(FutureConfig.crawler_sleep_time)
    cell = driver.find_element(By.XPATH, FutureConfig.price_xpath)
    price = cell.text

    return float(price)