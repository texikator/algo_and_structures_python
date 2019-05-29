# 4.	Определить, какое число в массиве встречается чаще всего.

import random

length = int(input('Введите длину массива: '))
array = [random.randrange(0,10) for i in range(length)]
unique = list(set(array))
counters = [0 for i in range(len(unique))]

#for i in range(length):
#    for j in range(len(unique)):
#        if array[i] == unique[j]:
#            counters[j] += 1


#for value in array:
#    for uniq_idx, uniq_val in enumerate(unique):
#        if value == uniq_val:
#            counters[uniq_idx] += 1

print(counters)
counters = [0 for i in range(len(unique))]

def func(array, unique, counters=counters, position=0):
    for i in range(len(unique)):
        if array[position] == unique[i]:
            counters[i] += 1

    position += 1
    if position < length:
        return func(array, unique, counters, position)
    else:
        return counters


counters = func(array, unique)

max_index = 0
max = counters[max_index]

for i in range(len(counters)):
    if counters[i] > max:
        max = counters[i]
        max_index = i

print(f'Исходный массив: {array}')
print(f'Уникальные элементы:   {unique}')
print(f'Количество повторений: {counters}')
print(f'Чаще всего встречается {unique[max_index]}')
