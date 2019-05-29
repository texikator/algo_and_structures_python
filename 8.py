"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
import random

len_x = 4
len_y = 4

#array = [random.randrange(0, 100) for i in range(20)]
array = (input(f'Введите разделенные пробелами {len_x*len_y} чисел: ')).split(' ')


print (array)
def fill_matrix(array):
    iterator = 0
    matrix = [[0 for i in range(len_x+1)] for i in range(len_y)]

    for i in range(len_y):
        for j in range(len_x):
                matrix[i][j] = int(array[iterator])
                iterator += 1
    return matrix

def print_matrix(array):
    for i in range(len_y):
        for j in range(len_x+1):
            print(f'{array[i][j]:2}', end=" ")
        print("")

def calc_matrix(array):
    for i in range(len_y):
        summ = 0
        for j in range(len_x):
            summ += array[i][j]
        array[i][len_x] = summ
    return array

matrix = fill_matrix(array)
new_matrix = calc_matrix(matrix) 
print_matrix(new_matrix)

