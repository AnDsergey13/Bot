import General_accumulator

from websocket import create_connection
# import json
import time
import threading

# Когда сокеты зарываются, закрываем и проверку аккумулятора. Чтобы процесс не висел в памяти
def status_trade(value):
	global status
	status = value
	General_accumulator.status_trade(value)

# Сам аккумулятор
def acc(trade):
	global list_trades
	list_trades.insert(0, trade) # Запись в начало

def check_accumulator():
	global list_trades

	while status == True:
		# print(len(list_trades), status)
		if len(list_trades) == 0:
			time.sleep(0.001) # Время обновления проверки списка
			continue
		# https://docs.python.org/3/howto/sorting.html#sortinghowto
		# list_trades = sorted(list_trades, key=lambda list_trades: list_trades[0])

		trade = list_trades.pop() # Извлекаем последний элемент
		remove_unused(trade)

def main():
	global request_price

	n = 0
	while n < 10:
		try:
			request_price = create_connection("ws://127.0.0.1:13254")
			n = 10
			print("Accumulator_data_base - подключен")
		except:
			time.sleep(0.1)
			n += 1
			if n > 0:
				print("Внутренний сервер для Accumulator_data_base недоступен! Количество попыток подключения - %d" % n)
				if n > 10:
					return

	flow_check = threading.Thread(target=check_accumulator)
	flow_check.start()

# ОТЛИЧИЯ 
# Дёргаем нужные ключ-значения в словаре и записываем в список
def remove_unused(trade):
	time_of_transaction = int(trade['T'])
	name_pair = str(trade['s'])
	request_price.send("price_BNBUSDT")
	try:
		price = float(request_price.recv())
	except:
		# print("\n__Цена по паре {} - недоступна__\n".format(pair))
		price = 0
	# price = round(float(trade['p']), 8) # Сделать преобразование цены в один вид
	volume = round(float(trade['q']), 6)
	# volume_quote = round(price * volume, 9)

	buy_market = str(trade['m'])
	if buy_market == "True":
		market = "SELL"
	elif buy_market == "False":
		market = "BUY"
	
	# Изменить. Ошибка присваивания вылетит раньше, если шаблоны устрарели
	try:
		list_trade = [time_of_transaction, name_pair, price, volume, market]
		# list_trade = [time_of_transaction, name_pair, volume, market]
	except:
		print("Ошибка обработки данных в модуле Accumulator_data_base. Используемые шаблоны устарели")
		return

	general_view(list_trade)

def general_view(list_trade):
	# if list_trade[1] == "BNBUSDT":
	# 	print(list_trade)
	General_accumulator.acc(list_trade)
	# print(list_trade)

status = True

list_trades = []
list_trade = []