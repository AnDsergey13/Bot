from binance_api import Binance
import pdb
#pdb.set_trace()

bot = Binance(
    API_KEY='',
    API_SECRET=''
)

#first_request = bot.trades(symbol='BTCUSDT', limit = 5)
#print (first_request)

new_list = []

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

new_list = first_request
last_index_sec_req = len(second_request)	# номер последней строки +1
#print (last_index_sec_req)
test_string = first_request[-1]

#pdb.set_trace()		#Отладчик

num_str_sec_req = 0
for string_sec_req in second_request:
	if test_string == string_sec_req:	#нахождение строки (2 list), на которой закончился прошлый запрос (1 list)
		num_str_sec_req += 1			#выставляем номер строки для начала записи (след. строка после обнаруженной)
		diapaz = second_request[num_str_sec_req:last_index_sec_req]
		print (diapaz)
		new_list.append(diapaz)
		break
	num_str_sec_req += 1

print(new_list)

'''
for num1 in first_request:
	for num2 in second_request:
		if num1 == num2:
			new_list.append(num2)
			print("Запись")
		else:
			continue'''

