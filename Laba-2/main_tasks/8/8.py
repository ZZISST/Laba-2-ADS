import time
from psutil import Process
from os import getpid

time_start = time.time()

# Open input.txt file
with open('input.txt', 'r', encoding='UTF-8') as file:
    n = int(file.readline())
    a = list(map(int, file.readline().split()))
    b = list(map(int, file.readline().split()))

# Multiplication of polynomials
res = [0] * (2*n + 1)
for i in range(n):
    for j in range(n):
        res[i+j]+=(a[i]*b[j])

while 0 in res:
    res.pop(res.index(0))

# Writing result into output.txt
with open('output.txt', 'w', encoding='UTF-8') as file:
    file.write(' '.join(list(map(str, res))))


time_end = time.time() - time_start

print('Затраты памяти:', Process(getpid()).memory_info().rss / 1024 ** 2, 'В Мб')
print('Время работы программы в секундах', time_end)