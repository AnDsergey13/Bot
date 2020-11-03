import json
import requests

def main(underline):
	currency_endings = []

	verification_request = requests.get("https://api.binance.com/api/v1/exchangeInfo")
	verification_request = json.loads(verification_request.text)
	all_pairs = verification_request['symbols']

	# запись всех пар в список
	for pair_dict in all_pairs:
		currency = pair_dict['quoteAsset']
		currency_endings.append(currency)

	currency_endings = set(currency_endings) # Обрезаем повторы благодаря перобразованию списка в множество
	currency_endings = list(currency_endings)# и обратно преобразуем в список
	currency_endings.sort()

	if underline == False:
		return currency_endings

	# Нужно для точного вычисления валюты в паре. Например: поиск по паре VETUSDT даёт, и TUSD, и USDT. Для того, что бы отсечь TUSD, поиск нужно проводить по паре VETUSDT_. В итоге будет только USDT_
	currency_endings_copy = currency_endings.copy()
	for ending in currency_endings_copy:	
		currency_endings.remove(ending)
		ending = ending + '_'
		currency_endings.append(ending)

	currency_endings.sort()

	return currency_endings