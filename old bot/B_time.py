import json
from binance_api import Binance

bot = Binance(
    API_KEY='',
    API_SECRET=''
)

def record_in_file():
	my_file = open('B_time.txt', 'w')
	my_file.write(str(binance_time))
	my_file.close()
	print('Данные записаны в файл')

response_from_binance = bot.time()
print(response_from_binance)
binance_time = response_from_binance['serverTime']
print(binance_time)
record_in_file()
