"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
import random

low_bound = -100
high_bound = 100
result = [high_bound, high_bound]


#сравнить число с максимумом в result, если меньше - заменить значение
def replace_max(num, result, max):
    max_idx = 0
    max = result[max_idx]
    for idx, val in enumerate(result):
        if max <= val:
            max = val
            max_idx = idx
    if num <= max:
        result[max_idx] = num
    return result

length = int(input('Введите длину массива: '))
array = [random.randrange(low_bound, high_bound) for i in range(length)]


for val in array:
    replace_max(val, result, max)

print(f'Массив: {array}')
print(f'Минимальные значения: {result}')
