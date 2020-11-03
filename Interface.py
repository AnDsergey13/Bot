import Paths_for_price_requests
import Request_currency_endings
import Socket_connection

from websocket_server import WebsocketServer
# from websocket_server import API
# import websocket_server

import json
import time
import requests
import threading

# # Модификация библиотеки websocket_server. Создана для закрытия сервера
# class modified(API):
# 	def server_complete(self):
# 		self.server_close()
# 		print("Server complete.")


def wb_price_BNBUSDT():
	while True:
		global price_BNBUSDT
		if exit == True:
			break
		response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT")
		response = json.loads(response.text)
		price_BNBUSDT = str(response['price'])
		# print(price_BNBUSDT)
		time.sleep(0.6)

def requests_price(list_paths):
	while True:
		# Динамический список цен по парам. Сделан для уменьшения задержек со стороны сервера binance
		global current_price_pairs
		global exit
		for path in list_paths:
			if exit == True:	# Закрываем цикл, когда поступает сигнал о закрытии сервера
				break
			try:
				response = requests.get(path)
				dict_ = json.loads(response.text)
			except:
				# print(dict_)
				print("Interface -> requests_price ___Остутствие подключение к binance. Проверьте соединение с интернетом")
				Socket_connection.close_module(False)
			try: # Если binance вернёт ошибку, то сработает исключение
				name_pair = dict_["symbol"]
				price = dict_["price"]
				current_price_pairs[name_pair] = price
			except:
				print(dict_)
				print("Interface -> requests_price __Ошибка обработки данных в словаре")
				Socket_connection.close_module(False)
			time.sleep(0.6) # Ставим приемлемую задержку, чтобы binance не заблокировал запросы
		# print(current_price_pairs)
		if exit == True:
			# print("Обновление цен - остановлено!")
			break

def run_time():
	response = time.time()
	time_pc = int(response * 1000)
	end_time = time_pc + OPERATING_TIME * 1000
	end_time = str(end_time) # Преобразование необходимо так как сервер отправляет данные клиентам в типе "строка"
	return end_time

# Эта фукция определяет сколько wb вообще будет подключатся
def counting_the_path(dict_path):
	global num_wb

	max_num_path = max(dict_path.keys())
	num_wb += max_num_path
	#print(num_wb)

def time_for_all(client, server):
	global list_clients
	
	# Наполняем список клинтов, до тех пор, пока не подключатся все
	# метод send_message_to_all - НЕ ИСПОЛЬЗОВАТЬ. Не всем клиентам рассылает сообщения
	if len(list_clients) < num_wb:
		list_clients.insert(0, client)

	if len(list_clients) == num_wb:
		for client_ in list_clients:
			server.send_message(client_, run_time())
		list_clients = []

def listening_to_messages(client, server, message):
	global list_clients
	global exit

	if message == "Time for all":
		time_for_all(client, server)

	if message == "Time for one":
		server.send_message(client, run_time())

	if "price_" in message: # пример: price_BNBUSDT 
		pair = message.replace("price_", "")
		# if pair == "BNBUSDT":
		# 	server.send_message(client, price_BNBUSDT)
		# else:
		# 	price = str(current_price_pairs.get(pair))
		# 	server.send_message(client, price)
		price = str(current_price_pairs.get(pair))
		server.send_message(client, price)

	# Debugging
	if message == "test":
		server.send_message(client, "Сервер работает")

	if message == "numcl":
		number_clients = len(server.clients)
		server.send_message(client, "Количество подключённых клиентов: %d" % number_clients
			)
	if message == "close":
		if exit == False:
			exit = True	# Закрываем цикл запроса цен
			print("Обновление цен - остановлено!")
		server.server_complete() # Отключение сервера 
		# ERROR: WebSocketsServer: [WinError 10038] Сделана попытка выполнить операцию на объекте, не являющемся сокетом . РЕШИТЬ!
	if message == "thinfo":
		a = threading.active_count()
		# b = threading.current_thread()
		# c = threading.get_ident()
		d = threading.enumerate()
		# e = threading.stack_size()
		# server.send_message(client, "{},\n {},\n {},\n {},\n {},\n".format(a,b,c,d,e))
		server.send_message(client, "Количество активных потоков - {},\n Список потоков - {}".format(a,d))

	if message == "price close":
		exit = True
		server.send_message(client,"Обновление цен - остановлено!")
		
def main(OPERAT_TIME):
	# WTF???
	global OPERATING_TIME
	OPERATING_TIME = OPERAT_TIME 

	ends = Request_currency_endings.main(underline=False)
	list_paths = Paths_for_price_requests.launch(ends, only_pairs=False)
	# Открываем параллельные потоки для запроса цен
	prices = threading.Thread(target=requests_price, args=(list_paths,))
	# fast_price = threading.Thread(target=wb_price_BNBUSDT)
	prices.start()
	# fast_price.start()

	server = WebsocketServer(13254, host='127.0.0.1')
	server.set_fn_message_received(listening_to_messages)
	server.run_forever()

# global OPERATING_TIME
num_wb = 0
list_clients = []
current_price_pairs = {}
exit = False
