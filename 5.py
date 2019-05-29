#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
import random

low_bound = -100
high_bound = 100
length = int(input('Введите длину массива: '))
array = [random.randrange(low_bound, high_bound) for i in range(length)]

max_index = 0
max = array[max_index]

for ind, val in enumerate(array):
    if val < 0:
        if val > low_bound:
            max_index = ind
            max = val

print(f'Массив: {array}')
print(f'Максимальное значение {max}, его индекc {max_index}')