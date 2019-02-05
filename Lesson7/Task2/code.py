"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
"""


import random


def merge_sort(a):
    if len(a) > 1:
        mid = len(a)//2

        left = merge_sort(a[mid:])
        right = merge_sort(a[:mid])

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1

    return a


lst = [random.randint(0, 50) for i in range(50)]
print("Исходный массив: ", lst)
print("Отсортированный массив: ", merge_sort(lst))
