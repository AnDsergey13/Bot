import Socket_connection
import Interface

import time
import json
import requests

def generation_paths_for_websockets():
	global paths_for_websockets
	paths_for_websockets = dict((number+1, "") for number in range(number_of_paths_websockets))
	paths_for_websockets.update({0:'wss://stream.binance.com:9443/ws'})

# Удаляем словари, которые официально не торгуются на Binance
def removing_unnecessary_pairs():
	verification_request = requests.get("https://api.binance.com/api/v1/exchangeInfo")
	verification_request = json.loads(verification_request.text)
	verification_request = verification_request['symbols']

	all_pairs_copy = all_pairs.copy()
	for current_pair in verification_request:
		pair = current_pair['symbol']
		current_status_pair = current_pair['status']

		if current_status_pair != 'TRADING':	
			for del_dict in all_pairs_copy:
				name_del_pair = del_dict['symbol']
				if name_del_pair == pair:
					all_pairs.remove(del_dict)

# Выбираем из всех пар на бирже, только пары с BTC
def selecting_a_PAIR_from_pairs(CURRENCY):
	for current_pair in all_pairs:
		pair = current_pair['symbol']
		presence_of_a_pair = pair.find(CURRENCY)	

		if presence_of_a_pair == 0 or presence_of_a_pair > 0:	# 0 = Есть пара в начале, >1 = Есть пара в середине или в конце, -1 = Пара отсутствует в строке 
			list_with_PAIR.append(current_pair)

# Удаление ненужных пар ключ-значение в словаре
def deleting_keys_and_values():
	for current_pair in list_with_PAIR:
		current_pair_copy = current_pair.copy()

		for key in current_pair_copy.keys():	
			if key != 'symbol' and key != 'quoteVolume':
				current_pair.pop(key)
	#print(len(list_with_PAIR))

# Вырезание названия пар с базовой валютой, в новый список для отдельного вебсокета
def base_pairs_path(CURRENCY):		# сменить название
	way_pair = []
	list_with_PAIR_copy = list_with_PAIR.copy()

	for current_pair in list_with_PAIR_copy:
		pair = current_pair['symbol']
	
		presence_of_a_pair = pair.find(CURRENCY)

		if presence_of_a_pair  == 0:
			way_pair.append(pair)
			list_with_PAIR.remove(current_pair)

	parsing_way_pair(1, way_pair)

def parsing_way_pair(path_number, way_pair):
	for pair in way_pair:
		pair = pair.lower()		# https://docs.python.org/3.7/library/stdtypes.html#str.lower
		convert_to_string(path_number, pair)

def convert_to_string(path_number, pair):	# way_pair - переименовать
	pair = "/{}@aggTrade".format(pair)
	old_value = paths_for_websockets[path_number] 
	concatenation = old_value + str(pair)
	paths_for_websockets[path_number] = concatenation

def gluing_paths():
	for path_number in range(1,number_of_paths_websockets+1):
		path_to_binance = paths_for_websockets[0] 
		current_way = paths_for_websockets[path_number]
		concatenation = path_to_binance + current_way
		paths_for_websockets[path_number] = concatenation
	del paths_for_websockets[0]

def main(CURRENCY, name_flow):
	global number_of_paths_websockets
	global list_with_PAIR
	global main_query
	global all_pairs

	number_of_paths_websockets = 1
	list_with_PAIR = []	

	main_query = requests.get("https://api.binance.com/api/v1/ticker/24hr")
	all_pairs = json.loads(main_query.text)

	generation_paths_for_websockets()
	removing_unnecessary_pairs()
	selecting_a_PAIR_from_pairs(CURRENCY)
	deleting_keys_and_values()
	base_pairs_path(CURRENCY)
	gluing_paths()

	# print(paths_for_websockets)
	time.sleep(10) # Задержка, чтобы внутренний сервер успел обновить стакан цен
	Interface.counting_the_path(paths_for_websockets)
	Socket_connection.main(paths_for_websockets, name_flow)