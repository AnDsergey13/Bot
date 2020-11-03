import Request_currency_endings
import Paths_for_price_requests
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

def preparatory_data():
	global ends
	global ends_with_underline
	global list_pairs
	ends_with_underline = Request_currency_endings.main(underline=True)

	ends = Request_currency_endings.main(underline=False)
	list_pairs = Paths_for_price_requests.launch(ends, only_pairs=True)
	# print(ends)
	# print(ends_with_underline)
	# print(list_pairs)

def main():
	global request_price

	n = 0
	while n < 10:
		try:
			request_price = create_connection("ws://127.0.0.1:13254")
			n = 10
			print("Accumulator_data_other - подключен")
		except:
			time.sleep(0.1)
			n += 1
			if n > 0:
				print("Внутренний сервер для Accumulator_data_other недоступен! Количество попыток подключения - %d" % n)
				if n > 10:
					return

	preparatory_flow = threading.Thread(target=preparatory_data)
	preparatory_flow.start()
	preparatory_flow.join()

	flow_check = threading.Thread(target=check_accumulator)
	flow_check.start()

# ОТЛИЧИЯ 
# Дёргаем нужные ключ-значения в словаре и записываем в список
def remove_unused(trade):
	time_of_transaction = int(trade['T'])
	name_pair = str(trade['s']) + "_"	# нижнее подчёркивание служит маркером конца строки
	price = round(float(trade['p']), 8) # Сделать преобразование цены в один вид
	volume = round(float(trade['q']), 6)
	volume_quote = round(price * volume, 9)

	buy_market = str(trade['m'])
	if buy_market == "True":
		market = "BUY_"
	elif buy_market == "False":
		market = "BUY_"

	# list_trade = [time_of_transaction, name_pair, "p = " + str(price), "v = " + str(volume), "p*v = " + str(volume_quote), market]
	# Изменить. Ошибка присваивания вылетит раньше, если шаблоны устрарели
	try:
		list_trade = [time_of_transaction, name_pair, volume_quote, market]
	except:
		print("Ошибка обработки данных в модуле Accumulator_data_other. Используемые шаблоны устарели")
		return

	general_view(list_trade)

# Функции pair_for_price и check_list_pairs, ищут пару для конвертации, основываясь только на название пары (сделки)
def check_list_pairs(currency):
	for pair in list_pairs:
		if currency in pair:
			return pair

def pair_for_price(name_pair):
	for currency_ in ends_with_underline:
		presence = name_pair.find(currency_)
		if presence > 0:
			currency = currency_.replace("_", "")
			pair = check_list_pairs(currency)
			# print(name_pair, currency)
			break
	return pair

def general_view(list_trade):
	name_pair = list_trade[1]
	pair = pair_for_price(name_pair)
	list_trade.insert(3, pair)

	request_price.send("price_" + pair)
	try:
		price = float(request_price.recv())
	except:
		print("\n__Цена по паре {} - недоступна__\n".format(pair))
		price = 0

	request_price.send("price_BNBUSDT")
	try:
		price_BNBUSDT = float(request_price.recv())
	except:
		# print("\n__Цена по паре {} - недоступна__\n".format(pair))
		price_BNBUSDT = 0

	list_trade.insert(4, price)

	presence = pair.find(CURRENCY)
	if presence == 0:
		volume_in_CURRENCY = list_trade[2] / price
		list_trade.insert(5, volume_in_CURRENCY)
	elif presence > 0:
		volume_in_CURRENCY = list_trade[2] * price
		list_trade.insert(5, volume_in_CURRENCY)
	volume_in_commission = round((list_trade[5] / 100) * СOMMISSION_PERCENTAGE, 8 )
	list_trade.insert(6, volume_in_commission)

	name_pair = list_trade[1].replace("_", "")
	# null_price = '-'
	list_trade = [list_trade[0], name_pair, price_BNBUSDT, list_trade[6], list_trade[7]]
	# time, pair, volume_commission, market
	General_accumulator.acc(list_trade)

status = True
CURRENCY = "BNB"
СOMMISSION_PERCENTAGE = 0.075 

list_trades = []
list_trade = []