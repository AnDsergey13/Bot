import json
import binance_api
import our_library

bot = binance_api.Binance(
	API_KEY='',
	API_SECRET=''
)

data = bot.exchangeInfo()
our_library.record_in_file('exchangeInfo', data)
