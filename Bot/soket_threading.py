import threading
import time
import requests

symbol = ['BTCUSD', 'BTCETH', 'BTCDGD', 'BNBUSDT']
#pair = ['BTC_LTC', 'BTC_ETH', 'BTC_USD']

def binance(symbol):
	local_start_time = time.time()
	try:
		requests.get("https://api.binance.com/api/v1/klines?symbol={symbol}&interval=1m&limit=1".format(symbol=symbol))
		#requests.get("https://api.exmo.com/v1/order_book/?symbol={symbol}&limit=1000".format(symbol=symbol))
	except Exception as e:
		print(e)
	print("Пара {symbol} на binance, время работы функции: {t:0.4f}".format(symbol=symbol, t=time.time()-local_start_time))

def exmo(symbol):
	local_start_time = time.time()
	try:
		#requests.get("https://api.binance.com/api/v1/klines?symbol={symbol}&interval=1m&limit=1".format(symbol=symbol))
		requests.get("https://api.exmo.com/v1/order_book/?pair={symbol}&limit=1000".format(symbol=symbol))
	except Exception as e:
		print(e)
	print("Пара {symbol} на exmo, время работы функции: {t:0.4f}".format(symbol=symbol, t=time.time()-local_start_time))


global_start_time = time.time()

threads = []
for symbol in symbol:
	# Подготавливаем потоки, складываем их в список
	threads.append(threading.Thread(target=binance, args=(symbol,)))
	threads.append(threading.Thread(target=exmo, args=(symbol,)))


# Запускаем каждый поток
for thread in threads:
	thread.start()

# Ждем завершения каждого потока
for thread in threads:
	thread.join()

				   
print('Общее время работы {s:0.4f}'.format(s=time.time()-global_start_time))

'''
a = 8
b = 13

def summ(a,b):
	try:
		s = a + b
	except Exception:
		print("код не верен")
	finally:
		#time.sleep(5)
		print(s)

def umn(a,b):
	try:
		u = a * b
	except Exception:
		print("код не верен")
	finally:
		#time.sleep(3)
		print(u)

mass = []

mass.append(threading.Thread(target=summ, args=(a, b)))
mass.append(threading.Thread(target=umn, args=(a, b)))

for znach in mass:
	znach.start()

for znach in mass:
	znach.join()

#print(s)
#print(u)'''

'''
from threading import Thread

def writer(filename, n):
	with open(filename, 'w') as inFile:
		for i in range(n):
			inFile.write(int(n))

t1 = Thread(target=writer, args=('test2.txt', 500,))
t2 = Thread(target=writer, args=('test3.txt', 500,))

t1.start()
t2.start()
t1.join()
t2.join()
'''