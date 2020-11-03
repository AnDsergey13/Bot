import time
import threading

# list_timeframes = [5, 10, 15, 20, 30, 60, 180, 300, 900, 1800] #сек
# 180 с = 3 м, 300 с = 5 м, 900 с = 15 м, 1800 с = 30 м
list_timeframes = [10]

def acc(trade_):
	global trade
	trade = trade_ # !!!!!!!/
	global tr_1

	tr_1.append(trade)

def status_trade(value):
	global status
	status = value

def request_time_1(timeframe_1):
	response = time.time()
	time_pc = int(response * 1000)
	end_time = time_pc + timeframe_1 * 1000
	return end_time

def time_storage_1(timeframe_1):
	global tr_1

	while status == True:
		end_time = request_time_1(timeframe_1)

		while status == True:
			current_time = int(time.time() * 1000)
			if current_time > end_time:
				if tr_1 != []:
					processing_1(timeframe_1, tr_1)
				tr_1 = []
				break

			time.sleep(0.001)

def processing_1(timeframe_1, tr_1):
	global price_old_1
	# Интервал времени по binance
	time_start_unix = int(tr_1[0][0] / 1000)
	time_start = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(time_start_unix))

	price_start = tr_1[0][2]
	price_end = tr_1[-1][2]

	if price_start > price_end:
		force_price = (1 - (price_end / price_start)) * - 1
		force_price = format(force_price, '.8f')
	elif price_start < price_end:
		force_price = 1 - (price_start / price_end)
		force_price = format(force_price, '.8f')
		#.format(round(force_price, 6))
	else:
		force_price = 0

	volume_sell = 0
	volume_buy = 0
	volume_comm = 0
	for trade in tr_1:
		if 'SELL' in trade:
			volume_sell += trade[3]
		if 'BUY' in trade:
			volume_buy += trade[3]
		if 'BUY_' in trade:
			volume_comm += trade[3]
	try:
		symm_vol_buy = volume_buy + volume_comm
		if symm_vol_buy > volume_sell:
			force_vol = 1 - (volume_sell / symm_vol_buy)
			force_vol = format(force_vol, '.5f')
		elif symm_vol_buy < volume_sell:
			force_vol = (1 - (symm_vol_buy / volume_sell)) * - 1
			force_vol = format(force_vol, '.5f')
		else:
			force_vol = 0	
	except:
		force_vol = 0

	num_sell = 0
	num_buy = 0
	num_comm = 0
	for trade in tr_1: 
		num_sell += trade.count('SELL')
		num_buy += trade.count('BUY')
		num_comm += trade.count('BUY_')

	summ_num_buy = num_buy + num_comm
	if summ_num_buy > num_sell:
		force_num = 1 - (num_sell / summ_num_buy)
		force_num = format(force_num, '.5f')
	elif summ_num_buy < num_sell:
		force_num = (1 - (summ_num_buy / num_sell)) * - 1
		force_num = format(force_num, '.5f')
	else:
		force_num = 0

	price_old_1 = price_end
	# result = [ time_start, price_start, round(volume_buy, 2), round(volume_comm, 2), round(volume_sell, 2), force_base, num_buy, num_comm, num_sell]
	result = [time_start, force_price, force_vol, force_num]

	with open('%d.txt' % timeframe_1, 'a') as f:
		f.write(str(result) + '\n')
	print(result)

def main():
	global tr_1

	timeframe_1 = list_timeframes[0]

	time_st_1 = threading.Thread(target=time_storage_1, args=(timeframe_1,))
	time_st_1.start()

status = True

tr_1 = []

price_old_1 = 0