'''
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
'''

c = 0
str = ''
for i in range(32, 128):
    str += "%s = %s | " % (i, chr(i))
    c += 1

    if c == 10 or i == 127:
        print(str)
        str = ''
        c = 0