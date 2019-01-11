a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
c = int(input("Введите число C: "))

if a > b > c:
    print("B - среднее число")
elif b > c > a:
    print("C - среднее число")
else:
    print("A - среднее число")
