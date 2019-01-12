x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

k = (y2-y1)/(x2-x1)
b = y1 - k*x1

print("Уравнение прямой имеет вид y = %sx + %s" % (k, b))