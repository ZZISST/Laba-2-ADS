import time
from psutil import Process
from os import getpid

time_start = time.time()
# Writing a merge_sort function
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
        return arr

# open input.txt file
with open('input.txt', 'r', encoding='UTF-8') as file:
    n = int(file.readline())
    a = list(map(int, file.readline().split()))



a = merge_sort(a)



# Writing a function result into output.txt
with open('output.txt', 'w', encoding='UTF-8') as file:
    file.write(' '.join(list(map(str, a))))


time_end = time.time() - time_start

print('Затраты памяти:', Process(getpid()).memory_info().rss / 1024 ** 2, 'В Мб')
print('Время работы программы в секундах', time_end)