'''
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
'''

k = int(input("Введите длину последовательности: "))

max = 0
sum = 0

for i in range(k):
    n = input("Введите число: ")

    if int(n) > max:
        max = int(n)
        sum = 0

        for j in range(len(n)):
            sum += int(n[j])

print("Наибольшее число: %d; Сумма его цифр: %d" % (max, sum))