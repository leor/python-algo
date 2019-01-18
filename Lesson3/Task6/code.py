'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''

from random import randint

length = int(input("Введите длину массива: "))
a = [randint(0, 99) for x in range(length)]

print("Исходный массив: ", a)

min_index = a.index(min(a))
max_index = a.index(max(a))

b = a[min_index+1:max_index] if min_index < max_index else a[max_index+1:min_index]
print("Список между минимальным и максмальным элементами: ", b)
print("Сумма фильтрованного списка: %d" % sum(b))
