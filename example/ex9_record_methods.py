import csv
import json

from binance_api import Binance
bot = Binance(
    API_KEY='',
    API_SECRET=''
)

#print(bot.aggTrades(symbol='BNBBTC',limit=50))

#запись данных в файл
def rec():
	my_file = open('exchangeInfo.txt', 'w'.format(rus_name))
	my_file.write(str(name_file))
	my_file.close()

Alpha = {
	'A':"Арбуз",
	'B':"Ботва",
	'V':"Ванюха",
	'G':"Гризли",
	'D':"Дурачок",
	'E':"Ель",
	'E_':"Ёж",
	'GH':"Жопа",
	'Z':"Зебра"
}





'''
exch_string = bot.exchangeInfo()
print(pair['symbols'])
'''
'''
methodss = {
	'exchangeInfo':"bot.exchangeInfo()",
	'depth':"bot.depth()",
	'trades':"bot.trades()",
	'historicalTrades':"bot.historicalTrades()",
	'aggTrades':"bot.aggTrades()",
	'klines':"bot.klines()",
	'ticker24hr':"bot.ticker24hr()",
	'tickerPrice':"bot.tickerPrice()",
	'tickerBookTicker':"bot.tickerBookTicker()"
}
'''

#print(bot.exchangeInfo())
'''
print(bot.depth())
print(bot.trades())
print(bot.historicalTrades())
print(bot.aggTrades())
print(bot.klines())
print(bot.ticker24hr())
print(bot.tickerPrice())
print(bot.tickerBookTicker())'''