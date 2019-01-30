"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
"""
from memory_profiler import profile
from sys import setrecursionlimit


# Реализация на циклах
@profile
def with_loop():
    for i in range(2, 9):
        count = 0
        for j in range(2, 9999):
            if j % i == 0:
                count += 1

        print("Найдено %d чисел кратных %d" % (count, i))


# рализация на "массивах"
@profile
def with_lists():
    for i in range(2, 9):
        print("Найдено %d чисел кратных %d" % (len({x for x in range(2, 9999) if x % i == 0}), i))


# рекурсия
@profile
def with_recursion():
    def step(one, two=2, count=0):
        if two > 9999:
            return count

        if two % one == 0:
            count += 1

        return step(one, two + 1, count)

    for i in range(2, 9):
        print("Найдено %d чисел кратных %d" % (step(i), i))


"""
Найдено 4999 чисел кратных 2
Найдено 3332 чисел кратных 3
Найдено 2499 чисел кратных 4
Найдено 1999 чисел кратных 5
Найдено 1666 чисел кратных 6
Найдено 1428 чисел кратных 7
Найдено 1249 чисел кратных 8
Filename: code2.py

Line #    Mem usage    Increment   Line Contents
================================================
     9     10.5 MiB     10.5 MiB   @profile
    10                             def with_loop():
    11     10.5 MiB      0.0 MiB       for i in range(2, 9):
    12     10.5 MiB      0.0 MiB           count = 0
    13     10.5 MiB      0.0 MiB           for j in range(2, 9999):
    14     10.5 MiB      0.0 MiB               if j % i == 0:
    15     10.5 MiB      0.0 MiB                   count += 1
    16                             
    17     10.5 MiB      0.0 MiB           print("Найдено %d чисел кратных %d" % (count, i))


Найдено 4999 чисел кратных 2
Найдено 3332 чисел кратных 3
Найдено 2499 чисел кратных 4
Найдено 1999 чисел кратных 5
Найдено 1666 чисел кратных 6
Найдено 1428 чисел кратных 7
Найдено 1249 чисел кратных 8
Filename: code2.py

Line #    Mem usage    Increment   Line Contents
================================================
    21     10.5 MiB     10.5 MiB   @profile
    22                             def with_lists():
    23     11.2 MiB      0.0 MiB       for i in range(2, 9):
    24     11.2 MiB      0.5 MiB           print("Найдено %d чисел кратных %d" % (len({x for x in range(2, 9999) if x % i == 0}), i))


Найдено 4999 чисел кратных 2
Найдено 3333 чисел кратных 3
Найдено 2499 чисел кратных 4
Найдено 1999 чисел кратных 5
Найдено 1666 чисел кратных 6
Найдено 1428 чисел кратных 7
Найдено 1249 чисел кратных 8
Filename: code2.py

Line #    Mem usage    Increment   Line Contents
================================================
    28     11.2 MiB     11.2 MiB   @profile
    29                             def with_recursion():
    30     26.6 MiB      0.1 MiB       def step(one, two=2, count=0):
    31     26.6 MiB      0.0 MiB           if two > 9999:
    32     26.6 MiB      0.0 MiB               return count
    33                             
    34     26.6 MiB      0.0 MiB           if two % one == 0:
    35     26.6 MiB      0.0 MiB               count += 1
    36                             
    37     26.6 MiB      0.0 MiB           return step(one, two + 1, count)
    38                             
    39     19.4 MiB      0.0 MiB       for i in range(2, 9):
    40     19.4 MiB      0.0 MiB           print("Найдено %d чисел кратных %d" % (step(i), i))


- Решение на списках потребляет дополнительные 0.5 MiB памяти на использование генератора списка. 
  Очевидно, потому что для каждой итерации создаётся отдельный список и он занимает память
  
- Судя по расходу памяти, решение на рекурсии самое затратное. Не совсем понятно, почему инкремент указан небольшой, 
  а расход памяти увеличился сильно
  
- При попытке профилировать шаг рекурсии код повис, т.к. память закончилась
"""
if __name__ == "__main__":
    setrecursionlimit(100000)
    with_loop()
    with_lists()
    with_recursion()
