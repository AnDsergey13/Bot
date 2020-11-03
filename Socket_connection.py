import Interface
import Accumulator_data_base
import Accumulator_data_quote
import Accumulator_data_other


from websocket import create_connection
import json
import time
import threading
import sys

def close_module(reception):
	Accumulator_data_base.status_trade(reception)
	Accumulator_data_quote.status_trade(reception)
	Accumulator_data_other.status_trade(reception)

	# Закрытие сервера
	try:
		red = create_connection("ws://127.0.0.1:13254")
		red.send("close")
		red.close()
	except:
		sys.exit()

# Параллельный поток для приёма данных с биржи
def client_binance(x, type_wb):
	while True:
		try:
			response = globals()["wb_{}_{}".format(x, type_wb)].recv()
		except:
			print("Binance перестал присылать сделки по пути {} в {}".format(x, type_wb))
			close_module(reception)

		if reception == True:
			trade = json.loads(response)
			# print(trade)
			if type_wb == "base":
				Accumulator_data_base.acc(trade)
				# print(trade)
			if type_wb == "quote":
				Accumulator_data_quote.acc(trade)
				# print(trade)
			if type_wb == "other":
				Accumulator_data_other.acc(trade)
				# print(trade)
		else:
			globals()["wb_{}_{}".format(x, type_wb)].close()
			print("Closed wb_{}, {}".format(x, type_wb))
			close_module(reception)
			break

def create(path, x, type_wb):
	global reception

	# Подключаемся к бирже
	try:
		globals()["wb_{}_{}".format(x, type_wb)] = create_connection(path)
	except:
		print("Не подключился к binance")
		print("Socket_connection -> create")
		reception = False
		close_module(reception)
		return

	locals()["flow_wb_binance_%d" % x] = threading.Thread(target=client_binance, args=(x, type_wb,))

	# Отправляем запрос на my_сервера о готовноти приёма данных с биржи
	try:
		locals()["my_wb_{}_{}".format(x, type_wb)] = create_connection("ws://127.0.0.1:13254")
		locals()["my_wb_{}_{}".format(x, type_wb)].send("Time for all")
	except:
		print("Сервер недоступен для подключения!")
		print("Socket_connection -> create")
		reception = False
		close_module(reception)
		return

	# Клиент принимает от my_сервера 
	end_time = int(locals()["my_wb_{}_{}".format(x, type_wb)].recv())
	locals()["my_wb_{}_{}".format(x, type_wb)].close()

	locals()["flow_wb_binance_%d" % x].start()

	while True:
		time_response = time.time()
		time_pc = int(time_response * 1000)
		if time_pc >= end_time:
			reception = False
			break

		time.sleep(0.01) # Чтобы не подвисали остальные процессы

def main(dict_path, type_wb):
	global reception
	reception = True

	min_num_path = min(dict_path.keys())
	max_num_path = max(dict_path.keys())

	#Генерирование потоков = количеству путей в словаре
	for x in range(min_num_path, max_num_path+1):
		locals()["thread%d" % x] = threading.Thread(target=create, args=(dict_path[x], x, type_wb,))
		locals()["thread%d" % x].start()

