'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
'''

from timeit import timeit
from sys import setrecursionlimit


# Реализация на циклах
def with_loop():
    for i in range(2, 9):
        count = 0
        for j in range(2, 999):
            if j % i == 0:
                count += 1
    
        print("Найдено %d чисел кратных %d" % (count, i))


# рализация на "массивах"
def with_lists():
    for i in range(2, 9):
        print("Найдено %d чисел кратных %d" % (len({x for x in range(2, 999) if x % i == 0}), i))


# рекурсия
def with_recursion():
    def step(one, two=2, count=0):
        if two > 999:
            return count

        if two % one == 0:
            count += 1

        return step(one, two + 1, count)

    for i in range(2, 9):
        print("Найдено %d чисел кратных %d" % (step(i), i))


setrecursionlimit(10000)
wlp_time = timeit("with_loop()", setup="from __main__ import with_loop", number=100)
wls_time = timeit("with_lists()", setup="from __main__ import with_lists", number=100)
wr_time = timeit("with_recursion()", setup="from __main__ import with_recursion", number=100)

# среднее время для списка 2-999 составляет 0.154
print("Time with loop: %s" % wlp_time)
# среднее время для списка 2-999 составляет 0.194
print("Time with lists: %s" % wls_time)
# среднее время для списка 2-999 составляет 1.131
print("Time with recursion: %s" % wr_time)

'''
Результат анализа: 

- Наименьшую эффективность на длинных списках имеет рекурсивная реализация, 
т.к. дополнительное время уходит на вызов вложенной функции.
Сложность рекурсивного алгоритма - O(n2)

- Реализация на простых циклах или списках примерно одинаковы по скорости работы
Сложность O(n)
'''
