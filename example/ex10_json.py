import json
#не использовать модуль pickle!!!

data = [
	{'a' : 10,'b' : 20,'c' : 30},
	{'a' : 100,'b' : 200,'c' : 300},
	{'a' : 1000,'b' : 2000,'c' : 3000}
	]

print(type(data),data)

with open('data.json', 'w') as file:
	data = json.dumps(data)
	file.write(data)

print(type(data),data)


with open('data.json') as file:
	data = file.read()
	print(type(data),data)
	data = json.loads(data)

print(type(data),data)
print(data[2]['a'])

