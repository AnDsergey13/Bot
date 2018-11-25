from binance_api import Binance

bot = Binance(
    API_KEY='',
    API_SECRET=''
)

#first_request = bot.trades(symbol='BTCUSDT', limit = 5)
#print (first_request)

new_list = []

first_request = [
	{'a':1, 'b':2, 'c':3},
	{'a':2, 'b':3, 'c':4},
	{'a':3, 'b':4, 'c':5},
	{'a':4, 'b':5, 'c':6},
	{'a':5, 'b':6, 'c':7},
	]

second_request = [
	{'a':3, 'b':4, 'c':5},
	{'a':4, 'b':5, 'c':6},
	{'a':5, 'b':6, 'c':7},
	{'a':6, 'b':7, 'c':8},
	{'a':7, 'b':8, 'c':9},	
	]

new_list = first_request
#for i in first_request:
#num = 0

i = first_request[-1]

for j in second_request:
	
	if i == j:
		new_list.append(j)
		print(i)

print(new_list)

'''
for num1 in first_request:
	for num2 in second_request:
		if num1 == num2:
			new_list.append(num2)
			print("Запись")
		else:
			continue'''

