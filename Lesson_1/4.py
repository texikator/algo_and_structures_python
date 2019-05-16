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

result_type = input('Нужно целое (1)  или вещественное (2) число в заданном интервале? :')

if instance(a, str)
if l_border > r_border:
    max = l_border
    min = r_border
elif r_border > l_border:
    max = r_border
    min = l_border
else:
    print('Границы равны')
    quit()

if result_type == 1:
    rnd = int(random*(max - min) + min)
elif result_type ==2:
    rnd = random*(max - min ) + min


