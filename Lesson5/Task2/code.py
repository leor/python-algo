"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections
import functools

nums = collections.defaultdict(list)
for d in range(2):
    n = input("Введите %d-е натуральное шестнадцатиричное число: " % (d+1))
    nums["%s-%s" % (d, n)] = list(n)

sum = sum([int(''.join(i), 16) for i in nums.values()])
print("Сумма: ", list('%X' % sum))

mult = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in nums.values()])
print("Произведение: ", list('%X' % mult))
