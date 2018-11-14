import csv
import json

from binance_api import Binance
bot = Binance(
    API_KEY='',
    API_SECRET=''
)

def rec():
	i = bot.time('serverTime')
	my_file = open('time.txt', 'w')
	my_file.write(str(i))
	my_file.close()

print(bot.time())
#запись данных в файл
'''
json_string = bot.time()
parsed_string = json.load(json_string)
print(parsed_string['serverTime'])
#parsed_string = ['serverTime']
'''
json_str = '{"commit":13}'
json_prs = json.load(json_str)
print(json_prs['commit'])