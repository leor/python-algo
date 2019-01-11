letters = 'abcdefghijklmnopqrstuvwxyz'
l1 = input("Введите первую букву (a-z): ")
l2 = input("Введите вторую букву (a-z): ")

li1 = letters.find(l1.lower())
li2 = letters.find(l2.lower())

print("Буква '%s' находится на позиции %d" % (l1, li1+1))
print("Буква '%s' находится на позиции %d" % (l2, li2+1))
print("Между буквами '%s' и '%s' есть ещё %d букв(ы)" % (l1, l2, li2-li1-1))