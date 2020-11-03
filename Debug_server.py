import Socket_connection

from websocket import create_connection
import sys
import os
import threading

class debug():

	def send_message(message):
		try:
			red.send(message)
		except:
			print("Сервер отключён. Невозможно отправить сообщение!")
			sys.exit()

	def help():
		print('''
test - Проверка работоспособности сервера
close - Завершить работу сервера вручную
exit - Закрыть клиент отладки
numcl - Количество подключенных клиентов к серверу 
kill - Убивает процесс python.exe и его потомки
price - Запрос цены по паре

price close - Закрываем запросы по цене
thinfo - Информация о потоках на сервере
th close - Завершение потоков вручную
		''')

list_commands = ["test","close","exit","help","numcl","kill","price","thinfo", "price close", "th close"]

try:
	red = create_connection("ws://127.0.0.1:13254")
except:
	print("Сервер ws://127.0.0.1:13254 не запущен!")
	sys.exit()

print("***Debug_open***")
while True:
	message = input("Введите комнаду: ")

	if message not in list_commands:
		print("Комадны нет в списке. Чтобы посмотреть список введите: help")
		continue

	if message == "help":
		debug.help()
		continue

	if message == "exit":
		red.close()
		break

	if message == "kill":
		os.system("taskkill /im python.exe /f")

	if message == "price":
		pair = input("Введите пару: ")
		# print(message + pair)
		debug.send_message(message + "_" + pair)
		print(red.recv())
		continue

	if message == "price close":
		debug.send_message(message)
		print(red.recv())
		continue

	if message == "numcl":
		debug.send_message(message)
		print(red.recv())
		continue

	if message == "thinfo":
		debug.send_message(message)
		print(red.recv())
		continue
	
	if message == "th close":
		Socket_connection.close_module(False)

	if message == "close":
		debug.send_message(message)
		red.close()
	else:
		debug.send_message(message)
		print(red.recv())

print("***Debug_close***")