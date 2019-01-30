"""
Написать два алгоритма нахождения i-го по счёту простого числа.
- Без использования «Решета Эратосфена»;
- Используя алгоритм «Решето Эратосфена»

"""

from memory_profiler import profile


@profile
def simple(i):
    count = 1
    # начинаем с 2, т.к. 1 не считается простым числом
    n = 2

    while count <= i:
        # print("Testing %d" % n)
        t = 1
        is_simple = True
        while t <= n:
            # print("Testing %d mod %d" % (n, t))
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break

            t += 1

        if is_simple:
            # print("%d is simple" % n)
            if count == i:
                break

            count += 1

        n += 1

    print("Искомое число %d" % n)


@profile
def eratosfen(i):
    n = 2

    # произвольное большое решето
    l = 10000
    sieve = [x for x in range(l)]
    # можно оптимизировать потребление памяти, перейдя на Boolean

    # 1 - не считается простым числом
    sieve[1] = 0

    while n < l:
        if sieve[n] != 0:
            m = n*2
            # можно оптимизировать, если начинать с элемента n^2 и двигаться шагами по n+(n-1)
            # т.е. для 2 - шаг 2 (2*1), для 3 - шаг 6 (3*2)
            while m < l:
                sieve[m] = 0
                m += n

        n += 1

    print("Искомое число %d" % [p for p in sieve if p != 0][i-1])


"""
Filename: code3.py

Line #    Mem usage    Increment   Line Contents
================================================
    11     10.3 MiB     10.3 MiB   @profile
    12                             def simple(i):
    13     10.3 MiB      0.0 MiB       count = 1
    14                                 # начинаем с 2, т.к. 1 не считается простым числом
    15     10.3 MiB      0.0 MiB       n = 2
    16                             
    17     10.3 MiB      0.0 MiB       while count <= i:
    18                                     # print("Testing %d" % n)
    19     10.3 MiB      0.0 MiB           t = 1
    20     10.3 MiB      0.0 MiB           is_simple = True
    21     10.3 MiB      0.0 MiB           while t <= n:
    22                                         # print("Testing %d mod %d" % (n, t))
    23     10.3 MiB      0.0 MiB               if n % t == 0 and t != 1 and t != n:
    24     10.3 MiB      0.0 MiB                   is_simple = False
    25     10.3 MiB      0.0 MiB                   break
    26                             
    27     10.3 MiB      0.0 MiB               t += 1
    28                             
    29     10.3 MiB      0.0 MiB           if is_simple:
    30                                         # print("%d is simple" % n)
    31     10.3 MiB      0.0 MiB               if count == i:
    32     10.3 MiB      0.0 MiB                   break
    33                             
    34     10.3 MiB      0.0 MiB               count += 1
    35                             
    36     10.3 MiB      0.0 MiB           n += 1
    37                             
    38     10.4 MiB      0.0 MiB       print("Искомое число %d" % n)
    
Filename: code3.py

Line #    Mem usage    Increment   Line Contents
================================================
    41     10.4 MiB     10.4 MiB   @profile
    42                             def eratosfen(i):
    43     10.4 MiB      0.0 MiB       n = 2
    44                             
    45                                 # произвольное большое решето
    46     10.4 MiB      0.0 MiB       l = 10000
    47     10.9 MiB      0.1 MiB       sieve = [x for x in range(l)]
    48                                 # можно оптимизировать потребление памяти, перейдя на Boolean
    49                             
    50                                 # 1 - не считается простым числом
    51     10.9 MiB      0.0 MiB       sieve[1] = 0
    52                             
    53     10.9 MiB      0.0 MiB       while n < l:
    54     10.9 MiB      0.0 MiB           if sieve[n] != 0:
    55     10.9 MiB      0.0 MiB               m = n*2
    56                                         # можно оптимизировать, если начинать с элемента n^2 и двигаться шагами по n+(n-1)
    57                                         # т.е. для 2 - шаг 2 (2*1), для 3 - шаг 6 (3*2)
    58     10.9 MiB      0.0 MiB               while m < l:
    59     10.9 MiB      0.0 MiB                   sieve[m] = 0
    60     10.9 MiB      0.0 MiB                   m += n
    61                             
    62     10.9 MiB      0.0 MiB           n += 1
    63                             
    64     11.0 MiB      0.0 MiB       print("Искомое число %d" % [p for p in sieve if p != 0][i-1])


- Решето Эратосфена потребляет больше памяти на хранение решета, в то же время, оно быстрее работает на больших числах
- Тест проведён для 100, где не видно прироста в скорости, но профилировать код на большем объёме не вышло
"""
if __name__ == "__main__":
    simple(100)
    eratosfen(100)
