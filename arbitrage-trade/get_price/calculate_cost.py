'''
交易成本包含期股的交易稅及手續費，計算方式如下：
1. 現股交易稅: 0.3%
2. 現股交易手續費(買賣皆要): 股價 * 股數 * 0.1425%
3. 期貨交易稅: 契約金額 * 0.0002
4. 期貨交易手續費(買賣皆要): 25 / 口
計算成本時，期貨數量為 1 口，現股數量為 2000 股
由於一口期貨為 2 張股票，所以可算出每股平均成本為總成本 / 2000
'''

def calculate_cost(stock_price: float, future_price: float) -> float:
    stock_tax = stock_price * 2000 * 0.003
    stock_fee = stock_price * 2000 * 0.001425 * 2
    future_tax = future_price * 1 * 0.00002
    future_fee = 1 * 25 * 2
    total_cost = (stock_tax + stock_fee + future_tax + future_fee) / 2000
    return total_cost