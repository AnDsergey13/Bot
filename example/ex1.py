from ex2 import sqr
from ex3 import root

#def summ1():
#	print("код в ex1 - выполнен. Вызов из ex2 успешно прошёл")

i = int(input("Введите число: "))
s = sqr(i)
k = root(i)
print("Квадрат числа {0} будет равен {1}".format(i, s))
print("Корень числа {0} будет равен {1:.50}".format(i, k))