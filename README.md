# 股票交易策略自動化
此專案為自動化交易而生，實行各項交易策略並回測，目標找出績效最好，能穩定獲利的交易策略，連接discord bot推播，告知使用者進出場時機

## 使用技術
- 訊號推播 : discord bot
- 取得即時行情
   - 股票 : yfinance
   - 期貨 : selenium動態爬蟲
- 部署 : Docker, Docker Compose

## 使用環境
- Python 3.8 或更高

## 使用方法
1. **創建discord bot**
至discord developer創建一隻專屬機器人並將其邀請至指定discord伺服器
(url: https://discord.com/developers/applications)
3. **clone the repository**
     ```bash
    git clone https://github.com/Steven0811/Trade-Strategy.git
    cd trade-stratege
     ```
3. **運行Docker**
    ```bash
    docker-compose up
    ```

## 各項策略
- arbitrage-trade : 期貨股票套利