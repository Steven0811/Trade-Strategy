import yfinance as yf

def get_current_stock_price(ticker: str) -> float:
    stock = yf.Ticker(ticker)
    current_price = stock.history(period='1d')['Close'][0]
    return float(current_price)