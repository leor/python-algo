'''
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''

a = input("Введите натуральное число: ")
odds = 0
evens = 0

for i in a:
    if int(i) % 2 == 0:
        evens += 1
    else:
        odds += 1

print("В числе %d всего %d цифр, из которых %d чётных и %d нечётных" % (int(a), len(a), evens, odds))