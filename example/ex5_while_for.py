from ex5_2 import rug
'''import pdb
pdb.set_trace() '''
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
	else:
		#print(rug(i))
		i = rug(i)
		i += 1 # счётчик
