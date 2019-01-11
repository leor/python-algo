year = int(input("Введите год (например 1970): "))

# вариант 1
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Год високосный")
        else:
            print("Год не високосный")
    else:
        print("Год високосный")
else:
    print("Год не високосный")

# вариант 2
import calendar

if calendar.isleap(year):
    print("Год високосный")
else:
    print("Год не високосный")
