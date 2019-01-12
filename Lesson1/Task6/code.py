letters = 'abcdefghijklmnopqrstuvwxyz'
p = int(input("Введите номер буквы в алфавите (a-z): "))

if p == 0 or p > len(letters):
    print("Указана позиция за пределами алфавита")
else:
    print("Это буква %s" % letters[p-1])