from binance_api import Binance
import pdb
import time
import copy
#pdb.set_trace()

bot = Binance(
    API_KEY='',
    API_SECRET=''
)
'''
period_record = 10	#в минутах
period_in_second = period_record * 60 *	1000 #перевод в секунды для binance
start_record = int(round(time.time(),0))*1000 
end_record = start_record + period_in_second
#print(start_record, " ", end_record)
'''
'''
first_request = [
	{'a':1, 'b':2, 'c':3},
	{'a':2, 'b':3, 'c':4},
	{'a':3, 'b':4, 'c':5},
	{'a':4, 'b':5, 'c':6},
	{'a':5, 'b':6, 'c':7},
	]

second_request = [
	{'a':3, 'b':4, 'c':5},
	{'a':4, 'b':5, 'c':6},
	{'a':5, 'b':6, 'c':7},
	{'a':6, 'b':7, 'c':8},
	{'a':7, 'b':8, 'c':9},	
	]
'''

def record_in_file():	#запись фильтрованных значений
	for string in range_for_record:
		test_data.write(str(string))
		test_data.write("\n")
		#print(string) 

test_data = open("statistic_data.txt", "w")
first_request = bot.trades(symbol='BTCUSDT', limit = 20)
range_for_record = copy.deepcopy(first_request)
record_in_file()
del range_for_record

time.sleep(2)
second_request = bot.trades(symbol='BTCUSDT', limit = 20)
print("создан второй лист")

last_index_sec_req = len(second_request)	# номер последней строки +1
test_string = first_request[-1]
num_str_sec_req = 0

for string_sec_req in second_request:
	if test_string == string_sec_req:	#нахождение строки (2 list), на которой закончился прошлый запрос (1 list)
		num_str_sec_req += 1			#выставляем номер строки для начала записи (след. строка после обнаруженной)
		range_for_record = second_request[num_str_sec_req:last_index_sec_req]
		record_in_file()
		#new_list = first_request + second_request[num_str_sec_req:last_index_sec_req]	#сшивание недостающих данных с первым списком
		break
	num_str_sec_req += 1
else:
	print("увеличьте число сделок в методе")
#print(new_list)
test_data.close()
'''
tt = bot.time()
print("Binance",tt['serverTime'])	#время биржи отстаёт, в среднем, на 34 секунды
print("PC     ",int(round(time.time(),0)))
'''