import json
import time
import requests

status = True
print("Для выхода введите - 0")
responce = requests.get("https://api.binance.com/api/v1/time")
while True:
	if status == False:
		break
	num_seconds = int(input("Введите количество секунд в таймфрейме - "))
	if num_seconds == 0:
		break
	num_milliseconds = num_seconds * 1000
	time_binance = json.loads(responce.text)
	time_binance = time_binance['serverTime']
	pc_time = int(time.time() * 1000)
	delta = pc_time - time_binance
	inaccuracy = (delta * 100) / num_milliseconds
	probability = 100 - inaccuracy
	print("Задержка сервера Binance к вашему ПК, составляет %d mс" % delta)
	print("Вероятность усешной торговли на интервале {n} c равна {p}%".format(n=num_seconds, p=probability))
