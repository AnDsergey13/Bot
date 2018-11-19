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

shift_in_klines = (
	(6 , 1),
	(0 , 5000),
	(0 , 10000),
	(0 , 15000),
	(0 , 20000),
	(0 , 25000),
	(0 , 30000),
	(0 , 35000),
	(0 , 40000),
	(0 , 45000),
	(0 , 50000),
	(0 , 55000)
)

def sinxron():	#синхронизация двух методов
	while 1:					
		time_check = bot.time()
		time_check = int(time_check['serverTime'])
		print("{0} {1}".format(time_next, time_check))
		if time_check > time_next:
			print ("Выход из цикла")
			break
		print ("Внутри цикла")
		continue

for i in range(12): #каждую итерацию последовательно выдёргиваем значения из словоря 
	#filt_klines(data) 
	print(i)
	data = bot.klines(symbol='BTCUSDT', interval='1m', limit=1)
	data = data[0]
	der = shift_in_klines[i]
	
	print(der)
	'''
	time_next = int(data[shift_in_klines.get(i)])+shift_in_klines.values(i)
	sinxron()
	
	print("Уровень = {}".format(shift_in_klines.value(i)))
	'''