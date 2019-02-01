"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

from memory_profiler import profile
from random import randint


# Простое решение
@profile
def simple(length):
    a = [randint(0, 99) for x in range(length)]

    # print("Исходный массив: ", a)

    min1 = min(a)
    print("Первый минимальный элемент: %d" % min1)

    a.remove(min1)
    min2 = min(a)
    print("Второй минимальный элемент: %d" % min2)


# вариант с рекурсией
@profile
def find_mins(lst, count):
    if count > 0:
        min_val = min(lst)
        print("Минимальный элемент: %d" % min_val)
        lst.remove(min_val)

        find_mins(lst, count - 1)

@profile
def rec(length):
    a = [randint(0, 99) for x in range(length)]

    # print("Исходный массив: ", a)

    find_mins(a, 2)


"""
Filename: code1.py

Line #    Mem usage    Increment   Line Contents
================================================
    26     13.1 MiB     13.1 MiB   @profile
    27                             def find_mins(lst, count):
    28     13.1 MiB      0.0 MiB       if count > 0:
    29                                     min_val = min(lst)
    30                                     print("Минимальный элемент: %d" % min_val)
    31                                     lst.remove(min_val)
    32                             
    33                                     find_mins(lst, count - 1)


Filename: code1.py

Line #    Mem usage    Increment   Line Contents
================================================
    26     13.1 MiB     13.1 MiB   @profile
    27                             def find_mins(lst, count):
    28     13.1 MiB      0.0 MiB       if count > 0:
    29     13.1 MiB      0.0 MiB           min_val = min(lst)
    30     13.1 MiB      0.0 MiB           print("Минимальный элемент: %d" % min_val)
    31     13.1 MiB      0.0 MiB           lst.remove(min_val)
    32                             
    33     13.1 MiB      0.0 MiB           find_mins(lst, count - 1)


Filename: code1.py

Line #    Mem usage    Increment   Line Contents
================================================
    26     13.1 MiB     13.0 MiB   @profile
    27                             def find_mins(lst, count):
    28     13.1 MiB      0.0 MiB       if count > 0:
    29     13.1 MiB      0.1 MiB           min_val = min(lst)
    30     13.1 MiB      0.0 MiB           print("Минимальный элемент: %d" % min_val)
    31     13.1 MiB      0.0 MiB           lst.remove(min_val)
    32                             
    33     13.1 MiB      0.0 MiB           find_mins(lst, count - 1)


Filename: code1.py

Line #    Mem usage    Increment   Line Contents
================================================
    35     12.4 MiB     12.4 MiB   @profile
    36                             def rec(length):
    37     13.0 MiB      0.0 MiB       a = [randint(0, 99) for x in range(length)]
    38                             
    39                                 # print("Исходный массив: ", a)
    40                             
    41     13.1 MiB      0.1 MiB       find_mins(a, 2)


Оба алгоритма работают с одинаковым потреблением памяти (по сути они идентичны)
Основной расход памяти идёт на хранение первоначального массива и поиск первого минимального элемента
"""
if __name__ == "__main__":
    length = int(input("Введите длину массива: "))

    simple(length)
    rec(length)
