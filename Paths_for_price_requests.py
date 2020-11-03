import json
import requests

class main():
	# WTF???
	global CURRENCY
	CURRENCY = "BNB"

	def request():
		request = requests.get("https://api.binance.com/api/v1/exchangeInfo")
		request = json.loads(request.text)
		all_pairs = request['symbols']
		return all_pairs

	# Оставляем торгуемые пары
	def traded_pairs(all_pairs):
		all_pairs_copy = all_pairs.copy()
		for dict_pair in all_pairs_copy:
			if dict_pair['status'] != 'TRADING':
				all_pairs.remove(dict_pair)
		return all_pairs

	# Запись в список всех пар содержащие CURRENCY
	def record_in_list(all_pairs):
		list_pairs = []
		for dict_pair in all_pairs:
			if CURRENCY in dict_pair.values():
				# Записываем в строчном виде названия пар в список
				name_pair = dict_pair['symbol']
				name_pair = name_pair.lower()
				list_pairs.insert(0, name_pair)
		return list_pairs

	# мы уже нашли все пары содержащие CURRENCY, поэтому удаляем из ends
	def del_CURRENCY_from_ends(ends):
		if CURRENCY in ends:
			ends.remove(CURRENCY)
		return ends

	def del_pairs_from_ends(list_pairs, ends):
		list_pairs_copy = list_pairs.copy() 
		for name_pair in list_pairs_copy:
			del_pair = True	# Удаляем пару, если в ней нет валют из списка ends
			for currency in ends:
				currency = currency.lower()
				if currency in name_pair:
					del_pair = False

			if del_pair == True:
				list_pairs.remove(name_pair)
		return list_pairs

	def capital_letter(list_pairs):
		list_pairs_copy = list_pairs.copy()
		for name_pair in list_pairs_copy:
			list_pairs.remove(name_pair)
			name_pair = name_pair.upper()
			list_pairs.append(name_pair)
		return list_pairs

	# Создание путей для API запросов
	def create_paths(list_pairs):
		paths_price_requests = []
		for name_pair in list_pairs:
			url = "https://api.binance.com/api/v3/ticker/price?symbol="
			path = url + name_pair
			paths_price_requests.insert(0, path)
	
		return paths_price_requests

def launch(ends, only_pairs):
	if "_" in ends[0]:
		print("Ошибка! Подайте на вход launch() валюты БЕЗ нижнего подчёркивания!!!")
		return None
	all_pairs = main.request()
	all_pairs = main.traded_pairs(all_pairs)
	list_pairs = main.record_in_list(all_pairs)
	ends = main.del_CURRENCY_from_ends(ends)
	list_pairs = main.del_pairs_from_ends(list_pairs, ends)
	list_pairs_big = main.capital_letter(list_pairs)
	if only_pairs == True:
		return list_pairs_big
	paths = main.create_paths(list_pairs_big)
	return paths