import Timeframe

from websocket import create_connection
import json
import time
import threading
import requests

# Когда сокеты зарываются, закрываем и проверку аккумулятора. Чтобы процесс не висел в памяти
def status_trade(value):
	global status
	status = value
	Timeframe.status_trade(value)

# Сам аккумулятор
def acc(trade):
	global list_trades
	list_trades.insert(0, trade) # Запись в начало

def check_accumulator():
	global list_trades

	while status == True:
		if len(list_trades) == 0:
			time.sleep(0.001) # Время обновления проверки списка
			continue

		trade = list_trades.pop() # Извлекаем последний элемент
		remove_unused(trade)

def main():
	flow_check = threading.Thread(target=check_accumulator)
	flow_check.start()

def remove_unused(trade):
	global old_time

	# new_time = trade[0]
	# if old_time > new_time:
	# 	print("____{t}____".format(t=old_time-new_time))
	# old_time = new_time

	# pc_time = int(time.time() * 1000)
	# delta_time = pc_time - old_time
	# trade.append(delta_time)
	# if trade[1] == "BNBUSDT":
		# Timeframe.acc(trade)
	# print(trade)
	Timeframe.acc(trade)

# def general_view(list_trade):
	# print(list_trade)

status = True

list_trades = []
# list_trade = []
# old_time = 0