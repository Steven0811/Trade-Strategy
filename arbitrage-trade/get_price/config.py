class FutureConfig:
    url = "https://mis.taifex.com.tw/futures/RegularSession/StockProducts/Futures/"
    crawler_sleep_time = 1
    button_class_name = "btn" 
    select_class_name = "form-control.form-select"
    price_xpath = f"//table/tbody/tr[2]/td[7]"