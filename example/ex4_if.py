num = int(input("Введите число: "))
i = 0

def prt(num,i):
	print("Условие выполнено! Число равно {0}. Уровень {1}".format(num, i))
	i = 0
	return i

# конфигурация if выполняется для всех elif
if num < 5: #and num <= 50:
	prt(num,i)
	'''if num <= 11:
		i += 1
		prt(num,i)'''
elif num > 5 and num <= 15:
	i += 1
	prt(num,i)
elif num > 15 and num <= 30:
	i += 2
	prt(num,i)
else:
	i += 3
	prt(num,i)

