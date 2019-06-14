"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

import random

m = 2
array = [random.randrange(-1000, 1000) for i in range(2*m+1)]
#array = [328, -875, -823, -164, 370] #-164
print(array)
def get_mediana(array):
    for c_item in range(len(array)):
        left_array = []
        right_array = []

        for item in array:
            if item < array[c_item]:
                left_array.append(item)
            elif item > array[c_item]:
                right_array.append(item)

        if len(left_array) == len(right_array):
            return array[c_item]

print(f'Медиана массива: {get_mediana(array)}')





