import json
import our_library
from binance_api import Binance

bot = Binance(
    API_KEY='qRmmGsVlut46jEAYV6oKu6QuvEOrKPkg5aflmYkgmvOglBBbVl0ixMn8u1pf82sc',
    API_SECRET='GGw5Rr5fan9JC1dIhfyQMM5JFR5riPgCcM9wCUOk5NkUDbBaARAajKPlqUi1gx9R'
)

#our_library.record_in_file('klines_in_csv', data)

'''
#выдёргивание выбранных значений из списка
data = bot.klines(symbol='BTCUSDT', interval='1m', limit=1)
data = data[0]
data2 = bot.klines(symbol='BTCUSDT', interval='1m', limit=1)
data2 = data2[0]
'''
'''
data = [1542639300000, '0.00133850', '0.00134130', '0.00132520', '0.00133480', '5438.50000000', 1542639359999, '7.24783883', 148, '225.36000000', '0.30115747', '0']
data2 = [1542639300000, '0.00133950', '0.00134250', '0.00130220', '0.00131580', '5460.75000000', 1542639359999, '9.53983883', 196, '250.37000000', '0.30125347', '0']
data3 = []
for m in range(len(data)):
	i = float(data[m])
	j = float(data2[m])
	data3.append(j-i)
print("выполнено")
print(data3)
'''
'''
for i in range(10):
	print(bot.time('serverTime'))
'''
'''
def filt_klines(data):
	data = bot.klines(symbol='BTCUSDT', interval='1m', limit=1)
	data = data[0]
	return data
'''
'''
print("Cинхронизация прошла успешно")
data = bot.klines(symbol='BTCUSDT', interval='1m', limit=1)
data = data[0]
time_next = int(data[0])+5000	#+5 секунд к нижней границе

sinxron()

print("Прошло 5 секунд, и запись объёмов")
data = bot.klines(symbol='BTCUSDT', interval='1m', limit=1)
data = data[0]
time_next = int(data[0])+10000	#+10 секунд к нижней границе

sinxron()

print("Прошло 10 секунд, и запись объёмов")
data = bot.klines(symbol='BTCUSDT', interval='1m', limit=1)
data = data[0]
time_next = int(data[0])+15000	#+15 секунд к нижней границе

sinxron()

print("Прошло 15 секунд, и запись объёмов")
'''


shift_time_in_klines = [
	[0 , 5000],
	[0 , 10000],
	[0 , 15000],
	[0 , 20000],
	[0 , 25000],
	[0 , 30000],
	[0 , 35000],
	[0 , 40000],
	[0 , 45000],
	[0 , 50000],
	[0 , 55000]
]

sinx_klines_time = [6 , 1]

def request_time(time_check):
	time_check = bot.time()
	time_check = int(time_check['serverTime'])
	#print("модуль request_time выполнен")
	return time_check

def request_klines(data):
	data = bot.klines(symbol='BTCUSDT', interval='1m', limit=1)
	data = data[0]
	#print("модуль request_klines выполнен")
	return data

def market_forces(rec, force):
	#price_moment = rec[1]
	value_BTC = rec[2]
	value_BTC2 = rec[3]
	#force = (price_moment*value_BTC)/value_USDT
	force = value_BTC/value_BTC2
	return force

def formation_list(time_check, data):
	rec = []				#???
	force = 1

	time_check = request_time(time_check)
	data = request_klines(data)
	rec.append(time_check)			#запись времени			(0)
	rec.append(round(float(data[4]), 2))	#запись цены	(1)
	rec.append(float(data[5]))				#запись объёмов в BTC 	(2)
	rec.append(float(data[9]))
	rec.append(float(data[7]))				#запись объёмов в USDT	(3)
	
	rec.append(float(data[10]))
	rec.append(data[8])				#общее количество транзакций за временной промежуток	(4)

	force = market_forces(rec, force)
	rec.append(round(force, 5))		#сила рынка 			(5)
	second = shift_time_in_klines[i][1]
	#rec.append(str(second/1000)+ " cекунд")
	print("{0} секунд прошло с начала свечи".format(int(second/1000)))
	print(rec)
	
	#test_data.write("{0} секунд прошло с начала свечи".format(str(second/1000)))
	#test_data.write("\n")
	test_data.write(str(rec))
	test_data.write("\n")
	
	del rec

def check(time_check, time_next, data, i):	#сверка заданного временного промежутка с временем биржи
	while 1:					
		time_check = request_time(time_check)
		print("{0} {1}".format(time_next, time_check))
		if time_check > time_next:
			#print ("Выход из цикла")
			break
		#print ("Внутри цикла")
		continue
	formation_list(time_check, data)

data = []
time_check = {}
i = 0

data = request_klines(data)
test_data = open("test_data.txt", "w")
#shift_in_klines[i][1] #номер позиции
time_next = int(data[sinx_klines_time[0]])+sinx_klines_time[1]
check(time_check, time_next, data, i)
for t in range(10): # 10 минут записи
	for i in range(len(shift_time_in_klines)):
		data = request_klines(data)
		time_next = int(data[shift_time_in_klines[i][0]])+shift_time_in_klines[i][1]	#условие перехода
		check(time_check, time_next, data, i)

test_data.close()
print("Запись завершина. файл закрыт")

#!time_check = request_time(time_check)

'''
for i in range(12): #каждую итерацию последовательно выдёргиваем значения из словоря 
	data = bot.klines(symbol='BTCUSDT', interval='1m', limit=1)
	data = data[0]
	#shift_in_klines[i][1] #номер позиции
	time_next = int(data[shift_in_klines[i][0]])+shift_in_klines[i][1]	#условие перехода
	sinxron()
	
	#print("Уровень = {}".format(shift_in_klines[i][1]))
'''