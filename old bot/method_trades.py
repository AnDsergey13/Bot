from binance_api import Binance
import threading
import pdb
import time
import json
#pdb.set_trace()

bot = Binance(
    API_KEY='',
    API_SECRET=''
)

period_record = 20	#Сколько производить запись в секундах
delay = 5	#задержка между двумя запросми (по умолчанию)(в секундах)

def record_in_file():	#запись фильтрованных значений
	#print(range_for_record)
	for string in range_for_record:
		test_data.write(str(string))
		test_data.write(",\n")
		
def request_time():
	current_time = bot.time()
	current_time = int(current_time['serverTime'])
	return current_time

def countdown(end_record):		#параллельный поток для показа времени
	while 1:
		current_time = request_time()
		ostatok = (end_record - current_time)/1000
		if current_time >= end_record:
			break
		print("Осталось = {o:0.1f} секунд".format(o=ostatok))
		time.sleep(0.4)


test_data = open("statistic_data.json", "w")
first_request = bot.trades(symbol='BTCUSDT', limit = 300)
range_for_record = first_request.copy()

record_in_file()			
del range_for_record							#!!!

period_in_second = period_record * 1000 #перевод в милисекунды для binance
start_record = request_time()
end_record = start_record + period_in_second

test_string = first_request[-1]

t = threading.Thread(target=countdown, args=(end_record,))
t.start()


while 1:
	current_time = request_time()

	if current_time < end_record:
		time.sleep(delay)
		second_request = bot.trades(symbol='BTCUSDT', limit = 300)

		#last_index_sec_req = len(second_request)	# номер последней строки +1
		num_str_sec_req = 0

		for string_sec_req in second_request:
			if test_string == string_sec_req:	#нахождение строки (2 list), на которой закончился прошлый запрос (1 list)
				num_str_sec_req += 1			#выставляем номер строки для начала записи (след. строка после обнаруженной)
				#itr = iter(num_list)
				range_for_record = second_request[num_str_sec_req:]
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