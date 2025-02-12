class Config:
    user_agent = "user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'"
    referer = "Referer=https://www.wantgoo.com/"
    accept_language = "Accept-Language=zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    other_setting = ["--headless", "--no-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
    user_data_dir = "user-data-dir=/tmp/user-data"