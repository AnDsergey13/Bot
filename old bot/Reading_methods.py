from binance_api import Binance

bot = Binance(
    API_KEY='',
    API_SECRET=''
)

def rm_klines(symbol, interval, limit):
	symbol='symbol=' + symbol
	interval= 'interval=' + interval
	list_klines = bot.klines(symbol='BTCUSDT', interval='1m', limit=1)
	list_klines = list_klines[0]
	return list_klines
	
# нужел ли вообще этот модуль?
def rm_time():
	list_time = bot.time()
	#list_time = int(time_check['serverTime'])
	return list_time
