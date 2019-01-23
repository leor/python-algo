'''
Написать два алгоритма нахождения i-го по счёту простого числа.
- Без использования «Решета Эратосфена»;
- Используя алгоритм «Решето Эратосфена»

Примечание ко всему домашнему заданию:
- Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
'''


import timeit


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


simple_time = timeit.timeit("simple(1000)", setup="from __main__ import simple", number=100)
eratosfen_time = timeit.timeit("eratosfen(1000)", setup="from __main__ import eratosfen", number=100)

print("Simple time = %s" % simple_time)
print("Seive time = %s" % eratosfen_time)

'''
Время работы алгоритмов для поиска 100го числа:
- простой - 0.419
- решето - 0.849

Время работы алгоритмов для поиска 1000го числа:
- простой - 53.97
- решето - 0.788

Из чего можно сделать вывод, что алгоритм решета Эратосфена выгден только для поиска больших элементов в больших списках.
Сложность простого алгоритма составляет O(n^2) - больше n - дольше работа
Сложность решета O(n log(log n)) - чем больше n, тем эффективнее алгоритм
'''
