"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""


def func(a, b, f):
    if f == '+' or f == '-' or f == '/' or f == '*':

        if f == '/' and b == 0:
            return 'Деление на ноль невозможно'

        if f == '+':
            return a + b
        elif f == '-':
            return a - b
        elif f == '/':
            return a / b
        else:
            return a * b

    elif f == '0':
        quit()
    else:
        return 'Ошибочная операция'



while True:
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    f = input('Введите операцию (/,*,-,+ или 0 для выхода: ')
    print(f'{a}{f}{b} = {func(a, b, f)}')


