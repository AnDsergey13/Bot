from ex5_2 import rug

i = 1

while 1: # бесконечный цикл # действие повторяется пока условие истинно
	num = input("Введите число от 0 до 100: ")
	if num == "s":
		break
	num = int(num)

	if num >= 0 and num <= 100:
		while 1: 
			num += 1
			print(num)
			if num > 20:
				print("Слишком быстро!")
				break
			'''if num > 40:
			pass
			print("Слишком быстро!")'''
	else:
		rug(i)
		i += 1 # счётчик