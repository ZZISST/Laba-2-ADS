import time
from psutil import Process
from os import getpid

time_start = time.time()

# Writing a Find_Max_Crossing_Subarray function
def find_Max_subarray(array):
    max_sum = 0
    summ = 0
    start_index = 0
    end_index = 0

    for i in range(len(array)):

        if summ == 0:
            start_index = i

        summ += array[i]

        if max_sum < summ:
            max_sum = summ
            end_index = i

        if summ < 0:
            summ = 0

    return [start_index, end_index, max_sum]


# Open input.txt file
with open('input.txt', 'r', encoding='UTF-8') as file:
    n = int(file.readline())
    a = list(map(float, file.readline().split()))

# Находим начало/конец/сумму максимальной подпоследовательности
res = find_Max_subarray(a)
start, end, suma = res[0], res[1], res[2]

# Записываем ответ
with open('output.txt', 'w', encoding='UTF-8') as file:
    file.write(str(start)+' '+str(end)+' '+str(suma))

time_end = time.time() - time_start

print('Затраты памяти:', Process(getpid()).memory_info().rss / 1024 ** 2, 'В Мб')
print('Время работы программы в секундах', time_end)