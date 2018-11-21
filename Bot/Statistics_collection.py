from Reading_methods import *
from binance_api import Binance

bot = Binance(
    API_KEY='',
    API_SECRET=''
)


symbol = "'BTCUSDT'"
interval= "'1m'"
limit=1
list_klines = rm_klines(symbol, interval, limit)
print("Чтение прошло успешно\n" + str(list_klines))
list_time = rm_time()
print("Чтение прошло успешно\n" + str(list_time))