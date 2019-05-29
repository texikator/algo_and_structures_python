#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
import random
length = int(input('Введите длину массива: '))
array = [random.randrange(-100, 100) for i in range(length)]

min_index  = 0 
min = array[0]
max_index = 0  
max = array[0]

#for i in range(length):
#    if array[i] < min:
#        min_index = i
#        min = array[i]
#    if array[i] > max:
#        max_index = i
#        max = array[i]

for idx, value in enumerate(array):
    if value < min:
        min_index = idx
        min = value
    if value > max:
        max_index = idx
        max = value




print(f'Исходный массив: {array}')
array[min_index] = max
array[max_index] = min
print(f'max_index: {max_index}, max_value: {max}, min_index: {min_index}, min_value: {min}')
print(f'Преобразованный массив: {array}')
