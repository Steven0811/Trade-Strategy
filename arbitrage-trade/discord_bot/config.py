from datetime import time
from datetime import datetime
import pytz

class Config:
    stock_per_future = 2000
    start_time = time(9, 0)
    end_time = time(13, 30)
    taiwan_tz = pytz.timezone('Asia/Taipei')
    current_time = datetime.now(taiwan_tz).time()