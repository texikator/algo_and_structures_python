"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

from random import random


l_border = input('Левая граница: ')
r_border = input('Правая граница: ')

try:
    l_border = int(l_border)
    r_border = int(r_border)

except ValueError: 
    pass


def rnd(l_border, r_border, result_type):
    if l_border > r_border:
        max = l_border
        min = r_border

    elif r_border > l_border:
        max = r_border
        min = l_border
    else:
        return False

    if result_type == 1:
        rnd = int(random() * (max - min) + min)

    elif result_type == 2:
        rnd = random() * (max - min) + min

    return rnd


if isinstance(l_border, str) and isinstance(r_border,str):

    l_border = ord(l_border)
    r_border = ord(r_border)    

    print(f'Случайный символ в интервал {chr(rnd(l_border, r_border, 1))}')

elif isinstance(l_border, int) and isinstance(r_border, int):

    result_type = int(input(
        'Нужно целое (1)  или вещественное (2) число в заданном интервале? :'))
    print(f'Случайное число в заданном интервале {rnd(l_border, r_border, result_type)}')


else:
    print('Ошибка ввода.')


