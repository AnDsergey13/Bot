i = int(input("Введите число от 1 до 10: "))

for j in [1,2,3,4,5,6,7,8,9,10]:
	if j == i:
	#print(j**j, end = "_")
		j = j**(j**j)
		#print("{}".format(j))
		my_file = open('10^10^10.txt', 'w')
		my_file.write(str(j))
		my_file.close()

'''
else:
	print("Попробуйте ещё раз")


else:
	print("Вы ввели число{}".format())
'''