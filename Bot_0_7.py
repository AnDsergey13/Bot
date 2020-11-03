import Path_for_websockets_BNB_base
import Path_for_websockets_BNB_quote
import Path_for_websockets_other
import Interface
import Accumulator_data_base
import Accumulator_data_quote
import Accumulator_data_other
import General_accumulator
import Timeframe

import threading

x = [
	{"name_module" : "Path_for_websockets_BNB_base", "name_flow" : "base"},
	{"name_module" : "Path_for_websockets_BNB_quote", "name_flow" : "quote"},
	{"name_module" : "Path_for_websockets_other", "name_flow" : "other"},
	{"name_module" : "___", "name_flow" : "read_base"},
	{"name_module" : "___", "name_flow" : "read_quote"},
	{"name_module" : "___", "name_flow" : "read_other"}
]

# Общий класс-шаблон для функций (использовать словарь, для передачи объектов)
class Flow():
	pass

def flow_read_base():
	Accumulator_data_base.main()
	pass

def flow_read_quote():
	Accumulator_data_quote.main()
	pass

def flow_read_other():
	Accumulator_data_other.main()
	pass

def flow_base(CURRENCY):
	name_flow = "base"
	Path_for_websockets_BNB_base.main(CURRENCY, name_flow)
	
def flow_quote(CURRENCY):
	name_flow = "quote"
	Path_for_websockets_BNB_quote.main(CURRENCY, name_flow)

def flow_other(CURRENCY):
	name_flow = "other"
	Path_for_websockets_other.main(CURRENCY, name_flow)

def interface(OPERATING_TIME):
	Interface.main(OPERATING_TIME)
	pass

def gen_accumulator():
	General_accumulator.main()
	pass

def TF():
	Timeframe.main()
	pass

def statistics_collection():
	# for timeframe in LIST_TIMEFRAMES:
		# time_frame = threading.Thread(target=TF, args=(timeframe,))
		# time_frame.start()
		# print(threading.current_thread().name)
		# print(threading.active_count())
		# print(threading.current_thread())
		# print(threading.get_ident())
		# print(threading.enumerate())
		# print(threading.stack_size())
	# print(threading.enumerate())
	# Timeframe.status_trade(value=False)
	time_frame = threading.Thread(target=TF)
	time_frame.start()

	gen_acc = threading.Thread(target=gen_accumulator)
	gen_acc.start()
	# https://docs.python.org/3.7/library/threading.html
	control = threading.Thread(target=interface, args=(OPERATING_TIME,))
	# name как передать??? https://www.youtube.com/watch?v=_2t9ohh1RCg
	base = threading.Thread(target=flow_base, args=(CURRENCY,))
	quote = threading.Thread(target=flow_quote, args=(CURRENCY,))
	other = threading.Thread(target=flow_other, args=(CURRENCY,))

	read_base = threading.Thread(target=flow_read_base)
	read_quote = threading.Thread(target=flow_read_quote)
	read_other = threading.Thread(target=flow_read_other)

	control.start()
	base.start()
	quote.start()
	other.start()
	read_base.start()
	read_quote.start()
	read_other.start()

CURRENCY = "BNB"
OPERATING_TIME = 60 # пока в секундах
# LIST_TIMEFRAMES = [5, 10, 15, 20, 30, 60, 180, 300, 900, 1800] 
# LIST_TIMEFRAMES = [5, 10, 15] 
statistics_collection()