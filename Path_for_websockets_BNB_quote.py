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
def removing_unnecessary_pairs(QUOTE_CURRENCY):
	verification_request = requests.get("https://api.binance.com/api/v1/exchangeInfo")
	verification_request = json.loads(verification_request.text)
	verification_request = verification_request['symbols']

	all_pairs_copy = all_pairs.copy()
	#print(len(all_pairs))
	for current_pair in verification_request:
		pair = current_pair['symbol']
		current_status_pair = current_pair['status']
		name_baseAsset = current_pair['baseAsset']
		name_quoteAsset = current_pair['quoteAsset']
		#print(pair, name_baseAsset, name_quoteAsset)

		# Удаляем неторгуемые пары и оставляем пары содержащие котируемую валюту bnb
		if current_status_pair != 'TRADING' or name_quoteAsset != QUOTE_CURRENCY:
			for del_dict in all_pairs_copy:
				name_del_pair = del_dict['symbol']
				if name_del_pair == pair:
					#print('Удаляем пару {}'.format(name_del_pair))
					all_pairs.remove(del_dict)

# Удаление ненужных пар ключ-значение в словаре
def deleting_keys_and_values():
	for current_pair in all_pairs:
		current_pair_copy = current_pair.copy()

		for key in current_pair_copy.keys():	
			if key != 'symbol' and key != 'quoteVolume':
				current_pair.pop(key)
	#print(len(all_pairs))

def convert_to_string(path_number, pair):	# way_pair - переименовать
	pair = "/{}@aggTrade".format(pair)
	old_value = paths_for_websockets[path_number] 
	concatenation = old_value + str(pair)
	paths_for_websockets[path_number] = concatenation

# Сортировка от max до min по объёмам 	#https://docs.python.org/3.7/library/collections.html?highlight=ordereddict#collections.OrderedDict
def sorting_by_volume():
	way_pair = []	# Убрать переменную!!
	all_pairs_copy = all_pairs.copy()

	for current_pair in all_pairs_copy:	#дёргаем чисто объёмы и складываем в список
		quoteVolume = float(current_pair['quoteVolume']) 
		way_pair.append(quoteVolume)

	way_pair.sort(reverse=True)	# Сортируем от большого объёма к маленькому
	way_pair_copy = way_pair.copy()		#Копируем список, дабы при итерации удалять элементы из списка

	for current_pair in all_pairs_copy:	
		pair = current_pair['symbol']
		quoteVolume = float(current_pair['quoteVolume']) 

		for index_x_copy, volumes_of_sorted_pairs in zip(range(len(way_pair_copy)), way_pair_copy):	#Вставляем названия пар на место отсортированных объёмов
			if volumes_of_sorted_pairs == quoteVolume:
				way_pair.remove(volumes_of_sorted_pairs)
				way_pair.insert(index_x_copy, pair)

	sort_by_path(way_pair)

# Сортировка большого пути на мелкие	# Поменять коммент!
def sort_by_path(way_pair):
	path_number = 1
	for pair in way_pair:
		pair = pair.lower()
		if path_number >= number_of_paths_websockets+1:
			path_number = 1
		convert_to_string(path_number, pair)
		path_number += 1			

def gluing_paths():
	for path_number in range(1,number_of_paths_websockets+1):
		path_to_binance = paths_for_websockets[0] 
		current_way = paths_for_websockets[path_number]
		concatenation = path_to_binance + current_way
		paths_for_websockets[path_number] = concatenation
	del paths_for_websockets[0]

def main(QUOTE_CURRENCY, name_flow):
	global number_of_paths_websockets
	global main_query
	global all_pairs

	number_of_paths_websockets = 4

	main_query = requests.get("https://api.binance.com/api/v1/ticker/24hr")
	all_pairs = json.loads(main_query.text)

	generation_paths_for_websockets()
	removing_unnecessary_pairs(QUOTE_CURRENCY)
	deleting_keys_and_values()
	sorting_by_volume()
	gluing_paths()

	#print(paths_for_websockets)
	time.sleep(10) # Задержка, чтобы внутренний сервер успел обновить стакан цен
	Interface.counting_the_path(paths_for_websockets)
	Socket_connection.main(paths_for_websockets, name_flow)