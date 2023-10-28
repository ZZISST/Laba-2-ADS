import time
from psutil import Process
from os import getpid

time_start = time.time()

# Open input.txt file and
with open('input.txt', 'r', encoding='UTF-8') as file:
    n = int(file.readline())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i] = list(map(int, file.readline().split()))
    for i in range(n):
        y[i] = list(map(int, file.readline().split()))

# Результативный массив
matr = [[0]*n for i in range(n)]

# Записываем в рез. массив перемноженные эллементы
for i in range (n):
    for q in range (n):
        for k in range (n):
            matr[i][q] += x[i][k] * y[k][q]


with open('output.txt', 'w', encoding='UTF-8') as file:
    for i in range(n):
        file.write('\n')
        for j in range(n):
            file.write(str(matr[i][j])+' ')


time_end = time.time() - time_start

print('Затраты памяти:', Process(getpid()).memory_info().rss / 1024 ** 2, 'В Мб')
print('Время работы программы в секундах', time_end)