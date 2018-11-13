def rug(i):
	if i == 1:
		print("число=1")
	elif i == 2:
		print("число=2")
	elif i == 3:
		print("число=3")
	elif i == 4:
		print("число=4")
	elif i == 5:
		print("число=5")
	elif i >= 6 and i < 8:
		print("число=6-8")
	elif i == 8:
		print("число=8 {0}".format(i))
	else:
		i = 1
		print ("Обновление списка. Число = {0}".format(i))
		return i