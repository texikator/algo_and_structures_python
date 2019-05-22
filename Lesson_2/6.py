"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

from random import random

min_border = 0
max_border = 100
shots = 10


def game(shots_left, rnd):
    shot = int(input(f'осталось {shots_left} попыток. Введите число: '))

    if shot > rnd:
        print('перелет')
    elif shot < rnd:
        print('недолет')
    else:
        return f'угадал! это число {shot}'

    shots_left -= 1

    if shots_left == 0:
        return f'Game over. this number is {rnd}'
    else:
        return game(shots_left, rnd)


rnd = int(random() *(max_border - min_border) + min_border)

print(game(10, rnd))

