'''
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''

# кол-во строк
N = int(input("Введите количество строк матрицы: "))
# кол-во столбцов
M = int(input("Введите количество столбцов матрицы: "))

a = [[int(input("Введите элемент %dx%d: " % (i, j))) for j in range(M)] for i in range(N)]

print("Матрица: ")
for b in a:
    print(' | '.join([str(i) for i in b]))

min_list = []
for i in range(N):
    min_list.append(min([v[i] for v in a]))

print("Максимальный элемент среди минимальных элементов столбцов матрицы: %d" % max(min_list))
