# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

len_x = int(input('Количество столбцов: '))
len_y = int(input('Количество строк: '))
low = -100
high = 100

matrix = [[random.randrange(low, high) for i in range(len_x)] for i in range(len_y)]
min_elements = [0 for i in range(len_x)]


def print_matrix(array):
    for i in range(len_y):
        for j in range(len_x):
            print(f'{array[i][j]:3}', end=' ')
        print("")
    print("____")
    for i in min_elements:
        print(f'{i:3}', end=' ')
    print('')


for j in range(len_x):
    min = matrix[0][j]
    for i in range(len_y):
        #print(f'{matrix[i][j]:3}', end='')
        if matrix[i][j] < min:
            min = matrix[i][j]
    min_elements[j] = min
    print("")

max = min_elements[0]
for element in min_elements:
    if max < element:
        max = element

print_matrix(matrix)
print("____")
print(f'Максимальный элемент: {max}')
#print(min_elements)
