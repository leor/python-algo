"""
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
"""


import random


def bubble_sort_mod(a):
    r = a[:]

    for i in range(1, len(r)):
        count = 0
        for j in range(len(r)-i):
            if r[j] > r[j+1]:
                r[j], r[j+1] = r[j+1], r[j]
                count += 1

        if count == 0:
            print("All ready in %d iterations" % i)
            break

    return r


def bubble_sort(a):
    r = a[:]

    for i in range(1, len(r)):
        for j in range(len(r)-i):
            if r[j] > r[j+1]:
                r[j], r[j+1] = r[j+1], r[j]

    print("All ready in %d iterations" % i)

    return r


lst = [random.randint(-100, 100) for i in range(199)]
print("Исходный массив: ", lst)
print("Отсортированный массив: ", bubble_sort(lst))
print("Отсортированный массив: ", bubble_sort_mod(lst))
