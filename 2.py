"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

import random
import timeit

array = [random.randrange(0, 50) for i in range(500)]

array = [-29, 36, -12, 11, 68, 75, -24, -22, 82, 25, -14, 98, -46, -88, 95, -41, 98, 92, -33, 75, 92, 9, -88, -30, 94, 76, 99, -8, 20, 9, 12, 90, 4,
         -76, -58, 16, 1, -58, -80, -49, 42, -9, -90, -23, 33, 14, 23, 29, 23, 34, -
         97, -36, 4, 71, -83, -51, -77, -52, 62, 42, 99, -59, -100, -76, -62, -60,
         85, -71, -61, 11, 84, 41, 3, 30, -8, 41, -35, -14, 82, -6, -31, -59, 69, -
         12, -39, 24, -51, 84, -46, -50, -21, 20, 95, -10, -3, -4, -49, -63, -97,
         71, -94, 96, -48, 44, 59, -17, -23, -61, 3, -46, 74, 86, -20, 41, -93, -
         48, -76, 34, -53, 69, -87, 56, -98, -92, -25, -38, 34, 30, 39, -22, 76, 60,
         -29, 79, -21, 58, 16, 22, 80, 19, -13, 69, 92, -1, 94, -41, -80, 33, -51, -
         83, -98, -10, 42, -27, -74, -27, 28, -52, 85, -10, -99, 68, 47, -96, -69,
         71, -67, -86, 50, 64, 85, 58, -48, 46, 71, -83, 16, 28, 95, 96, -36, 99, 88, -
         12, -32, -23, -94, -27, -5, 31, 26, 33, -22, -49, -32, -25, 84, -51,
         -70, 54]



print(f'Исходный массив: {array}')


def get_sorted(orig_array):
    if len(orig_array) > 1:
        center = len(orig_array) // 2
        left_array = orig_array[:center]
        right_array = orig_array[center:]

        get_sorted(left_array)
        get_sorted(right_array)

        i, j, k = 0, 0, 0
        
        while i < len(left_array) and j < len(right_array):

            if left_array[i] < right_array[j]:
                orig_array[k] = left_array[i]
                i += 1
            else:
                orig_array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            orig_array[k] = left_array[i]

            i += 1
            k += 1

        while j < len(right_array):
            
            orig_array[k] = right_array[j]
            j += 1
            k += 1

    return orig_array

print(f'Отсортированный массив {get_sorted(array)}')

print(timeit.timeit('get_sorted(array)', setup='from __main__ import get_sorted, array', number=100))

