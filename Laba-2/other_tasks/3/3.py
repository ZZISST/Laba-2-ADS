import time
from psutil import Process
from os import getpid

time_start = time.time()

# Writing a Score function
def score(a):
    n = len(a)
    k = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                dope = a[j]
                a[j] = a[j+1]
                a[j+1] = dope
                k+=1
    return k

# Open input.txt file
with open('input.txt', 'r', encoding='UTF-8') as file:
    n = int(file.readline())
    a = list(map(int, file.readline().split()))

# Calling a score funtion
k = score(a)

# Writing a function result into output.txt
with open('output.txt', 'w', encoding='UTF-8') as file:
    file.write(str(k))


time_end = time.time() - time_start

print('Затраты памяти:', Process(getpid()).memory_info().rss / 1024 ** 2, 'В Мб')
print('Время работы программы в секундах', time_end)
