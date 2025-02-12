# 期股套利
此資料夾為實施期股套利各項程式碼，首先程式會計算出每股交易所需成本(含買賣交易稅、手續費)，接著抓取期、現貨價格，以正價差為例，若價差大於交易成本即可進場，此時買現貨、空期貨，並在期貨結算日時平倉，即可實現無成本套利，且勝率為100%，可進場時discord bot會推播訊號

## 使用技術
- yfinance
- selenium動態爬蟲

## 資料來源
- 股票價格 : 由 yfinance 抓取
- 期貨價格 : 由動態爬蟲從期交所行情資訊網(url : https://mis.taifex.com.tw/futures/RegularSession/StockProducts/Futures/)抓取
- 交易成本 : 由期交所提供(url : https://www.taifex.com.tw/cht/4/feeSchedules)