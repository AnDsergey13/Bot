import json
#import binance_api
import our_library
'''
bot = binance_api.Binance(
    API_KEY='qRmmGsVlut46jEAYV6oKu6QuvEOrKPkg5aflmYkgmvOglBBbVl0ixMn8u1pf82sc',
    API_SECRET='GGw5Rr5fan9JC1dIhfyQMM5JFR5riPgCcM9wCUOk5NkUDbBaARAajKPlqUi1gx9R'
)
'''

from binance_api import Binance

bot = Binance(
    API_KEY='qRmmGsVlut46jEAYV6oKu6QuvEOrKPkg5aflmYkgmvOglBBbVl0ixMn8u1pf82sc',
    API_SECRET='GGw5Rr5fan9JC1dIhfyQMM5JFR5riPgCcM9wCUOk5NkUDbBaARAajKPlqUi1gx9R'
)

data = bot.exchangeInfo()
our_library.record_in_file('exchangeInfo', data)
'''
data = bot.depth(symbol='BNBBTC')
our_library.record_in_file('depth', data)

data = bot.trades(symbol='BNBBTC')
our_library.record_in_file('trades', data)
'''
#data = bot.historicalTrades(symbol='BNBBTC', limit=5)
#our_library.record_in_file('historicalTrades', data)
'''
data = bot.aggTrades(symbol='BNBBTC')
our_library.record_in_file('aggTrades', data)

data = bot.klines(symbol='BNBBTC', interval='5m')
our_library.record_in_file('klines', data)

data = bot.ticker24hr(symbol='BNBBTC')
our_library.record_in_file('ticker24hr', data)

data = bot.tickerPrice(symbol='BNBBTC')
our_library.record_in_file('tickerPrice', data)

data = bot.tickerBookTicker(symbol='BNBBTC')
our_library.record_in_file('tickerBookTicker', data)
'''