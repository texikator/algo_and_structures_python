"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random

length = int(input('Введите длину масива: '))
low_bound = -100
high_bound = 100

array = [random.randrange(low_bound, high_bound) for i in range(length)]

max = low_bound
max_index = 0

min = high_bound
min_index = 0

for idx, value in enumerate(array):
    if value > max:
        max = value
        max_index = idx
    if value < min:
        min = value
        min_index = idx

print(array)
print(f'max_index: {max_index}, max_value: {max}, min_index: {min_index}, min_value: {min}')

if max_index < min_index:
    (min_index, max_index) = (max_index, min_index)

print(min_index, max_index)

for i in range(min_index, max_index):
    print(i, print(array[i]), end = " ")
