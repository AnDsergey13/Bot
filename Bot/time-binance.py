import csv
import json

from binance_api import Binance
bot = Binance(
    API_KEY='',
    API_SECRET=''
)

#запись данных в файл
def rec():
	i = bot.time('serverTime')
	my_file = open('time.txt', 'w')
	my_file.write(str(i))
	my_file.close()

print(bot.time())


json_string = bot.time()
#parsed_string = json.load(json_string)
print(json_string['serverTime'])
#parsed_string = ['serverTime']
'''
json_str = '{"serverTime": 1542267149637}'
json_prs = json.load(json_str)
print(json_prs['serverTime'])
'''
spisok_pokupok = {
	'Сметана':{
		'Name':"Сметана",
		'Price':1.5,
		'Date':"11 ноября"
		},
	'Чебурек':{
		'Name':"Чебурек",
		'Price':5,
		'Date':"3 ноября"
		},
	'Молоко':{
		'Name':"Молоко",
		'Price':2.95,
		'Date':"15 ноября"
		}
	}
for item in spisok_pokupok:
	   print(spisok_pokupok[item]['Name'])
#print(spisok_pokupok['Чебурек'])
'''
for items in spisok_pokupok:
    print("Текущее значение переменной items=", items)
    print("В словаре под этим ключом хранится вот что: ", spisok_pokupok[items])
    print("Возьмем из вложенного словаря значение name -> ", spisok_pokupok[items]['Name'])
    print('---')
'''
for key, value in spisok_pokupok.items():
    print(key, value)
    print(value['Name'])
    print('---')