from binance_api import Binance
import pdb
import time
import copy # Нужен ли этот модуль вообще?
#pdb.set_trace()

bot = Binance(
    API_KEY='',
    API_SECRET=''
)

period_record = 1	#Сколько производить запись в минутах
delay = 20	#задержка между двумя запросми (по умолчанию)(в секундах)

def record_in_file():	#запись фильтрованных значений
	for string in range_for_record:
		test_data.write(str(string))
		test_data.write("\n")
		#print(string) 

def request_time():
	current_time = bot.time()
	current_time = int(current_time['serverTime'])
	return current_time

test_data = open("statistic_data.txt", "w")
first_request = bot.trades(symbol='BTCUSDT', limit = 500)
range_for_record = copy.deepcopy(first_request)	#!!!
record_in_file()			
del range_for_record							#!!!

period_in_second = period_record * 60 *	1000 #перевод в милисекунды для binance
#start_record = int(round(time.time(),0))*1000 
start_record = request_time()
end_record = start_record + period_in_second
#print(start_record, " ", end_record)
#print(end_record - start_record)

test_string = first_request[-1]

while 1:
	current_time = request_time()

	#print("PC     ",int(round(time.time(),0)))
	#print("end_record 	  = ", end_record)
	#rint("B_current_time = ", current_time)
	ostatok = (end_record - current_time)/1000
	print("Продолжаем, осталось = ", int(ostatok))

	if current_time < end_record:
		time.sleep(delay)
		second_request = bot.trades(symbol='BTCUSDT', limit = 500)

		last_index_sec_req = len(second_request)	# номер последней строки +1
		#(!)
		num_str_sec_req = 0

		for string_sec_req in second_request:
			if test_string == string_sec_req:	#нахождение строки (2 list), на которой закончился прошлый запрос (1 list)
				num_str_sec_req += 1			#выставляем номер строки для начала записи (след. строка после обнаруженной)
				#itr = iter(num_list)
				range_for_record = second_request[num_str_sec_req:last_index_sec_req]
				test_string = range_for_record[-1]	#при следующих записях, обновляет проверочную строку во избежания сдвига при записи
				record_in_file()
				del range_for_record
				break
			num_str_sec_req += 1
		else:
			print("Увеличьте число сделок в методе, или уменьшите время запроса")
	else:
		print("Конец записи")
		break
test_data.close()
'''
tt = bot.time()
print("Binance",tt['serverTime'])	#время биржи отстаёт, в среднем, на 34 секунды
print("PC     ",int(round(time.time(),0)))
'''