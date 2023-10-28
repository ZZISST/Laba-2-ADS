import time
from psutil import Process
from os import getpid

time_start = time.time()

# Writing a BinarySearch function
def BinarySearch(lys, val):
    first = 0 # начальный индекс массива
    last = len(lys)-1 # Последний индекс массива
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index

# Open input.txt file
with open('input.txt', 'r', encoding='UTF-8') as file:
    n = int(file.readline())
    lys = list(map(int, file.readline().split()))
    ka = int(file.readline())
    k = list(map(int, file.readline().split()))

# Вызов функции для каждого числа
for i in range(len(k)):
    k[i] = BinarySearch(lys, k[i])

# Writing indexes into output.txt
with open('output.txt', 'w', encoding='UTF-8') as file:
    file.write(' '.join(map(str, k)))

time_end = time.time() - time_start

print('Затраты памяти:', Process(getpid()).memory_info().rss / 1024 ** 2, 'В Мб')
print('Время работы программы в секундах', time_end)