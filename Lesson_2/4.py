"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def recursion(iterations_left, value, summ):
    iterations_left -= 1
    summ += value

    #print(value)
    value *= -0.5
    if iterations_left > 0:
        return recursion(iterations_left, value, summ)
    else:
        return summ


last_member = int(input('Введите номер элемента'))
print(f'Summ: {recursion(last_member, 1, 0)}')
