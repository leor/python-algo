'''
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
'''

a = input("Введите число: ")
newNum = ''
index = len(a)

while index:
    index -= 1
    newNum += a[index]

print("Перевёрнутая версия числа: %s" % newNum)