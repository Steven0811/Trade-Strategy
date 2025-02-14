import yfinance as yf
from logger.logger import Logger

def get_current_stock_price(ticker: str) -> float:
    logger = Logger(__name__, "get_current_stock_price").get_logger()

    try:
        stock = yf.Ticker(ticker)
        current_price = stock.history(period='1d')['Close'][0]
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None
    return float(current_price)