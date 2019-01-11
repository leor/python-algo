import random

i1 = int(input("Введите начало диапазона для генерации целого числа: "))
i2 = int(input("Введите конец диапазона для генерации целого числа: "))
print("Случайное целое число: %d" % random.randint(i1, i2))

f1 = float(input("Введите начало диапазона для генерации вещественного числа: "))
f2 = float(input("Введите конец диапазона для генерации вещественного числа: "))
print("Случайное вещественное число: %f" % random.uniform(f1, f2))

l1 = input("Введите начало диапазона для генерации буквы (a-z): ")
l2 = input("Введите конец диапазона для генерации буквы (a-z): ")
letters = 'abcdefghijklmnopqrstuvwxyz'
li1 = letters.find(l1.lower())
li2 = letters.find(l2.lower())
print("Случайная буква: %s" % letters[random.randint(li1, li2)])