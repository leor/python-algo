'''
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
'''

from random import randint

length = int(input("Введите длину массива: "))
a = [randint(0, 99) for x in range(length)]

print("Исходный массив: ", a)

'''
Простое решение

min1 = min(a)
print("Первый минимальный элемент: %d" % min1)

a.remove(min1)
min2 = min(a)
print("Второй минимальный элемент: %d" % min2)
'''

# вариант с рекурсией
def find_mins(lst, count):
    if count > 0:
        min_val = min(lst)
        print("Минимальный элемент: %d" % min_val)
        lst.remove(min_val)

        find_mins(lst, count - 1)


find_mins(a, 2)
