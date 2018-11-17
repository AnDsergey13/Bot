def record_in_file(file_name, data):
	file_name = 'B_' + file_name + '.json'
	with open(file_name, 'w') as f:
		f.write(str(data))
		print('Данные записаны в файл')
		f.closed
