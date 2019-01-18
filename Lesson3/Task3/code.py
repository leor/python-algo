'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

from random import randint

length = int(input("Введите длину массива: "))
a = [randint(1, 99) for x in range(length)]

print("Исходный массив: ", a)
'''
Вариант на цикле

min_index = 0
min_el = 0
max_index = 0
max_el = 0

for i in range(length):
    if a[i] > max_el:
        max_el, max_index = (a[i], i)

    if min_el == 0 or a[i] < min_el:
        min_el, min_index = (a[i], i)

'''

# Вариант на списке
min_index = a.index(min(a))
max_index = a.index(max(a))
a[min_index], a[max_index] = a[max_index], a[min_index]

print("Изменённый массив: ", a)
